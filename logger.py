import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler
import config


class LoggerConfig(object):

    def __init__(self):
        self.logger_name = 'root'

        logging.basicConfig(level=logging.DEBUG)

        self.add_stream_handler()
        self.add_file_handler()

    @property
    def logger(self):
        return logging.getLogger(self.logger_name)

    def add_stream_handler(self):

        handler = StreamHandler()
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s [%(pathname)s:%(lineno)d]'))
        logging.getLogger(self.logger_name).addHandler(handler)

    def add_file_handler(self):

        file_handler = RotatingFileHandler(config.LOGGER_PATH, maxBytes=1024*1024*500, delay=False, backupCount=20)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s [%(pathname)s:%(lineno)d]'))
        logging.getLogger(self.logger_name).addHandler(file_handler)


logger = LoggerConfig().logger

if __name__ == "__main__":

    logger.warning("warning...")