# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Основной скрипт, который запускает парсер и генерирует эксельку                                                   #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from create_yaml import create_yaml
from vk_parser import get_all_subs_numbers
from export_to_xls import create_xls


if __name__ == '__main__':
    print("VK Group list subscribers counter")
    create_yaml()
    print('\nStart parsing data')
    data = get_all_subs_numbers()
    print('Create Excel document')
    create_xls(data)