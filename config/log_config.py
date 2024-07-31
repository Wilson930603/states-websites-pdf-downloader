import logging
import os
from datetime import datetime


class ContextLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        return f'{{{self.extra["context"]}}} - {msg}', kwargs


def setup_logging():
    logger = logging.getLogger()
    if not logger.handlers:  # Check if handlers already exist
        logs_dir = "logs"  # TODO: Check lateer
        os.makedirs(
            logs_dir, exist_ok=True
        )  # Create logs directory if it doesn't exist

        # Timestamp for unique log file names
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = os.path.join(logs_dir, f"log_{timestamp}.log")

        logger.setLevel(logging.DEBUG)

        # Console Handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # File Handler
        fh = logging.FileHandler(log_filename)
        fh.setLevel(logging.INFO)

        # Formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Add handlers to the logger
        logger.addHandler(ch)
        logger.addHandler(fh)
