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
import copy
import xlwt


HEADER = [
    '№',
    'адрес',
    'Площадь',
    'Год',
    'Количество этажей',
]
COLS_WIDTH = [1455, 12000, 4500, 6500, 9000]


def create_xls(data):
    """Создаём документ"""
    book = xlwt.Workbook('utf8')
    sheet = book.add_sheet('Данные по соцсетям')
    styles = create_styles()
    header_style, data_style, tt_id_style = styles['header_style'], styles['data_style'], styles['tt_id_style']
    sheet, sheet.portrait = render_table(sheet, HEADER, COLS_WIDTH, data, header_style, data_style, tt_id_style), False
    sheet.set_print_scaling(100)
    try:
        book.save('Группы и паблики ВКонтакте.xls')
        print('SUCCESS!\nFile "Группы и паблики ВКонтакте.xls" successfully saved!')
    except PermissionError:
        print('ERROR!\n\tProbably file "Группы и паблики ВКонтакте.xls" is open!\n\tPlease close file and try again.')


def render_table(sheet, header, width, data, header_style, data_style, tt_id_style):
    """Рендерим страницу"""
    # Render table header
    for i in range(len(header)):
        sheet.write(0, i, header[i], header_style)
        sheet.col(i).width = width[i]
    sheet.row(1).height = 2500
    # Render table data
    i = 1
    for d in data:
        sheet.row(i + 1).height = 2500
        cols = [i, 'address', 's', 'year', 'height',]
        for col in range(len(cols)):
            if col == 0:
                sheet.write(i, col, i, tt_id_style)
            elif col == 1:
                sheet.write(i, col, d[cols[col]], tt_id_style)
            else:
                sheet.write(i, col, d[cols[col]], data_style)
        i = i + 1
    return sheet


def create_styles():
    """Создаем стили для документа"""
    # Init all styles
    header_style, data_style, tt_id_style = xlwt.XFStyle(), xlwt.XFStyle(), xlwt.XFStyle()
    # Create fonts
    header_font = xlwt.Font()
    header_font.name, header_font.bold, header_font.colour_index = 'Arial', True, xlwt.Style.colour_map['black']
    header_font.height = 260
    data_font = copy.deepcopy(header_font)
    data_font.bold, data_font.height = False, 240
    # Set fonts to styles
    header_style.font = header_font
    data_style.font = tt_id_style.font = data_font
    # Set borders
    borders = xlwt.Borders()
    borders.left, borders.right, borders.top, borders.bottom = 1, 1, 1, 1
    header_style.borders = data_style.borders = tt_id_style.borders = borders
    # Set alignments
    al = xlwt.Alignment()
    al.horz, al.vert = al.HORZ_CENTER, al.VERT_CENTER
    header_style.alignment = al
    al.horz, al.wrap = al.HORZ_LEFT, True
    data_style.alignment = tt_id_style.alignment = al
    # Set integer cell format to tt_id_style
    tt_id_style.num_format_str = '0'
    return {'header_style': header_style, 'data_style': data_style, 'tt_id_style': tt_id_style}


def get_groups_list():
    """Читает YAML документ со списком групп и возвращает список словарей с названиями групп и их URL"""
    with open('groups.yml') as f:
        groups = yaml.safe_load(f)
    return groups


def get_group_subs_number(driver, url):
    """Получает HTML и находит в нём количество подписчиков"""
    driver.get(url)
    sleep(1)
    try:
        res = int(driver.find_element_by_class_name('group_friends_count').text.strip())
    except NoSuchElementException:
        text = driver.find_element_by_class_name('header_count')
        print(text)
        res = int(driver.find_element_by_class_name('header_count').text.replace(" ", '').strip())
    return res


def prepare_data(driver, groups_list):
    """Получает список групп с ссылками на них и возвращает список словарей {"название" "кол-во подписчиков"}"""
    res = []
    for group in groups_list:
        subs = get_group_subs_number(driver, group['url'])
        res.append({'name': group['name'], 'city': group['city'], 'subs': subs})
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
    # data = get_all_subs_numbers()
    # print(data)
    url = "https://dom.mingkh.ru/yamalo-neneckiy-ao/salehard/"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    sleep(5)
    # subs = get_group_subs_number(driver, url)
    # print(subs)
    res = []
    for _ in range(10):
        table = driver.find_element_by_class_name('table-responsive')
        rows = table.find_elements_by_tag_name('tr')
        for row in rows:
            address = row.find_elements_by_class_name('text-left')[1].text
            s = row.find_elements_by_class_name('text-left')[2].text
            year = row.find_elements_by_class_name('text-left')[3].text
            height = row.find_elements_by_class_name('text-left')[4].text
            if address != 'Адрес':
                res.append({'address': address, 's': s, 'year': year, 'height': height})
        next_button = driver.find_element_by_class_name('next').find_element_by_tag_name('a')
        next_button.click()
        sleep(3)
    create_xls(res)
    driver.quit()