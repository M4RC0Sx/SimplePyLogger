from abc import ABCMeta, abstractmethod
import logging
import sys
from datetime import datetime
from typing import Optional

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
    def configure(name: str, level: int, format: str, date_format: str, filename: Optional[str] = None) -> None:
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
