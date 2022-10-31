from abc import ABCMeta, abstractmethod

import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

import sys
from datetime import datetime
from typing import Optional


DEFAULT_LEVEL = logging.INFO
DEFAULT_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
DEFAULT_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ISPLogger(metaclass=ABCMeta):

    __name: str
    __logger: logging.Logger

    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'configure') and
                callable(subclass.configure) and
                hasattr(subclass, '__add_handlers') and
                callable(subclass.__add_handlers) and
                hasattr(subclass, 'debug') and
                callable(subclass.debug) and
                hasattr(subclass, 'info') and
                callable(subclass.info) and
                hasattr(subclass, 'warning') and
                callable(subclass.warning) and
                hasattr(subclass, 'error') and
                callable(subclass.error) and
                hasattr(subclass, 'critical') and
                callable(subclass.critical) or
                False)

    @staticmethod
    @abstractmethod
    def configure(name: str, level: int, format: str, date_format: str, filename: Optional[str] = None,
                  when: Optional[str] = None) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def __add_handlers(level: int, formatter: logging.Formatter) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def debug(msg: str) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def info(msg: str) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def warning(msg: str) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def error(msg: str) -> None:
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def critical(msg: str) -> None:
        raise NotImplementedError


class ConsoleLogger(ISPLogger):

    @staticmethod
    def configure(name: str, level: int = DEFAULT_LEVEL, fmt: str = DEFAULT_FORMAT,
                  date_fmt: str = DEFAULT_DATE_FORMAT) -> None:

        ConsoleLogger.__name = name
        ConsoleLogger.__logger = logging.getLogger(name)
        ConsoleLogger.__logger.setLevel(level)

        formatter = logging.Formatter(fmt=fmt, datefmt=date_fmt)

        ConsoleLogger.__add_handlers(level, formatter)

    @staticmethod
    def __add_handlers(level: int, formatter: logging.Formatter) -> None:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)
        ConsoleLogger.__logger.addHandler(stdout_handler)

    @staticmethod
    def debug(msg: str) -> None:
        ConsoleLogger.__logger.debug(msg)

    @staticmethod
    def info(msg: str) -> None:
        ConsoleLogger.__logger.info(msg)

    @staticmethod
    def warning(msg: str) -> None:
        ConsoleLogger.__logger.warning(msg)

    @staticmethod
    def error(msg: str) -> None:
        ConsoleLogger.__logger.error(msg)

    @staticmethod
    def critical(msg: str) -> None:
        ConsoleLogger.__logger.critical(msg)


class FileLogger(ISPLogger):

    __filename: str

    @staticmethod
    def configure(name: str, level: int = DEFAULT_LEVEL, fmt: str = DEFAULT_FORMAT,
                  date_fmt: str = DEFAULT_DATE_FORMAT,
                  filename: str = f'{datetime.now().strftime("%Y%m%d%H%M%S")}.log') -> None:

        FileLogger.__name = name
        FileLogger.__filename = filename

        FileLogger.__logger = logging.getLogger(name)
        FileLogger.__logger.setLevel(level)

        formatter = logging.Formatter(fmt=fmt, datefmt=date_fmt)

        FileLogger.__add_handlers(level, formatter)

    @staticmethod
    def __add_handlers(level: int, formatter: logging.Formatter) -> None:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)

        file_handler = TimedRotatingFileHandler(FileLogger.__filename, )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)

        FileLogger.__logger.addHandler(file_handler)
        FileLogger.__logger.addHandler(stdout_handler)

    @staticmethod
    def debug(msg: str) -> None:
        FileLogger.__logger.debug(msg)

    @staticmethod
    def info(msg: str) -> None:
        FileLogger.__logger.info(msg)

    @staticmethod
    def warning(msg: str) -> None:
        FileLogger.__logger.warning(msg)

    @staticmethod
    def error(msg: str) -> None:
        FileLogger.__logger.error(msg)

    @staticmethod
    def critical(msg: str) -> None:
        FileLogger.__logger.critical(msg)


class RotatingFileLogger(ISPLogger):

    __filename: str
    __when: str

    @staticmethod
    def configure(name: str, level: int = DEFAULT_LEVEL, fmt: str = DEFAULT_FORMAT,
                  date_fmt: str = DEFAULT_DATE_FORMAT,
                  filename: str = 'example_.log',
                  when: str = 'h') -> None:

        RotatingFileLogger.__name = name
        RotatingFileLogger.__filename = filename

        RotatingFileLogger.__when = when

        RotatingFileLogger.__logger = logging.getLogger(name)
        RotatingFileLogger.__logger.setLevel(level)

        formatter = logging.Formatter(fmt=fmt, datefmt=date_fmt)

        RotatingFileLogger.__add_handlers(level, formatter)

    @staticmethod
    def __add_handlers(level: int, formatter: logging.Formatter) -> None:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(level)
        stdout_handler.setFormatter(formatter)

        file_handler = RotatingFileHandler(RotatingFileLogger.__filename, when=RotatingFileLogger.__when)

        RotatingFileLogger.__logger.addHandler(file_handler)
        RotatingFileLogger.__logger.addHandler(stdout_handler)

    @staticmethod
    def debug(msg: str) -> None:
        RotatingFileLogger.__logger.debug(msg)

    @staticmethod
    def info(msg: str) -> None:
        RotatingFileLogger.__logger.info(msg)

    @staticmethod
    def warning(msg: str) -> None:
        RotatingFileLogger.__logger.warning(msg)

    @staticmethod
    def error(msg: str) -> None:
        RotatingFileLogger.__logger.error(msg)

    @staticmethod
    def critical(msg: str) -> None:
        RotatingFileLogger.__logger.critical(msg)
