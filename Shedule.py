# Получает имена святых в честь кого служба по дате
# crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#id18
import docx
import bs4
import requests
import datetime
from docx import Document
from bs4 import BeautifulSoup
from requests import get

document = Document()
document.add_heading('Расписание Богослужений') # Izhitsa 36
document.add_heading('Седмица -я по Пятидесятнице', level=2) # Izhitsa 24 bold
table = document.add_table(rows=30, cols=4)
cell = table.cell(0, 0)
cell.text = 'Дата'
cell = table.cell(0, 1)
cell.text = 'Поминаемые святые'
cell = table.cell(0, 2)
cell.text = 'Время'
cell = table.cell(0, 3)
cell.text = 'Богослужение'

a = [20,21,22,23,24,25,26]
for day in a:
    today = str('2021-12-')+str(day)
    href = get(r'http://www.patriarchia.ru/bu/'+today)
    soup = BeautifulSoup(href.text, 'html.parser')
    p = soup.p.string
    print(p)
    paragraph = document.add_paragraph(p)

# Программа должна исходя из текущей даты - метод
# и выбранных дней богослужений - input + метод date
# определять соответствие выбранных дней недели предстоящей дате
# делать запросы на святых по предстоящим датам (шт.)
# затем сохранять в таблицу

document.save('new-file-name.docx')
#Замена 'Свт. ' 'Мч. ' 'Прп. ' 'Вмч. ' 'Сщмч. ' 'митр. ' пробела на ;&nbsp
# if len(p) < 56 p = p+b
#document.save('test.docx')
