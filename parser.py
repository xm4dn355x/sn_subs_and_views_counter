# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Парсер для ВКонтакте                                                                                              #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from bs4 import BeautifulSoup
from requests import get
import yaml


def get_html(url):
    """Создает GET-запрос и возвращает HTML"""
    try:
        r = get(url, headers={'User-Agent': 'Custom'})  # Создаем объект web-страницы по полученному url
        print(r, end=" ")  # Ответ от сервера <Response [200]>
        return r.text
    except :
        print('Ошибка подключения')
        return ''   # Возвращаем пустую строку вместо HTML


def get_groups_list():
    """Читает YAML документ со списком групп и возвращает список словарей с названиями групп и их URL"""
    with open('groups.yml') as f:
        groups = yaml.safe_load(f)
    return groups


if __name__ == '__main__':
    pass
