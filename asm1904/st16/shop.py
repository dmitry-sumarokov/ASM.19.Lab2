# -*- coding: utf-8 -*-

from pickle import load
from pickle import dump
from os import path

from MobilePhone import MobilePhone
from SmartPhone import SmartPhone


class Shop:

    __DATAFILE = 'asm1904/st16/data/mobile_phone_shop.dat'

    def __init__(self):
        self.load_from_file()

    def add_list_entry(self, args):
        if args['type'] == 'smart':
            phone = SmartPhone()
        elif args['type'] == 'mobile':
            phone = MobilePhone()
        phone.set_data(args)
        self.mobile_list.append(phone)
        self.save_to_file()

    def edit_list_entry(self, args):
        self.mobile_list[int(args['id'])].set_data(args)
        self.save_to_file()

    def remove_from_list(self, id):
        del self.mobile_list[id]
        self.save_to_file()

    def load_from_file(self):
        if path.exists(self.__DATAFILE):
            with open(self.__DATAFILE, 'rb') as f:
                self.mobile_list = load(f)
        else:
            self.mobile_list = []

    def save_to_file(self):
        with open(self.__DATAFILE, 'wb') as f:
            dump(self.mobile_list, f)

    def clear_current_list(self):
        self.mobile_list.clear()
        self.save_to_file()


if __name__ == '__main__':
    pass
