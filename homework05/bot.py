import requests
import telebot
from datetime import datetime
from bs4 import BeautifulSoup
from typing import List, Tuple

access_token = '811668477:AAGXDa7U_jS2Oln0ei8cKHRkQf-4WOcxrq0'
bot = telebot.TeleBot(access_token)

day_b = {'/monday': 0,
         '/tuesday': 1,
         '/wednesday': 2,
         '/thursday': 3,
         '/friday': 4,
         '/saturday': 5,
         '/sunday': 6}

day_rus = {0: 'Понедельник',
           1: 'Вторник',
           2: 'Среда',
           3: 'Четверг',
           4: 'Пятница',
           5: 'Суббота',
           6: 'Воскресенье'}

day_c = {0: '1day',
         1: '2day',
         2: '3day',
         3: '4day',
         4: '5day',
         5: '6day',
         6: '7day'}


def get_page(group: str) -> str:
    now = datetime.now()
    week = datetime.date(now).isocalendar()[1]
    if week % 2 == 0:
        week = '2'
    else:
        week = '1'
    url = '{domain}/{group}/{week}/raspisanie_zanyatiy_{group}.htm'.format(
        domain='http://www.ifmo.ru/ru/schedule/0',
        week=week,
        group=group
    )
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_a_day(web_page, day_p):
    soup = BeautifulSoup(web_page, "html5lib")

    # Получаем таблицу с расписанием на конкретный день
    schedule_table = soup.find("table", attrs={"id": day_p})

    # Исключение, если в этот день нет пар
    if not schedule_table:
        return

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Номер аудитории
    aud_list = schedule_table.find_all("td", attrs={"class": "room"})
    aud_list = [aud.dd.text for aud in aud_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]

    return times_list, locations_list, lessons_list, aud_list


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message):
    """ Получить расписание на указанный день """
    try:
        day, group = message.text.split()
    except:
        bot.send_message(message.chat.id, 'Будь внимательнее при вводе данных 🌚')
        return None
    day_print = day_b.get(day)
    day_p = day_c.get(day_print)
    web_page = get_page(group)
    schedule_for_day = parse_schedule_for_a_day(web_page, day_p)
    if not schedule_for_day:
        bot.send_message(message.chat.id, 'В этот день нет пар 😉 \n'
                                          'Либо такой группы не существует 🙅')
        return None
    times_lst, locations_lst, lessons_lst, aud_lst = schedule_for_day
    resp = ''
    day_rus_print = day_rus.get(day_print)
    resp += '📅 <b>{}</b> \n'.format(day_rus_print)
    for time, location, lesson, aud in zip(times_lst, locations_lst, lessons_lst, aud_lst):
        resp += '\n\n <b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lesson, aud)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message):
    """ Получить ближайшее занятие """
    try:
        _, group = message.text.split()
    except:
        bot.send_message(message.chat.id, 'Будь внимательнее при вводе данных 🌚')
        return None
    now = datetime.now()
    day = datetime.weekday(now)
    day_p = day_c.get(day)
    time_p = tuple([now.hour, now.minute])
    count_minute_p = (time_p[0] * 60) + time_p[1]
    web_page = get_page(group)
    schedule_for_day = parse_schedule_for_a_day(web_page, day_p)
    if not schedule_for_day:
        bot.send_message(message.chat.id, 'У вас сегодня нет пар 😉 \n'
                                          'Либо такой группы не существует 🙅')
        return
    times_lst, locations_lst, lessons_lst, aud_lst = schedule_for_day
    for time_s in times_lst:
        time_s = time_s.split('-')
        time_s = datetime.strptime(time_s[0], '%H:%M')
        time_s = tuple([time_s.hour, time_s.minute])
        count_minute_s = (time_s[0] * 60) + time_s[1]
        if count_minute_p < count_minute_s:
            resp = ''
            for time, location, lesson, aud in zip(times_lst, locations_lst, lessons_lst, aud_lst):
                resp = '⏰ Следущая пара:\n \n\n <b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lesson, aud)
            return bot.send_message(message.chat.id, resp, parse_mode='HTML')
        else:
            pass
    bot.send_message(message.chat.id, 'Че смотришь? \n'
                                      'Домой иди \n'
                                      'Пары закончились 😜')


@bot.message_handler(commands=['tomorrow'])
def get_tomorrow(message):
    """ Получить расписание на следующий день """
    try:
        _, group = message.text.split()
    except:
        bot.send_message(message.chat.id, 'Будь внимательнее при вводе данных 🌚')
        return None
    now = datetime.now()
    day = datetime.weekday(now)
    if day <= 5:
        day += 1
    else:
        day = 0
    day_p = day_c.get(day)
    web_page = get_page(group)
    schedule_for_day = parse_schedule_for_a_day(web_page, day_p)
    if not schedule_for_day:
        bot.send_message(message.chat.id, 'У вас завтра нет пар 😉 \n'
                                          'Либо такой группы не существует 🙅')
        return None
    times_lst, locations_lst, lessons_lst, aud_lst = schedule_for_day
    resp = ''
    day_rus_print = day_rus.get(day)
    resp += '📅 <b>{}</b> \n'.format(day_rus_print)
    for time, location, lesson, aud in zip(times_lst, locations_lst, lessons_lst, aud_lst):
        resp += '\n\n <b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lesson, aud)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message):
    """ Получить расписание на всю неделю для указанной группы """
    try:
        _, group = message.text.split()
    except:
        bot.send_message(message.chat.id, 'Будь внимательнее при вводе данных 🌚')
        return None
    web_page = get_page(group)
    resp = ''
    counter = 0
    for day in range(0, 7):
        day_p = day_c.get(day)
        day_rus_print = day_rus.get(day)
        schedule_for_day = parse_schedule_for_a_day(web_page, day_p)
        if not schedule_for_day:
            counter += 1
            continue
        times_lst, locations_lst, lessons_lst, aud_lst = schedule_for_day
        resp += '📅 <b>{}</b> \n'.format(day_rus_print)
        for time, location, lesson, aud in zip(times_lst, locations_lst, lessons_lst, aud_lst):
            resp += '\n\n <b>{}</b>, {} <i>{}</i> {} \n\n'.format(time, location, lesson, aud)
        resp += '------------------------ \n\n'.format(resp)
    if counter == 7:
        bot.send_message(message.chat.id, 'Такой группы не существует 🙅')
    else:
        bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)
    
