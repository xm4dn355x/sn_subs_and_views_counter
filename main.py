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
from sn_parsers.fb_parser import parse_fb
from sn_parsers.ig_parser import parse_ig
from sn_parsers.mm_parser import parse_mm
from sn_parsers.ok_parser import parse_ok
from sn_parsers.tg_parser import parse_tg
from sn_parsers.vk_parser import parse_vk
from sn_parsers.yt_parser import parse_yt


# Globals
CSV_PATH = 'data/information_map_20_11_06.csv'
XLSX_PATH = 'data/tg_digest_20_11_03.xlsx'
XLSX_ROWS_COUNT = 81


if __name__ == '__main__':
    print("VK Group list subscribers counter")
    # create_all_yamls(csv_path=CSV_PATH, xlsx_path=XLSX_PATH, xlsx_rows_count=XLSX_ROWS_COUNT)
    # fb_data = parse_fb()
    ig_data = parse_ig('2020-10', '2020-09', '2020-08')
    # for data in ig_data:
    #     print(data)
    # mm_data = parse_mm()
    # ok_data = parse_ok()
    # tg_data = parse_tg()
    # vk_data = parse_vk()
    # yt_data = parse_yt()
    # print(fb_data)
    print(ig_data)
    # print(mm_data)
    # print(ok_data)
    # print(tg_data)
    # print(vk_data)
    # print(yt_data)
