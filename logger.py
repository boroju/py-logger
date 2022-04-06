import datetime as dt
import logging
import os

class Logger():

    def __init__(self, log_directory, log_file_app, vendor_name, vendor_product):
        os.umask(0o002)
        self._log_file_app = log_file_app
        self._log_directory = self._check_log_file_path(log_directory)
        self._vendor_name = vendor_name
        self._vendor_product = vendor_product

        # create the log file name using current date time
        self._log_file_name = f'{dt.datetime.today().strftime("%Y%m%d_%H%M%S")}.log'
        self._log_file = os.path.join(self._log_directory, self._log_file_name)

        self._logger = self._setup_logging()

    def _setup_logging(self):
        # Create root logger
        logger = logging.getLogger(self._log_file_app)
        logger.setLevel(logging.DEBUG)

        # Create a file and console log handler and set the log levels to DEBUG
        fh = logging.FileHandler(self._log_file)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger

    def debug(self, msg: str):
        self._logger.debug(msg)
    
    def info(self, msg: str):
        self._logger.info(msg)

    def warning(self, msg: str):
        self._logger.warning(msg)

    def error(self, msg: str):
        self._logger.error(msg)

    def critical(self, msg: str):
        self._logger.critical(msg)

    def _check_log_file_path(self, path):
        if isinstance(path, str):
            if not os.path.exists(path):
                os.makedirs(path)
            _path = path
        else:
            raise TypeError(f'Path is not a valid string: [{path}]')
        return _path