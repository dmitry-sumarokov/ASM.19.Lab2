# -*- coding: utf-8 -*-


class RAM:
    def input(self):
        raise NotImplementedError()


class ConstRAM(RAM):
    def input(self):
        return "16MB"


class EnterRAM(RAM):
    def input(self):
        return None
