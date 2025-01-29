import logging
from datetime import datetime


class TradingLogger:
    def __init__(self):
        self.logger = logging.getLogger('trading_bot')
        self._setup_logger()

    def _setup_logger(self):
# Logging configuration