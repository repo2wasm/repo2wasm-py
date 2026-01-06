import logging
import os.path

from .buildpacks.conda import CondaBuildPack
from .buildpacks.requirements import RequirementsBuildPack
from .buildpacks.install import InstallBuildPack

logger = logging.getLogger(__name__)

# As documented in https://repo2docker.readthedocs.io/en/latest/specification/
ALLOWED_REPO2DOCKER_DIR = [".binder", "binder", "."]

ALLOWED_REPO2DOCKER_CONFIGURATION_MAPPING = {
    "environment.yml": CondaBuildPack,
    "requirements.txt": RequirementsBuildPack,
    "install.R": InstallBuildPack,
}

# As documented in https://notebook.link/docs/user-guide/enable-your-github-repository#define-the-environment
ALLOWED_NOTEBOOK_LINK_DIR = [".nblink", "."]

ALLOWED_NOTEBOOK_LINK_CONFIGURATION_MAPPING = {
    "environment.yml": CondaBuildPack,
}

CONFIGURATION_PROVIDERS = {
    "repo2docker": (ALLOWED_REPO2DOCKER_CONFIGURATION_MAPPING, ALLOWED_REPO2DOCKER_DIR),
    "notebook.link": (
        ALLOWED_NOTEBOOK_LINK_CONFIGURATION_MAPPING,
        ALLOWED_NOTEBOOK_LINK_DIR,
    ),
}


def get_buildpack(path_to_repository, ide, output_dir, forgiving=False):
    configuration_file_path = None
    BuildPack = None

    for provider, (
        configuration_mapping,
        allowed_dir,
    ) in CONFIGURATION_PROVIDERS.items():
        logger.debug("Testing for %s as provider ...", provider)
        for configuration_file in configuration_mapping:
            for binder_dir in allowed_dir:
                file_path = os.path.join(
                    path_to_repository, binder_dir, configuration_file
                )
                logger.debug("Searching for %s ...", file_path)
                if os.path.isfile(file_path):
                    logger.debug("Found %s", file_path)
                    configuration_file_path = file_path
                    BuildPack = configuration_mapping[configuration_file]
                    break

            if configuration_file_path is not None:
                break

        if configuration_file_path is not None:
            break

    if configuration_file_path is None:
        raise RuntimeError("Configuration file not found.")

    return BuildPack(
        path_to_repository, configuration_file_path, ide, output_dir, forgiving
    )
