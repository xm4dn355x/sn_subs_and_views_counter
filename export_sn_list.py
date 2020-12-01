# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
#                                                                                                                   #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import copy
import xlwt
import yaml


# CONSTS
HEADER = [
    '№',
    'Имя/название',
    'Соцсеть',
    'Территория',
    'Ссылка',
    'Тема'
]
COLS_WIDTH = [1455, 12000, 4500, 6500, 9000, 4700]


def get_agents_list(name: str):
    """Читает YAML документ со списком агентов и возвращает список словарей с названиями, локациями и их URL"""
    with open(f'yamls/{name}.yml') as f:
        res = yaml.safe_load(f)
    return res


def create_xls(sn_list: list):
    """Создаём документ"""
    book = xlwt.Workbook('utf8')
    for data in sn_list:
        sheet = book.add_sheet(f"Список {data[0]['link'].split('/')[2]}")
        styles = create_styles()
        header_style, data_style, tt_id_style = styles['header_style'], styles['data_style'], styles['tt_id_style']
        sheet, sheet.portrait = render_table(sheet, HEADER, COLS_WIDTH, data, header_style, data_style, tt_id_style), False
        sheet.set_print_scaling(100)
    filename = 'Аккаунты соцсети'
    try:
        book.save(f'{filename}.xls')
        print(f'SUCCESS!\nFile "{filename}.xls" successfully saved!')
    except PermissionError:
        print(f'ERROR!\n\tProbably file "{filename}.xls" is open!\n\tPlease close file and try again.')


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
        cols = [i, 'name', 'sn', 'location', 'link', 'theme']
        for col in range(len(cols)):
            if col == 0:
                sheet.write(i, col, i, tt_id_style)
            elif col == 1:
                sheet.write(i, col, d[cols[col]], tt_id_style)
            else:
                try:
                    if col == 9:
                        sheet.write(i, col, (round((d[cols[col]] / 30), 2)), data_style)
                    else:
                        sheet.write(i, col, d[cols[col]], data_style)
                except KeyError:
                    sheet.write(i, col, 0, data_style)
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


if __name__ == '__main__':
    sn_list = []
    print('FaceBook')
    fb = get_agents_list('fb')
    for agent in fb:
        print(agent)
    sn_list.append(fb)

    print('Instagram')
    ig = get_agents_list('ig')
    for agent in ig:
        print(agent)
    sn_list.append(ig)

    print('OK')
    ok = get_agents_list('ok')
    for agent in ok:
        print(agent)
    sn_list.append(ok)

    print('Telegram')
    tg = get_agents_list('tg')
    for agent in tg:
        print(agent)
    sn_list.append(tg)

    print('vk.com')
    vk = get_agents_list('vk')
    for agent in vk:
        print(agent)
    sn_list.append(vk)

    print('YouTube')
    yt = get_agents_list('yt')
    for agent in yt:
        print(agent)
    sn_list.append(yt)

    create_xls(sn_list)
