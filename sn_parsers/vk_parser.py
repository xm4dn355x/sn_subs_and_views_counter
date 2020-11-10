# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Парсер количества подписчиков и среднего количества просмотров, лайков и комментариенв за месяц                   #
# для социальной сети ВКонтакте                                                                                     #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################


import re
import threading
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, \
    ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import yaml


def get_agents_list():
    """Читает YAML документ со списком агентов и возвращает список словарей с названиями, локациями и их URL"""
    with open('../yamls/vk.yml') as f:
        groups = yaml.safe_load(f)
    return groups


def get_group_subs_count_and_views(driver, url):
    """Получает driver и URL группы и возвращает количество подписчиков и среднее число просмотров за месяц"""
    try:
        driver.get(url)
    except InvalidArgumentException:
        print('НЕПРАВИЛЬНЫЙ URL!!!!')
        return 0, 0, 0, 0
    sleep(1)
    try:
        subs = int(driver.find_element_by_class_name('page_counter').find_element_by_class_name('count').text.replace(' ', ''))
        views, likes, comments = get_median_views_count(driver, url)
    except NoSuchElementException:
        try:
            subs = int(driver.find_element_by_class_name('group_friends_count').text.strip())
            views, likes, comments = get_median_views_count(driver, url)
        except NoSuchElementException:
            try:
                subs = int(driver.find_element_by_class_name('header_count').text.replace(" ", '').strip())
                views, likes, comments = get_median_views_count(driver, url)
            except NoSuchElementException:
                print('NoSuchElementException. Видимо страница скрыта!')
                subs = 0
                views = 0
                likes = 0
                comments = 0
    return subs, views, likes, comments


def get_median_views_count(driver, url):
    """Считает среднее количество просмотров, лайков и комментариев"""
    TARGET_MONTH = 'окт'
    CURRENT_MONTH = 'ноя'
    REGEXP_STRING_TARGET = f'\A\d?\d\s{TARGET_MONTH}\sв\s\d?\d:\d\d'
    REGEXP_STRING_CURRENT_MONTH = f'\A\d?\d\s{CURRENT_MONTH}\sв\s\d?\d:\d\d'
    REGEXP_STRING_MINUTES_AGO = f'^\A\d?\d\s(минут)?.?\sназад'
    REGEXP_STRING_HOURS_AGO = f'^\A...?.?.?.?\sчас?.?. назад'
    REGEXP_STRING_TODAY = f'^\Aсегодня в \d?\d:\d\d'
    REGEXP_STRING_YESTERDAY = f'^\Aвчера\sв\s\d?\d:\d\d'
    TARGET_PATTERN = re.compile(REGEXP_STRING_TARGET)
    CURRENT_MONTH_PATTERN = re.compile(REGEXP_STRING_CURRENT_MONTH)
    MINUTES_AGO_PATTERN = re.compile(REGEXP_STRING_MINUTES_AGO)
    HOURS_AGO_PATTERN = re.compile(REGEXP_STRING_HOURS_AGO)
    TODAY_PATTERN = re.compile(REGEXP_STRING_TODAY)
    YESTERDAY_PATTERN = re.compile(REGEXP_STRING_YESTERDAY)
    wall_url = url.replace('club', 'wall-') + '/?own=1'
    driver.get(wall_url)
    try:
        error = driver.find_element_by_class_name('message_page_title').text
    except:
        error = None
    if error == 'Ошибка':
        return 0, 0, 0
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(0.5)
        temp_posts = driver.find_elements_by_class_name('post--with-likes')
        try:
            last_temp_post = temp_posts[-1]
            date = last_temp_post.find_element_by_class_name('rel_date').text
            if not re.match(TARGET_PATTERN, date) and not re.match(CURRENT_MONTH_PATTERN, date) \
                    and not re.match(MINUTES_AGO_PATTERN, date) and not re.match(HOURS_AGO_PATTERN, date) \
                    and not re.match(TODAY_PATTERN, date) and not re.match(YESTERDAY_PATTERN, date):
                break
        except IndexError:
            break
    raw_posts = driver.find_elements_by_class_name('post--with-likes')
    posts = []
    for raw_post in raw_posts:
        date = raw_post.find_element_by_class_name('rel_date').text
        if re.match(TARGET_PATTERN, date):
            posts.append(raw_post)
    views = []
    likes = []
    comments = []
    for post in posts:
        while True:
            try:
                post_replyes = post.find_element_by_class_name('replies_next_main')
                location = post_replyes.location
                location_offset = location['y'] - 100
                print(location_offset)
                driver.execute_script(f'window.scrollTo(0, {location_offset});')
                post_replyes.click()
                location = post_replyes.location
                location_offset = location['y'] + 200
                print(location_offset)
                driver.execute_script(f'window.scrollTo(0, {location_offset});')
                sleep(1)
            except ElementClickInterceptedException:
                sleep(2.5)
            except NoSuchElementException:
                break
            except ElementNotInteractableException:
                break
            except StaleElementReferenceException:
                break
        while True:
            try:
                post_replyes = post.find_element_by_class_name('replies_short_text_deep')
                location = post_replyes.location
                location_offset = location['y'] - 100
                driver.execute_script(f'window.scrollTo(0, {location_offset});')
                post_replyes.click()
                location = post_replyes.location
                location_offset = location['y'] + 200
                driver.execute_script(f'window.scrollTo(0, {location_offset});')
                sleep(0.5)
            except NoSuchElementException:
                break
            except ElementClickInterceptedException:
                sleep(0.5)
            except ElementNotInteractableException:
                break
            except StaleElementReferenceException:
                break
        try:
            post_views = convert_text_count_to_int(post.find_element_by_class_name('_views').text.strip())
        except StaleElementReferenceException:
            print('StaleElementReferenceException: post_views')
            post_views = 0
        try:
            post_likes = convert_text_count_to_int(post.find_element_by_class_name('like_button_count').text.strip())
        except StaleElementReferenceException:
            print('StaleElementReferenceException: post_likes')
            post_likes = 0
        try:
            post_comments = len(post.find_elements_by_class_name('reply'))
        except StaleElementReferenceException:
            print('StaleElementReferenceException: post_comments')
            post_comments = 0
        print(f'post comments = {post_comments}')
        views.append(post_views)
        likes.append(post_likes)
        comments.append(post_comments)
    views_sum = sum(views)
    likes_sum = sum(likes)
    comments_sum = sum(comments)
    try:
        views_median = views_sum / len(views)
    except ZeroDivisionError:
        views_median = 0

    try:
        likes_median = likes_sum / len(likes)
    except ZeroDivisionError:
        likes_median = 0

    try:
        comments_median = comments_sum / len(comments)
    except ZeroDivisionError:
        comments_median = 0

    return round(views_median, 2), round(likes_median, 2), round(comments_median, 2)


