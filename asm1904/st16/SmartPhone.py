# -*- coding: utf-8 -*-

from Phone import Phone
from OS import WithOS
from RAM import EnterRAM


class SmartPhone(Phone):

    def __init__(self):
        self.OS = WithOS()
        self.RAM = EnterRAM()
