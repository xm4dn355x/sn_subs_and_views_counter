# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Основной скрипт, который запускает парсер и генерирует эксельку                                                   #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


from create_yamls import create_all_yamls


# Globals
CSV_PATH = 'data/information_map_20_11_06.csv'
XLSX_PATH = 'data/tg_digest_20_11_03.xlsx'
XLSX_ROWS_COUNT = 81


if __name__ == '__main__':
    print("VK Group list subscribers counter")
    create_all_yamls(csv_path=CSV_PATH, xlsx_path=XLSX_PATH, xlsx_rows_count=XLSX_ROWS_COUNT)
