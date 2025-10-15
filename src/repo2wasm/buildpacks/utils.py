import logging
import re

logger = logging.getLogger(__name__)


def clean_dependency(dependency, forgiving=False):
    # Documented in PEP 440 – Version Identification and Dependency Specification,
    # see https://peps.python.org/pep-0440/.
    #
    # Documented in Conda's Package match specifications,
    # see https://docs.conda.io/projects/conda-build/en/latest/resources/package-spec.html#package-match-specifications.
    if not forgiving:
        return dependency

    dependency = dependency.strip().split()
    if len(dependency) > 1:
        return dependency[0]

    dependency = dependency[0]

    match = re.match(r"([\w\-]+)[><!=~]+", dependency)
    if match:
        return match.group(1)

    logger.warning("Fail to remove the version number in '%s'", dependency)

    return dependency
