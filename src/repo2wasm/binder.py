import logging
import os.path

from .buildpacks.conda import CondaBuildPack
from .buildpacks.requirements import RequirementsBuildPack
from .buildpacks.install import InstallBuildPack

logger = logging.getLogger(__name__)

ALLOWED_BINDER_DIR = [".binder", "binder", "."]

ALLOWED_BINDER_CONFIGURATION_MAPPING = {
    "environment.yml": CondaBuildPack,
    "requirements.txt": RequirementsBuildPack,
    "install.R": InstallBuildPack,
}


def find_configuration_file(path_to_repository):
    for configuration_file in ALLOWED_BINDER_CONFIGURATION_MAPPING:
        for binder_dir in ALLOWED_BINDER_DIR:
            file_path = os.path.join(path_to_repository, binder_dir, configuration_file)
            logger.debug("Searching for %s ...", file_path)
            if os.path.isfile(file_path):
                logger.debug("Found %s", file_path)
                return file_path

    raise RuntimeError("Configuration file not found.")


def get_buildpack(path_to_repository, ide, output_dir, forgiving=False):
    configuration_file_path = find_configuration_file(path_to_repository)

    configuration_file = os.path.basename(configuration_file_path)

    for (
        buildpack_configuration_file,
        BuildPack,
    ) in ALLOWED_BINDER_CONFIGURATION_MAPPING.items():
        if configuration_file == buildpack_configuration_file:
            return BuildPack(
                path_to_repository, configuration_file_path, ide, output_dir, forgiving
            )

    raise RuntimeError("Build pack not found.")
