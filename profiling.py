from time import time

import logging


class LogTimer(object):
    def __init__(self, description, logger=None):
        if not logger:
            self.logger = logging.getLogger(__name__)
        else:
            self.logger = logger
        self.description = description
        self.logger.setLevel(logging.DEBUG)

    def __enter__(self):
        self.start = time()

    def __exit__(self, type, value, traceback):
        self.end = time()
        self.duration = self.end - self.start
        self.logger.debug(f"{self.description}: {self.duration}")
