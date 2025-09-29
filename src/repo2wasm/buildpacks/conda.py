import logging

from .base import BaseBuildPack

logger = logging.getLogger(__name__)


class CondaBuildPack(BaseBuildPack):
    def __init__(self, repository, configuration_file, ide, output_dir):
        super().__init__(repository, configuration_file, ide, output_dir)
