# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Читает CSV документ экспортированный из airtable и xls документ экспортированный из google docs, создаёт          #
# yaml файлы со списками необходимых для парсинга агентов.                                                          #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import csv

import xlrd
import yaml


# GLOBALS
CSV_PATH = 'data/information_map_20_11_06.csv'
XLSX_PATH = 'data/tg_digest_20_11_03.xlsx'
XLSX_ROWS_COUNT = 81

VK = []
OK = []
TG = []
FB = []
IG = []
YT = []
MASS_MEDIA = []
MISC = []


def read_csv(filename):
    """Читает CSV файл и записывает данные в глобальные переменные имена/названия локации и ссылки"""
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        csvdata = csv.DictReader(csvfile, delimiter=',')
        for row in csvdata:
            if row['Соцсеть'] == 'ВКонтакте':
                VK.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка']})
            elif row['Соцсеть'] == 'Инстаграм':
                IG.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка']})
            elif row['Соцсеть'] == 'ОК':
                OK.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка']})
            elif row['Соцсеть'] == 'Фейсбук':
                FB.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка']})
            elif row['Соцсеть'] == 'Ютуб':
                YT.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка']})
            elif row['Соцсеть'] == 'Интернет':
                MASS_MEDIA.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка']})
            else:
                MISC.append(row)


def read_xlsx(filename: str, rows_count: int):
    """Читает документ xlsx и записывает данные в глобальную переменную названия телеграм каналов, локации и ссылки"""
    worksheet = xlrd.open_workbook(filename, on_demand=True).sheet_by_index(0)
    for i in range(rows_count):
        TG.append({'name': worksheet.cell(i, 0).value, 'location': '', 'link': worksheet.cell(i, 1).value})


def create_yaml(dataset: list, filename: str):
    """Получает список словарей с данными и желаемое имя файла и создает yaml-файл с данными"""
    with open(filename, mode='w', encoding='utf-8') as yaml_file:
        yaml_file.write(yaml.dump(dataset))


def create_all_yamls():
    """Создает все необходимые yaml файлы"""
    create_yaml(VK, 'yamls/vk.yml')
    create_yaml(OK, 'yamls/ok.yml')
    create_yaml(TG, 'yamls/tg.yml')
    create_yaml(FB, 'yamls/fb.yml')
    create_yaml(IG, 'yamls/ig.yml')
    create_yaml(YT, 'yamls/yt.yml')
    create_yaml(MASS_MEDIA, 'yamls/mm.yml')
    create_yaml(MISC, 'yamls/misc.yml')
    print('all files created succesfully')


if __name__ == '__main__':
    print('create_vk_list_yaml')
    read_csv(CSV_PATH)
    read_xlsx(XLSX_PATH, XLSX_ROWS_COUNT)
    create_all_yamls()
