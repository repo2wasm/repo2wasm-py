import logging
import os.path

from .buildpacks.conda import CondaBuildPack

logger = logging.getLogger(__name__)

ALLOWED_BINDER_DIR = [".binder", "binder", "."]

ALLOWED_BINDER_CONFIGURATION = ["environment.yml"]


def find_configuration_file(path_to_repository):
    for configuration_file in ALLOWED_BINDER_CONFIGURATION:
        for binder_dir in ALLOWED_BINDER_DIR:
            file_path = os.path.join(path_to_repository, binder_dir, configuration_file)
            logger.debug("Searching for %s ...", file_path)
            if os.path.isfile(file_path):
                logger.debug("Found %s", file_path)
                return file_path

    raise RuntimeError("Configuration file not found.")


def get_buildpack(path_to_repository, ide, output_dir):
    configuration_file_path = find_configuration_file(path_to_repository)

    configuration_file = os.path.basename(configuration_file_path)

    if configuration_file == "environment.yml":
        return CondaBuildPack(
            path_to_repository, configuration_file_path, ide, output_dir
        )
    else:
        raise RuntimeError("Build pack not found.")
