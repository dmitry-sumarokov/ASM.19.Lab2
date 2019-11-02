# -*- coding: utf-8 -*-


class Phone:
    OS = None
    RAM = None

    def set_data(self, args):
        self.brand = args['brand']
        self.screen_size = args['screen_size']
        self.housing_type = args['housing_type']
        self.os = self.OS.input() or args['os']
        self.ram = self.RAM.input() or args['ram']
