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


def read_csv(filename):
    """Читает CSV файл и записывает данные в глобальные переменные имена/названия локации и ссылки"""
    vk = []
    ok = []
    fb = []
    ig = []
    yt = []
    mass_media = []
    misc = []
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        csvdata = csv.DictReader(csvfile, delimiter=',')
        for row in csvdata:
            if row['Соцсеть'] == 'ВКонтакте':
                vk.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка'], 'theme': row['Тематика']})
            elif row['Соцсеть'] == 'Инстаграм':
                ig.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка'], 'theme': row['Тематика']})
            elif row['Соцсеть'] == 'ОК':
                ok.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка'], 'theme': row['Тематика']})
            elif row['Соцсеть'] == 'Фейсбук':
                fb.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка'], 'theme': row['Тематика']})
            elif row['Соцсеть'] == 'Ютуб':
                yt.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка'], 'theme': row['Тематика']})
            elif row['Соцсеть'] == 'Интернет':
                mass_media.append({'name': row['\ufeffName'], 'location': row['Локация'], 'link': row['Ссылка'], 'theme': row['Тематика']})
            else:
                misc.append(row)
    return vk, ok, fb, ig, yt, mass_media, misc


def read_xlsx(filename: str, rows_count: int):
    """Читает документ xlsx и записывает данные в глобальную переменную названия телеграм каналов, локации и ссылки"""
    tg = []
    worksheet = xlrd.open_workbook(filename, on_demand=True).sheet_by_index(0)
    for i in range(rows_count):
        tg.append({'name': worksheet.cell(i, 0).value, 'location': '', 'link': worksheet.cell(i, 1).value})
    return tg


def create_yaml(dataset: list, filename: str):
    """Получает список словарей с данными и желаемое имя файла и создает yaml-файл с данными"""
    with open(filename, mode='w', encoding='utf-8') as yaml_file:
        yaml_file.write(yaml.dump(dataset))


def create_all_yamls(csv_path: str, xlsx_path: str, xlsx_rows_count: int):
    """Создает все необходимые yaml файлы"""
    vk, ok, fb, ig, yt, mass_media, misc = read_csv(filename=csv_path)  # Читает данные из CSV-файла
    tg = read_xlsx(filename=xlsx_path, rows_count=xlsx_rows_count)      # Читает данные из xlsx-файла
    create_yaml(vk, 'yamls/vk.yml')
    create_yaml(ok, 'yamls/ok.yml')
    create_yaml(tg, 'yamls/tg.yml')
    create_yaml(fb, 'yamls/fb.yml')
    create_yaml(ig, 'yamls/ig.yml')
    create_yaml(yt, 'yamls/yt.yml')
    create_yaml(mass_media, 'yamls/mm.yml')
    create_yaml(misc, 'yamls/misc.yml')
    print('all yaml files created succesfully')


if __name__ == '__main__':
    print('create_vk_list_yaml')
    create_all_yamls(csv_path=CSV_PATH, xlsx_path=XLSX_PATH, xlsx_rows_count=XLSX_ROWS_COUNT)
