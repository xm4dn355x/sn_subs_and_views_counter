# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Экспорт данных в документ Microsoft Excel                                                                         #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import copy
import xlwt


# CONSTS
HEADER = [
    '№',
    'Наименование группы',
    'Территория',
    'Количество подписчиков',
]
COLS_WIDTH = [1455, 10186, 5093, 5093]


def create_xls(data):
    """Создаём документ"""
    book = xlwt.Workbook('utf8')
    sheet = book.add_sheet('Группы Вконтакте')
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
        cols = [i, 'name', 'city', 'subs']
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


if __name__ == '__main__':
    print("Создаём документ Excel со списком групп и количеством подписчиков")
    from vk_parser import get_all_subs_numbers
    create_xls(get_all_subs_numbers())
