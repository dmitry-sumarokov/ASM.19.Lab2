# -*- coding: utf-8 -*-

from Phone import Phone
from OS import NoOS
from RAM import ConstRAM


class MobilePhone(Phone):

    def __init__(self):
        self.OS = NoOS()
        self.RAM = ConstRAM()
