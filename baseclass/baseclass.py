import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup", "login")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # Check if logger already has handlers
        if not logger.handlers:
            fileHandler = logging.FileHandler('D://Seleniumx//logs//' + 'logfile.log', mode='a')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(filename)s : %(funcName)s :%(message)s")
            fileHandler.setFormatter(formatter)
            logger.addHandler(fileHandler)
            logger.setLevel(logging.DEBUG)

        return logger

