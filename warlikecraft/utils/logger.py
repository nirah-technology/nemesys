from datetime import datetime
from enum import Enum
from pathlib import Path
from types import NoneType
from colorama import init, Fore

init(autoreset=True)

class LogLevel(Enum):
    DEBUG=0
    INFO=1,
    WARNING=2
    ERROR=3

class Logger:
    def __init__(self, name: type, filename: Path|NoneType=None) -> None:
        self.__name: str = "{}.Menu(parent=self)
        # menu.display(){}".format(name.__module__, name.__name__)

    def log(self, level: LogLevel, message: object):
        color = Fore.RESET
        match(level):
            case LogLevel.DEBUG:
                color = Fore.MAGENTA
            case LogLevel.INFO:
                color = Fore.CYAN
            case LogLevel.WARNING:
                color = Fore.YELLOW
            case LogLevel.ERROR:
                color = Fore.RED

            case _:
                color = Fore.RESET
        print("{}{} {} - {}".format(color, datetime.now(), self.__name, message))

    def debug(self, message: object):
        self.log(LogLevel.DEBUG, message)
    def info(self, message: object):
        self.log(LogLevel.INFO, message)
    def warning(self, message: object):
        self.log(LogLevel.WARNING, message)
    def error(self, message: object):
        self.log(LogLevel.ERROR, message)