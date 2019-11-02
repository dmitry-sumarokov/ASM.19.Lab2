# -*- coding: utf-8 -*-


class OS:
    def input(self):
        raise NotImplementedError()


class NoOS(OS):
    def input(self):
        return "NoOS"


class WithOS(OS):
    def input(self):
        return None
