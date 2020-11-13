# -*- coding: utf-8 -*-
#####################################################################################################################
#                                                                                                                   #
# Парсер количества подписчиков и среднего количества просмотров за месяц для социальной сети Instagram             #
#                                                                                                                   #
# MIT License                                                                                                       #
# Copyright (c) 2020 Michael Nikitenko                                                                              #
#                                                                                                                   #
#####################################################################################################################

from time import sleep
import threading
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException, \
    ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
import yaml


def get_agents_list():
    """Читает YAML документ со списком агентов и возвращает список словарей с названиями, локациями и их URL"""
    with open('yamls/ig.yml') as f:
        res = yaml.safe_load(f)
    return res


def get_posts_list_and_subs(driver: webdriver, url: str, months: list):
    """Прогружает страницу пользователя и возвращает список из большинства последних постов"""
    driver.get(url)
    sleep(2)
    try:
        subs = int(driver.find_elements_by_class_name('g47SY')[1].get_attribute('title').replace(' ', ''))
        print(f'{subs} подписчиков')
    except IndexError:
        subs = 0
        print(f'У аккаунта {url} не получилось собрать количество подписчиков')
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(2)
    posts = driver.find_elements_by_class_name('v1Nh3')
    posts_links = []
    for post in posts:
        posts_links.append(post.find_element_by_tag_name('a').get_attribute('href'))
    try:
        more_button = driver.find_element_by_class_name('xLCgt')
        more_button.click()
    except NoSuchElementException:
        pass
    except ElementClickInterceptedException:
        print('кнопка не нажимается')
    for _ in range(5):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        sleep(2)
        posts = driver.find_elements_by_class_name('v1Nh3')
        for post in posts:
            posts_links.append(post.find_element_by_tag_name('a').get_attribute('href'))
    posts_links = delete_dublicates_from_list(posts_links)
    res = filter_posts_list(driver=driver, months=months, posts_list=posts_links)
    return res, subs


