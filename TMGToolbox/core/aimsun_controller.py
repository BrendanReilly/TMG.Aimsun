import sys
from PyANGKernel import *
from PyANGApp import *
from PyANGConsole import *
from PyANGKernel import *


class AimsunController:

    def __init__(self) -> None:
        self._console = ANGConsole()

    @property
    def console(self) -> ANGConsole:
        return self._console
