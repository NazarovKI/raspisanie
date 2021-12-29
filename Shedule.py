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


# Функция определяет дату следующего дня недели на выбор относительно.
# Заданной даты. Взято https://stackoverflow.com/users/35070/phihag
# Взято без изменений и встроено.
def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

# Определяем русские дни недели и дату следующего воскресения
rus_week = ('Пн.', 'Вт.', 'Ср.', 'Чт.', 'Пт.', 'Сб.', 'Вс.')
next_sunday = next_weekday(date.today(), 6) # 0 = Monday, 1=Tuesday, 2=Wednesday...


print(next_sunday.strftime("%d.%m.%y")+'\n'+rus_week[next_sunday.weekday()])
saint_of_sunday = saint (next_sunday)
print (saint_of_sunday)


# Создаём документ, заголовок, подзаголовок.
document = Document()
document.add_heading('Расписание Богослужений') # Izhitsa 36
heading = saint_of_sunday.replace(' Неделя', 'Седмица').split('.',2)
document.add_heading(heading[1], level=2) # Izhitsa 24 bold


# Создаём таблицу и заголовок таблицы.
table = document.add_table(rows=8, cols=4)
heading_cells = table.rows[0].cells
heading_cells[0].text = 'Дата'
heading_cells[1].text = 'Поминаемые святые'
heading_cells[2].text = 'Время'
heading_cells[3].text = 'Богослужение'


# Получаем данные для таблицы
week = [1,2,3,4,5,6,7]
for day in week:
    day_ = date(2022,1,2)+timedelta(day)
    saint_of_day = saint (day_)
    row = table.rows[day]
    row.cells[0].text = str(day_.strftime("%d.%m.%y")+'\n'+rus_week[day_.weekday()])
    row.cells[1].text = saint (day_)
    row.cells[2].text = '9:00'
    row.cells[3].text = 'Божественная Литургия'


# Помещаем данные в строку 1 по ячейкам
row = table.rows[1]


# Прочитываем последовательно таблицу
for row in table.rows:
    for cell in row.cells:
        print(cell.text)

# Сохраняем документ
filename = heading[1].split(',')
document.save(str(filename[0])+'.docx')
