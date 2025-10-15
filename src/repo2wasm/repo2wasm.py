import logging
import os.path
import tempfile

from repo2docker import contentproviders

from .binder import get_buildpack
from .buildpacks.exceptions import Repo2WasmError

logger = logging.getLogger(__name__)

content_providers = [
    contentproviders.Local,
    contentproviders.Zenodo,
    contentproviders.Figshare,
    contentproviders.Dataverse,
    contentproviders.Swhid,
    contentproviders.Mercurial,
    contentproviders.Git,
]


def fetch_repository(repository):
    for ContentProvider in content_providers:
        cp = ContentProvider()
        spec = cp.detect(repository)
        if spec is not None:
            picked_content_provider = cp
            logger.info(
                "Picked {cp} content provider.\n".format(cp=cp.__class__.__name__)
            )
            break
    else:
        RuntimeError(
            "No matching content provider found for {repository}.".format(
                repository=repository
            )
        )

    if cp.__class__.__name__ == "Local":
        checkout_path = repository
    else:
        checkout_path = tempfile.mkdtemp(prefix="repo2wasm-")

    for log_line in picked_content_provider.fetch(
        spec, checkout_path, yield_output=True
    ):
        logger.info(log_line, extra=dict(phase="fetching"))

    return checkout_path


def repo2wasm(repository, ide="jupyterlab", output_dir="public", forgiving=False):
    output_dir_absolute_path = os.path.abspath(output_dir)

    logger.info("Repository: %s", repository)
    logger.info("Integrated development environment (IDE): %s", ide)
    logger.info("Output directory: %s", output_dir_absolute_path)

    checkout_path = fetch_repository(repository)
    try:
        buildpack = get_buildpack(checkout_path, ide, output_dir, forgiving)

        buildpack.doit_run("build")
        buildpack.doit_run("post_build")
    except Repo2WasmError as error:
        logger.error(error)