def convert_text_count_to_int(text):
    """Конвертирует из текстового формата в число"""
    try:
        if text[-1] == 'K':
            text = float(text.replace('K', '').replace(' ', '')) * 1000
            return int(text)
        return int(text.replace(' ', ''))
    except IndexError:
        return 0


def parsing_thread(data: list, number_of_thread: int):
    """Парсит данные в отдельном потоке и сохраняет их в папку subresults"""
    res = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for agent in data:
        subs, views, likes, comments = get_group_subs_count_and_views(driver=driver, url=agent['link'])
        res.append(
            {
                'name': agent['name'],
                'sn': 'ВКонтакте',
                'link': agent['link'],
                'location': agent['location'],
                'subs': subs,
                'views': views,
                'likes': likes,
                'comments': comments,
            }
        )
    filename = f'../subresults/vk_subres{number_of_thread}.yml'
    with open(filename, mode='w', encoding='utf-8') as yaml_file:
        yaml_file.write(yaml.dump(res))
    driver.quit()




def parse_vk():
    """Выполняет всю грязную работу по парсингу ВКонтакте и возвращает готовые для записи данные"""
    agents_list = get_agents_list()
    first_thread_agents_list = agents_list[:10]
    second_thread_agents_list = agents_list[10:60]
    third_thread_agents_list = agents_list[60:100]
    fourth_thread_agents_list = agents_list[100:140]
    fifth_thread_agents_list = agents_list[140:190]
    sixth_thread_agents_list = agents_list[190:]
    t1 = threading.Thread(target=parsing_thread, args=(first_thread_agents_list, 1))
    t2 = threading.Thread(target=parsing_thread, args=(second_thread_agents_list, 2))
    t3 = threading.Thread(target=parsing_thread, args=(third_thread_agents_list, 3))
    t4 = threading.Thread(target=parsing_thread, args=(fourth_thread_agents_list, 4))
    t5 = threading.Thread(target=parsing_thread, args=(fifth_thread_agents_list, 5))
    t6 = threading.Thread(target=parsing_thread, args=(sixth_thread_agents_list, 6))
    t1.start()
    sleep(1)
    t2.start()
    sleep(1)
    t3.start()
    sleep(1)
    t4.start()
    sleep(1)
    t5.start()
    sleep(1)
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    res = concatenate_subresults()
    return res


def concatenate_subresults():
    """Объединяет промежуточные результаты потоков в один результат"""
    res = []
    for i in range(1, 7):
        with open(f'../subresults/vk_subres{i}.yml', encoding='utf-8') as f:
            subres = yaml.safe_load(f)
            for sub in subres:
                res.append(sub)
    return res


if __name__ == '__main__':
    print('vk_parser')
    # agents_list = get_agents_list()
    res = parse_vk()
    print('ВСЁ СПАРСЕНО!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    for r in res:
        print(r)

    # driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.get('https://vk.com/hearsalehard')
    # driver.get('https://vk.com/hiinshd')
    # while True:
    #     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    #     sleep(0.5)
    #     temp_posts = driver.find_elements_by_class_name('post--with-likes')
    #     last_temp_post = temp_posts[-1]
    #     date = last_temp_post.find_element_by_class_name('rel_date').text
    #     if not re.match(TARGET_PATTERN, date) and not re.match(CURRENT_MONTH_PATTERN, date) \
    #             and not re.match(MINUTES_AGO_PATTERN, date) and not re.match(HOURS_AGO_PATTERN, date) \
    #             and not re.match(TODAY_PATTERN, date) and not re.match(YESTERDAY_PATTERN, date):
    #         break
    # raw_posts = driver.find_elements_by_class_name('post--with-likes')
    # posts = []
    # for raw_post in raw_posts:
    #     date = raw_post.find_element_by_class_name('rel_date').text
    #     if re.match(TARGET_PATTERN, date):
    #         posts.append(raw_post)
    # for post in posts:
    #     print(post)
    # sleep(30)
    # driver.quit()