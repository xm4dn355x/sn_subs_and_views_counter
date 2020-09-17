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

GROUPS = [
    {
        'name': 'Подслушано в Салехарде',
        'city': 'г. Салехард',
        'url': 'https://vk.com/hearsalehard'
    },
    {
        'name': 'Мы ♥ САЛЕХАРД',
        'city': 'г. Салехард',
        'url': 'https://vk.com/salekhard89'
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
    {
        'name': 'Черная метка В Салехарде',
        'city': 'г. Салехард',
        'url': 'https://vk.com/bpinshd'
    },
    {
        'name': 'Инцидент Салехард',
        'city': 'г. Салехард',
        'url': 'https://vk.com/inc_salekhard'
    },
    {
        'name': 'Cвобода Zлова',
        'city': 'г. Салехард',
        'url': 'https://vk.com/svobodazlova'
    },
    {
        'name': 'Ветхое и аварийное жильё Ямала',
        'city': 'г. Салехард',
        'url': 'https://vk.com/yamalnash'
    },
    {
        'name': 'Подслушано «ЯМК» | Салехард',
        'city': 'г. Салехард',
        'url': 'https://vk.com/podslushanoyamk'
    },
    {
        'name': 'Коммунальщик Салехарда',
        'city': 'г. Салехард',
        'url': 'https://vk.com/gkhshd'
    },
    {
        'name': 'Салехард 89',
        'city': 'г. Салехард',
        'url': 'https://vk.com/shd__news'
    },
    {
        'name': 'Лабытнанги Info',
        'city': 'г. Лабытнанги',
        'url': 'https://vk.com/lbtinfo'
    },
    {
        'name': 'Подслушано №1 | Лабытнанги',
        'city': 'г. Лабытнанги',
        'url': 'https://vk.com/labti'
    },
    {
        'name': 'Лабытнанги сегодня',
        'city': 'г. Лабытнанги',
        'url': 'https://vk.com/lbt_today'
    },
    {
        'name': 'Лабытнанги NEWS',
        'city': 'г. Лабытнанги',
        'url': 'https://vk.com/club40068'
    },
    {
        'name': 'ГУБКИНСКИЙ - ГОРОД МЕЧТЫ',
        'city': 'г. Губкинский',
        'url': 'https://vk.com/gubkinskiy'
    },
    {
        'name': 'Губкинский',
        'city': 'г. Губкинский',
        'url': 'https://vk.com/gubkinskyi'
    },
    {
        'name': 'Губкинский 24',
        'city': 'г. Губкинский',
        'url': 'https://vk.com/gbk24'
    },
    {
        'name': '[ТГ] ТИПИЧНЫЙ ГУБКИНСКИЙ',
        'city': 'г. Губкинский',
        'url': 'https://vk.com/gubkinskiy_ru'
    },
    {
        'name': 'Подслушано Губкинский',
        'city': 'г. Губкинский',
        'url': 'https://vk.com/gubkinski'
    },
    {
        'name': 'ГУБКИНСКИЙ - ТВОЙ ГОРОД ЯНАО',
        'city': 'г. Губкинский',
        'url': 'https://vk.com/gubkinskiyyanao'
    },
    {
        'name': '[ТН] ТИПИЧНЫЙ НОЯБРЬСК',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/noyabrsk_89_region'
    },
    {
        'name': 'Происшествия Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/nojabrsk112'
    },
    {
        'name': 'Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/tvoynbrsk'
    },
    {
        'name': '|НТН| НЕтипичный Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/nsk_89rus'
    },
    {
        'name': 'Реальный Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/real_noyabrsk'
    },
    {
        'name': 'Ноябрьск Неспокойный',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/nospok_noyabrsk'
    },
    {
        'name': 'Злой Ноябрянин',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/blacklistnotabrsk89'
    },
    {
        'name': 'Ноябрьск - ЯМАЛ -',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/my_noyabrsk'
    },
    {
        'name': 'Пульс Севера | жизнь ЯНАО | Новости | Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/vse_novosti_nsk'
    },
    {
        'name': '[LIFE] Независимый Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/life.noyabrsk'
    },
    {
        'name': 'Живи Как Хочешь. Ноябрьск ',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/zkh_noyabrsk'
    },
    {
        'name': '|НТР| НЕтипичные родители Ноябрьска',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/parents_nsk'
    },
    {
        'name': 'Н.Н | Наш_Ноябрьск | ваши Новости',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/nash_noyabrsk'
    },
    {
        'name': 'Ноябрьск',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/tvoynbrsk'
    },
    {
        'name': 'Подслушано в Ноябрьске',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/nsk_overheard'
    },
    {
        'name': 'Ноябряне (Подслушано Ноябрьск)',
        'city': 'г. Ноябрьск',
        'url': 'https://vk.com/nospok_noyabrsk'
    },
    {
        'name': 'Муравленко',
        'city': 'г. Муравленко',
        'url': 'https://vk.com/muravlen'
    },
    {
        'name': 'Подслушано Муравленко',
        'city': 'г. Муравленко',
        'url': 'https://vk.com/muravlenka'
    },
    {
        'name': 'Муравленковский день',
        'city': 'г. Муравленко',
        'url': 'https://vk.com/muravlenko_day'
    },
    {
        'name': 'Типичный Муравленко',
        'city': 'г. Муравленко',
        'url': 'https://vk.com/tippermol'
    },
    {
        'name': 'ГОРОРО | Новый Уренгой',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/nurengoy'
    },
    {
        'name': 'Подслушано Новый Уренгой',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/public_urengoy'
    },
    {
        'name': 'N24.RU | Новостное агентство Ямала',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/n24_yanao'
    },
    {
        'name': 'ЧП | ДТП | Новый Уренгой',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/regik89'
    },
    {
        'name': 'Аварийный Новый Уренгой',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/avariyniynur_89'
    },
    {
        'name': 'Новый Уренгой | Официальная группа города',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/newurengoyru'
    },
    {
        'name': 'ЗЛОЙ УРЕНГОЕЦ 18+',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/zloy089'
    },
    {
        'name': 'Новый Уренгой',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/newurengoy_89'
    },
    {
        'name': 'ГОРОРО | Новый Уренгой 2.0',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/novurengoi'
    },
    {
        'name': 'НОВЫЙ УРЕНГОЙ 89 REGION',
        'city': 'г. Новый Уренгой',
        'url': 'https://vk.com/nur89region'
    },
    {
        'name': 'ЗЛОЙ И ДОБРЫЙ НАДЫМЧАНИН',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/zloynadym'
    },
    {
        'name': 'Типичный Надым',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/nadymcity'
    },
    {
        'name': 'Надым и Надымский район',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/nadymregion'
    },
    {
        'name': 'Надым',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/nnadym'
    },
    {
        'name': 'Это Пангоды, детка! [Типичные Пангоды]',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/pangodydetka'
    },
    {
        'name': 'п. Пангоды',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/pangody'
    },
    {
        'name': 'НАДЫМ online',
        'city': 'Надымский р-н',
        'url': 'https://vk.com/nadym_online'
    },
    {
        'name': 'ПЕРВЫЙ ЯМАЛЬСКИЙ (Яр-Сале ЯНАО)',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/yamal_news'
    },
    {
        'name': 'ЯМАЛ СПГ (САБЕТТА)',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/yamallng'
    },
    {
        'name': 'Панаевск LIVE',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/panaevsklive'
    },
    {
        'name': 'Подслушано в Сабетте',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/sabetta2'
    },
    {
        'name': 'Сеяха',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/seyakha'
    },
    {
        'name': 'МОЙ ЯМАЛЬСКИЙ РАЙОН',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/moi_yamalskiy_raion'
    },
    {
        'name': 'Новый Порт',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/new_port'
    },
    {
        'name': 'Подслушано в Сеяхе',
        'city': 'Ямальский р-н',
        'url': 'https://vk.com/public154237522'
    },
    {
        'name': 'Тазовский раЁн',
        'city': 'Тазовский р-н',
        'url': 'https://vk.com/tazraion'
    },
    {
        'name': 'ГАЗ & ТАЗ - Газ-Сале Тазовский',
        'city': 'Тазовский р-н',
        'url': 'https://vk.com/gaztaz'
    },
    {
        'name': 'ЧС Тазовский',
        'city': 'Тазовский р-н',
        'url': 'https://vk.com/cstazovsky'
    },
    {
        'name': 'SelkupLiveNews',
        'city': 'Красноселькупский р-н',
        'url': 'https://vk.com/selkuplivenews'
    },
    {
        'name': 'Красноселькуп',
        'city': 'Красноселькупский р-н',
        'url': 'https://vk.com/krasnoselkup'
    },
    {
        'name': 'Самый лучший посёлок -КРАСНОСЕЛЬКУП!!!ЗДЕСЬ ЖИЛИ, ЖИВУТ И БУДУТ ЖИТЬ САМЫЕ ЛУЧШИЕ ЛЮДИ!!!',
        'city': 'Красноселькупский р-н',
        'url': 'https://vk.com/club2777620'
    },
    {
        'name': 'Тарко-Сале',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/tarkosale'
    },
    {
        'name': 'Уренгой FOREVER',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/urengoy_forever'
    },
    {
        'name': 'Мой город | Тарко-Сале',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/my_tarkosale'
    },
    {
        'name': 'Сплетни | Тарко-Сале',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/spletni_ts'
    },
    {
        'name': 'Типичный Уренгой',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/new_urengoy89'
    },
    {
        'name': 'ВЕСТИГОРОДА|Тарко-Сале|Пуровск|Уренгой|Пурпе|',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/vestigoroda'
    },
    {
        'name': 'Злой Ямал',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/zloy_yamal'
    },
    {
        'name': 'Жизнь в пгт Уренгой :)',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/starurengoi'
    },
    {
        'name': 'Чёрный список пгт Уренгой',
        'city': 'Пуровский р-н',
        'url': 'https://vk.com/chsurengoy'
    },
    {
        'name': 'Подслушано Харп | ЯНАО',
        'city': 'Приуральский р-н',
        'url': 'https://vk.com/public81904511'
    },
    {
        'name': 'Подслушано в Аксарке',
        'city': 'Приуральский р-н',
        'url': 'https://vk.com/public152678658'
    },
    {
        'name': 'Аксарка',
        'city': 'Приуральский р-н',
        'url': 'https://vk.com/club53119538'
    },
    {
        'name': 'Аксарка-City - Рулит!!',
        'city': 'Приуральский р-н',
        'url': 'https://vk.com/aksarka'
    },
    {
        'name': 'Подслушано Шурышкaрский район. Мужи',
        'city': 'Шурышкарский р-н',
        'url': 'https://vk.com/clubmuji'
    },
    {
        'name': 'Подслушано в Мужах',
        'city': 'Шурышкарский р-н',
        'url': 'https://vk.com/public146004564'
    },
    {
        'name': 'ЧП Ямал',
        'city': 'ЯНАО',
        'url': 'https://vk.com/incident_yamal'
    },
    {
        'name': 'Ямал наш',
        'city': 'ЯНАО',
        'url': 'https://vk.com/yamalas'
    },
    {
        'name': '👑 Говорящий ЯМАЛ 👑',
        'city': 'ЯНАО',
        'url': 'https://vk.com/shdonline'
    },
    {
        'name': 'Не гони Пургу | Чисто ямальский подкаст',
        'city': 'ЯНАО',
        'url': 'https://vk.com/negonipurgu'
    },
    {
        'name': 'СТОП СВИН ЯНАО',
        'city': 'ЯНАО',
        'url': 'https://vk.com/stopthepiggi'
    },
    {
        'name': 'МОЙ ЯМАЛ',
        'city': 'ЯНАО',
        'url': 'https://vk.com/afisha89ru'
    },
    {
        'name': 'Ямал LIFE',
        'city': 'ЯНАО',
        'url': 'https://vk.com/yamallife'
    },
    {
        'name': 'Сплетни | ЯНАО',
        'city': 'ЯНАО',
        'url': 'https://vk.com/vtarkosale'
    },
    {
        'name': 'Бесит в Салехарде I ЯНАО',
        'city': 'Салехард',
        'url': 'https://vk.com/public186055277'
    },
]


def create_yaml():
    print('\nTrying to open yaml file')
    f = open('groups.yml', 'w')
    print('Saving data...')
    f.write(yaml.dump(GROUPS))
    f.close()
    print('Data saved to groups.yml successfully.')


if __name__ == '__main__':
    print('YAML creator.')
    create_yaml()
