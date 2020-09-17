# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Парсер для ВКонтакте                                                                                              #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import yaml


def get_groups_list():
    """Читает YAML документ со списком групп и возвращает список словарей с названиями групп и их URL"""
    with open('groups.yml') as f:
        groups = yaml.safe_load(f)
    return groups


def get_group_subs_number(driver, url):
    """Получает HTML и находит в нём количество подписчиков"""
    driver.get(url)
    try:
        res = int(driver.find_element_by_class_name('group_friends_count').text.strip())
    except NoSuchElementException:
        res = int(driver.find_element_by_class_name('header_count').text.replace(" ", '').strip())
    return res


def prepare_data(driver, groups_list):
    """Получает список групп с ссылками на них и возвращает список словарей {"название" "кол-во подписчиков"}"""
    res = []
    for group in groups_list:
        subs = get_group_subs_number(driver, group['url'])
        res.append({'name': group['name'], 'subs': subs})
    return res


def get_all_subs_numbers():
    """Основная функция возвращающая список групп с их количеством подписчиков"""
    groups_list = get_groups_list()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://vk.com/hearsalehard")
    sleep(5)
    return prepare_data(driver, groups_list)


if __name__ == '__main__':
    print("Парсер групп вконтакте с целью поиска количества подписчиков")
    data = get_all_subs_numbers()
    print(data)

