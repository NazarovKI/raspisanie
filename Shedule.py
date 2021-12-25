# Получает имена святых в честь кого служба по дате
# crummy.com/software/BeautifulSoup/bs4/doc.ru/bs4ru.html#id18






import docx
import bs4
import requests
import datetime
from docx import Document
from bs4 import BeautifulSoup
from requests import get
from datetime import date
document = Document()
document.add_heading('Расписание Богослужений') # Izhitsa 36
sedmica = 30
document.add_heading('Седмица'+str( sedmica)+ '-я по Пятидесятнице', level=2) # Izhitsa 24 bold
table = document.add_table(rows=10, cols=4)
cell = table.cell(0, 0)
cell.text = 'Дата'
cell = table.cell(0, 1)
cell.text = 'Поминаемые святые'
cell = table.cell(0, 2)
cell.text = 'Время'
cell = table.cell(0, 3)
cell.text = 'Богослужение'

def next_weekday(d, weekday): 
    days_ahead = weekday - d.weekday() 
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7 
    return d + datetime.timedelta(days_ahead) 
d = date.today()
next_monday = next_weekday(d, 0) # 0 = Monday, 1=Tuesday, 2=Wednesday... 
print(next_monday)

c = 0
a = [4,5,6,7,8]
for day in a:
#    today = str('2021-12-')+str(day)
    href = get(r'http://www.patriarchia.ru/bu/'+str(next_monday))
    soup = BeautifulSoup(href.text, 'html.parser')
    p = soup.p.string
    c = c + 1
    r = 1
    cell =  table.cell(c, r)
    cell.text = str(p)
    
    print (p)
#    paragraph = document.add_paragraph(p)

# Программа должна исходя из текущей даты - метод
# и выбранных дней богослужений - input + метод date
# определять соответствие выбранных дней недели предстоящей дате
# делать запросы на святых по предстоящим датам (шт.)
# затем сохранять в таблицу

document.save('Седмица'+str(sedmica)+'по Пятидесятнице.docx')
#Замена 'Свт. ' 'Мч. ' 'Прп. ' 'Вмч. ' 'Сщмч. ' 'митр. ' пробела на ;&nbsp
# if len(p) < 56 p = p+b
#document.save('test.docx')
