import logging
import os
import tempfile
from pathlib import Path

import yaml

from .base import BaseBuildPack
from .utils import clean_dependency

logger = logging.getLogger(__name__)


class RequirementsBuildPack(BaseBuildPack):
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
            "dependencies": ["xeus-python"],
        }

        with open(self.configuration_file, "r") as _file:
            requirements_txt = _file.readlines()

        if self.forgiving:
            configuration_yaml["dependencies"].extend(
                [clean_dependency(dependency) for dependency in requirements_txt]
            )

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
