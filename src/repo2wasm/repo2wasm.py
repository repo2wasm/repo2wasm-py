import logging
import os.path

from .binder import get_buildpack

logger = logging.getLogger(__name__)


def repo2wasm(repository, ide="jupyterlab", output_dir="public"):
    repository_absolute_path = os.path.abspath(repository)
    output_dir_absolute_path = os.path.abspath(output_dir)

    logger.info("Repository: %s", repository_absolute_path)
    logger.info("Integrated development environment (IDE): %s", ide)
    logger.info("Output directory: %s", output_dir_absolute_path)

    buildpack = get_buildpack(repository_absolute_path, ide, output_dir)

    buildpack.doit_run("build")
    buildpack.doit_run("post_build")
