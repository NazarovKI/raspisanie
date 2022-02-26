# Программа получает имена святых в честь кого служба исходя из даты
# Ближайшего Воскресения (с воскресения в церкви начинается неделя, оно так
# и называется - неделя. И ложится в основу имени и номера последующей седмицы
# crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#id18
# - документация по BeautifulSoup - ядро программы, модуль который загружает
# с сайта только нужную нам информацию

import docx
import bs4
import requests
import datetime
from docx import Document
from bs4 import BeautifulSoup
from requests import get
from datetime import date
from datetime import timedelta


# Функция возвращает поминаемых в этот день святых
def saint(date):
    href = get(r'http://www.patriarchia.ru/bu/'+str(date))
    soup = BeautifulSoup(href.text,'html.parser')
    return soup.p.string



# была одна мысль -- сделать функцию определяющую след. воскресение
def next_sunday():
    days_ahead = 6 - date.today().weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return date.today() + datetime.timedelta(days_ahead)


# была вторая мысль, которая привела к открытию:
# str(date.today()) -- годится для постановки в функцию saint
# str(date.today()+timedelta(5)) -- годится для постановки в цикл


# Определяем русские дни
rus_week = ('Пн.', 'Вт.', 'Ср.', 'Чт.', 'Пт.', 'Сб.', 'Вс.')
print(next_sunday().strftime("%d.%m.%y")+'\n'+rus_week[next_sunday().weekday()])

week = [0,1,2,3,4,5,6,7,8]
for day in week:
    saint_of_day = saint (next_sunday()+timedelta(day))
    print (saint_of_day)

