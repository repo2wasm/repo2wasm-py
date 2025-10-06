import logging
import os
import tempfile

import yaml

from .base import BaseBuildPack

logger = logging.getLogger(__name__)


class CondaBuildPack(BaseBuildPack):
    def __init__(self, repository, configuration_file, ide, output_dir):
        super().__init__(repository, configuration_file, ide, output_dir)

        logger.debug("Configuration file: %s", self.configuration_file)

        with open(self.configuration_file, "r") as _file:
            configuration_yaml = yaml.safe_load(_file)

        if "name" not in configuration_yaml:
            logger.info('Environment\'s name is missing. Using "repo2wasm".')
            configuration_yaml["name"] = "repo2wasm"

        if "channels" not in configuration_yaml:
            configuration_yaml["channels"] = []

        logger.info("Prepending conda channels provided by Prefix.")
        configuration_yaml["channels"] = [
            "https://repo.prefix.dev/emscripten-forge-dev",
            "https://repo.prefix.dev/conda-forge",
            *configuration_yaml["channels"],
        ]

        if "dependencies" not in configuration_yaml:
            logger.info("Environment's dependencies is missing. Using empty list.")
            configuration_yaml["dependencies"] = []

        requires_r = False
        for dependency in configuration_yaml["dependencies"]:
            if dependency.startswith("r-"):
                logger.debug("Found r-* dependency.")
                requires_r = True
                break
        if requires_r:
            for dependency in configuration_yaml["dependencies"]:
                if dependency.startswith("xeus-r"):
                    break
            else:
                logger.debug("Adding xeus-r as dependency.")
                configuration_yaml["dependencies"].append("xeus-r")

        for dependency in configuration_yaml["dependencies"]:
            if dependency.startswith("xeus-python"):
                break
        else:
            logger.debug("Adding xeus-python as dependency.")
            configuration_yaml["dependencies"].append("xeus-python")

        _file_descriptor, _file_path = tempfile.mkstemp(
            suffix=".yml", prefix="repo2wasm-"
        )
        logger.debug("Created temporary file %s", _file_path)
        with os.fdopen(_file_descriptor, "w") as _file:
            yaml.dump(configuration_yaml, _file)

        self._addons["jupyterlite-xeus"].environment_file.append(_file_path)
