import logging
import os
import tempfile
from pathlib import Path

import yaml

from . import exceptions
from .base import BaseBuildPack

logger = logging.getLogger(__name__)


def clean_line_from_install_r(line):
    if line.startswith("install.packages("):
        return line.replace('install.packages("', "").replace('")', "")

    return None


class InstallBuildPack(BaseBuildPack):
    def __init__(
        self, repository, configuration_file, ide, output_dir, forgiving=False
    ):
        super().__init__(repository, configuration_file, ide, output_dir, forgiving)

        logger.debug("Configuration file: %s", self.configuration_file)

        configuration_yaml = {
            "name": "repo2wasm",
            "channels": [
                "https://repo.prefix.dev/emscripten-forge-dev",
                "https://repo.prefix.dev/conda-forge",
            ],
            "dependencies": ["xeus-r"],
        }

        with open(self.configuration_file, "r") as _file:
            install_r = _file.readlines()

        raw_dependencies = [
            clean_line_from_install_r(dependency) for dependency in install_r
        ]

        configuration_yaml["dependencies"].extend(
            [
                f"r-{dependency}"
                for dependency in raw_dependencies
                if dependency is not None
            ]
        )

        for dependency in configuration_yaml["dependencies"]:
            if dependency.startswith("r-tidyverse"):
                raise exceptions.TidyVerseError()

        _file_descriptor, _file_path = tempfile.mkstemp(
            suffix=".yml", prefix="repo2wasm-"
        )
        logger.info("Created temporary configuration file %s", _file_path)
        with os.fdopen(_file_descriptor, "w") as _file:
            yaml.dump(configuration_yaml, _file)

        self._addons["jupyterlite-xeus"].environment_file.append(_file_path)
        self._addons["jupyterlite-xeus"].xeus_output_dir = (
            Path(self.output_dir) / "xeus"
        )
