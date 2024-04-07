import re
import pandas as pd
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("hw\\6_2_regex\\phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

n = 1
for contact in contacts_list[1:]:
  # распределяем фио по столбцам
  contacts_list[n][0:3] = ' '.join(contact[0:3]).split(' ')[0:3]
  
  # распознаем тел номера и группируем по составляющим
  text = contact[5]
  group1_2 = "(\+7|8?)\s?\(?([0-9]{3})\)?[\s|-]?"
  group3_5 = "([0-9]{3})[\s|-]?([0-9]{2})[\s|-]?([0-9]{2})"
  group6_8 = "(\s\(?(доб\.?)\s([0-9]{4})\)?)?"
  pattern = group1_2+group3_5+group6_8
  # распределяем группы тел номера в последовательности(
  # к единому виду) 
  contacts_list[n][5] = re.sub(
    pattern, r'+7(\2)\3-\4-\5 \7\8', text).strip()

#создаем датафрейм из измененного списка   
df = pd.DataFrame(contacts_list[1:], columns=contacts_list[0])
# группируем датафрейм для группироки дублей
df = df.groupby(['lastname', 'firstname']).max().reset_index()
#сохраняем результат в csv
df.to_csv("hw\\6_2_regex\\phonebook.csv", encoding="utf-8")




# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w", encoding="utf-8") as f:
#   datawriter = csv.writer(f, delimiter=',')
#   # Вместо contacts_list подставьте свой список
#   datawriter.writerows(contacts_list)