def delete_dublicates_from_list(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def filter_posts_list(driver: webdriver, months: list, posts_list: list) -> list:
    """Отфильтровывает только нужные для анализа записи"""
    res = []
    for post_url in posts_list:
        driver.get(post_url)
        try:
            sleep(2)
            time = driver.find_element_by_class_name('Nzb55').get_attribute('datetime')
            for month in months:
                if time[0:7] == month:
                    res.append(post_url)
        except NoSuchElementException:
            print(f'ДАТУ НЕ НАХОДИТ!!! ПОСТ {post_url}')
            driver.get(post_url)
            try:
                sleep(2)
                time = driver.find_element_by_class_name('Nzb55').get_attribute('datetime')
                for month in months:
                    if time[0:7] == month:
                        res.append(post_url)
            except NoSuchElementException:
                print(f'ДАТУ НЕ НАХОДИТ ВТОРОЙ РАЗ!!! ПОСТ {post_url}')
                res.append(post_url)
    return res


def parse_post_data(driver: webdriver, url):
    """Собирает данные о лайках и комментах к посту"""
    driver.get(url)
    try:
        likes = int(driver.find_elements_by_class_name('sqdOP')[2].find_element_by_tag_name('span').text.replace(' ', ''))    # sqdOP yWX7d     _8A5w5 vcOH2
        views = 0
    except NoSuchElementException:
        print('это видео')
        try:
            button = driver.find_element_by_class_name('vcOH2')
            views = int(button.find_element_by_tag_name('span').text.replace(' ', ''))
            button.click()
            likes = int(driver.find_element_by_class_name('vJRqr').find_element_by_tag_name('span').text.replace(' ', ''))
            button = driver.find_element_by_class_name('QhbhU')
            button.click()
        except NoSuchElementException:
            views = 0
            try:
                likes = int(driver.find_element_by_class_name('vJRqr').find_element_by_tag_name('span').text.replace(' ', ''))
            except NoSuchElementException:
                likes = 0
                print(f'Нихуя не нашло у поста: {url}')
    comments = get_comments_count(driver=driver)
    return likes, views, comments


def get_comments_count(driver):
    # need_to_reload = True   # Защита от разрывов интернета
    # while need_to_reload == True:
    #     try:  # Доставатель всех трэдов в посте
    #         need_to_reload = True   # Защита от разрывов интернета
    #         thread_click_counter = 0
    #         while need_to_reload == True:   # Защита от разрывов интернета
    #             if thread_click_counter < 200:
    #                 sleep(1.5)
    #                 load_more = driver.find_element_by_class_name('dCJp8')
    #                 load_more.click()
    #                 thread_click_counter += 1
    #             else:
    #                 break
    #     except:
    #         threads = driver.find_elements_by_class_name('Mr508')
    #         need_to_reload = False  # Интернет есть и заново страницу грузить не нужно
    #
    #     if need_to_reload == False:
    #         need_to_reload = True
    #         for thread in threads:
    #             try:  # Доставатель всех сабтредов в тредах
    #                 sleep(1.5)
    #                 look_repls = thread.find_element_by_class_name('EizgU')
    #                 look_repls.click()
    #                 sleep(2)
    #                 look_repls = thread.find_element_by_class_name('EizgU').text
    #                 sleep(1.5)
    #                 subthread_click_counter = 0
    #                 while look_repls[0:17] == 'Посмотреть ответы':  # Раскрываем ответы на комменты до посинения
    #                     if subthread_click_counter < 200:
    #                         look_repls = thread.find_element_by_class_name('EizgU')
    #                         look_repls.click()
    #                         sleep(1)
    #                         look_repls = thread.find_element_by_class_name('EizgU').text
    #                         subthread_click_counter += 1
    #                     else:
    #                         print('SUBTHREADS MORE THAN 200!!! Reload!!!')
    #                         break
    #                 if subthread_click_counter >= 200:
    #                     print('SUBTHREADS MORE THAN 200!!! Reload!!!')
    #                     break
    #             except:
    #                 need_to_reload = False
    #
    # threads = driver.find_elements_by_class_name('Mr508')  # Список всех комментов с ответами
    # comments = count_comments(threads)
    comments = 0
    return comments


def count_comments(threads):
    # replies = []
    # for thread in threads:
    #     try:
    #         answers = thread.find_elements_by_class_name('ZyFrc')
    #         replies.append(len(answers))
    #     except Exception as ex:
    #         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    #         message = template.format(type(ex).__name__, ex.args)
    #         print(message)
    # replies = sum(replies)
    # comments = len(threads)
    # comments = comments + replies
    comments = 0
    return comments


def get_posts_data_lists(driver: webdriver, posts_list: list):
    likes_list, views_list, comments_list = [], [], []
    for post in posts_list:
        likes, views, comments = parse_post_data(driver, post)
        # print(f'У поста {post} {likes} лайков и {views} просмотров {comments} комментариев')
        likes_list.append(likes)
        views_list.append(views)
        comments_list.append(comments)
    return likes_list, views_list, comments_list


def count_medians(likes_list: list, views_list: list, comments_list: list):
    """Считает среднее значение лайков просмотров и комментариев"""
    try:
        median_likes = sum(likes_list) / len(likes_list)
    except ZeroDivisionError:
        median_likes = 0
    videos = 0
    for i in views_list:
        if i != 0:
            videos += 1
    try:
        median_views = sum(views_list) / videos
    except ZeroDivisionError:
        median_views = 0
    try:
        median_comments = sum(comments_list) / len(comments_list)
    except ZeroDivisionError:
        median_comments = 0
    return round(median_likes, 2), round(median_views, 2), round(median_comments, 2)


def parsing_thread(accounts: list, month: str, prev_month: str, prev_prev_month: str, number_of_thread: int):
    """Парсит данные в отдельном потоке и сохраняет их в папку subresults"""
    res = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for account in accounts:
        posts_list, subs = get_posts_list_and_subs(driver, account['link'], [month, prev_month, prev_prev_month])
        likes_list, views_list, comments_list = get_posts_data_lists(driver=driver, posts_list=posts_list)
        median_likes, median_views, median_comments = count_medians(likes_list, views_list, comments_list)
        data = {
            'comments': median_comments,
            'likes': median_likes,
            'link': account['link'],
            'location': account['location'],
            'name': account['name'],
            'sn': 'Инстаграм',
            'subs': subs,
            'views': median_views,
            'theme': account['theme'],
            'posts_freq': len(posts_list)
        }
        print(data)
        res.append(data)
    filename = f'subresults/ig_subres{number_of_thread}.yml'
    with open(filename, mode='w', encoding='utf-8') as yaml_file:
        yaml_file.write(yaml.dump(res))
    driver.quit()


def concatenate_subresults():
    """Объединяет промежуточные результаты потоков в один результат"""
    res = []
    for i in range(12, 13):                                                      # СТАВИМ ОБРАТНО 13 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        with open(f'subresults/ig_subres{i}.yml', encoding='utf-8') as f:
            subres = yaml.safe_load(f)
            for sub in subres:
                res.append(sub)
    return res


def parse_ig(month, p_month, p_p_month):
    accounts = get_agents_list()
    print(f'Количество аккаунтов инстаграм: {len(accounts)}')
    first_thread_accounts_list = accounts[:10]
    second_thread_accounts_list = accounts[10:20]
    third_thread_accounts_list = accounts[20:30]
    fourth_thread_accounts_list = accounts[30:40]
    fifth_thread_accounts_list = accounts[40:50]
    sixth_thread_accounts_list = accounts[50:60]
    seventh_thread_accounts_list = accounts[60:70]
    eighth_thread_accounts_list = accounts[70:80]
    nineth_thread_accounts_list = accounts[80:90]
    tenth_thread_accounts_list = accounts[90:100]
    eleventh_thread_accounts_list = accounts[100:110]
    twelfth_thread_accounts_list = accounts[110:]
    t1 = threading.Thread(target=parsing_thread, args=(first_thread_accounts_list, month, p_month, p_p_month, 1))
    t2 = threading.Thread(target=parsing_thread, args=(second_thread_accounts_list, month, p_month, p_p_month, 2))
    t3 = threading.Thread(target=parsing_thread, args=(third_thread_accounts_list, month, p_month, p_p_month, 3))
    t4 = threading.Thread(target=parsing_thread, args=(fourth_thread_accounts_list, month, p_month, p_p_month, 4))
    t5 = threading.Thread(target=parsing_thread, args=(fifth_thread_accounts_list, month, p_month, p_p_month, 5))
    t6 = threading.Thread(target=parsing_thread, args=(sixth_thread_accounts_list, month, p_month, p_p_month, 6))
    t7 = threading.Thread(target=parsing_thread, args=(seventh_thread_accounts_list, month, p_month, p_p_month, 7))
    t8 = threading.Thread(target=parsing_thread, args=(eighth_thread_accounts_list, month, p_month, p_p_month, 8))
    t9 = threading.Thread(target=parsing_thread, args=(nineth_thread_accounts_list, month, p_month, p_p_month, 9))
    t10 = threading.Thread(target=parsing_thread, args=(tenth_thread_accounts_list, month, p_month, p_p_month, 10))
    t11 = threading.Thread(target=parsing_thread, args=(eleventh_thread_accounts_list, month, p_month, p_p_month, 11))
    t12 = threading.Thread(target=parsing_thread, args=(twelfth_thread_accounts_list, month, p_month, p_p_month, 12))
    # t1.start()
    # sleep(1)
    # t2.start()
    # sleep(1)
    # t3.start()
    # sleep(1)
    # t4.start()
    # sleep(1)
    # t5.start()
    # sleep(1)
    # t6.start()
    # sleep(1)
    # t7.start()
    # sleep(1)
    # t8.start()
    # sleep(1)
    # t9.start()
    # sleep(1)
    # t10.start()
    # sleep(1)
    # t11.start()
    # sleep(1)
    t12.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()
    # t6.join()
    # t7.join()
    # t8.join()
    # t9.join()
    # t10.join()
    # t11.join()
    t12.join()
    res = concatenate_subresults()
    return res

if __name__ == '__main__':
    print('ig_parser')
