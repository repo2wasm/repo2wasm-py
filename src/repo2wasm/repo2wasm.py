import logging

logger = logging.getLogger(__name__)


def repo2wasm(repository, ide="jupyterlab", output_dir="public"):
    logger.info("Repository: %s", repository)
    logger.info("Integrated development environment (IDE): %s", ide)
    logger.info("Output directory: %s", output_dir)
