# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import yaml


if __name__ == '__main__':
    print('YAML creator.')
    settings = [
        {
            'name': 'В Салехарде',
            'city': 'г. Салехард',
            'url': 'https://vk.com/inshd'
        },
        {
            'name': 'Подслушано в Салехарде',
            'city': 'г. Салехард',
            'url': 'https://vk.com/hearsalehard'
        },
        {
            'name': 'В Салехарде.ru',
            'city': 'г. Салехард',
            'url': 'https://vk.com/vsaleharderu'
        },
        {
            'name': 'Салехард',
            'city': 'г. Салехард',
            'url': 'https://vk.com/public124643438'
        },
        {
            'name': 'Афиша В Салехарде',
            'city': 'г. Салехард',
            'url': 'https://vk.com/afisha_shd'
        },
    ]
    print('\nTrying to open yaml file')
    f = open('groups.yml', 'w')
    print('Saving data...')
    f.write(yaml.dump(settings))
    f.close()
    print('Setting saved to bots.yaml successfully.')
