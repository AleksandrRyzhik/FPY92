import requests
import bs4
import fake_headers
import re
import json

'''
company
div class vacancy-serp-item__meta-info-company

name
span class = serp-item__title-link serp-item__title

link
span class = serp-item__title-link-wrapper

    desc
    div class = g-user-content

money
span data-qa= vacancy-serp__vacancy-compensation
class = bloko-header-section-2

city
div data-qa = vacancy-serp__vacancy-address
class = bloko-text

'''

url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"

def gen_headers():
    headers_gen = fake_headers.Headers(
        os='win', browser='firefox')
    return headers_gen.generate() 

response = requests.get(url, headers=gen_headers())
html_data = response.text
soup = bs4.BeautifulSoup(html_data, "lxml")

vacancy_list = soup.find_all(
    'div', class_="vacancy-serp-item-body__main-info")
# print(len(vacancy_list))

vacancy_dict = {}
id = 0

for vacancy in vacancy_list:
    vac_name = vacancy.find('span', class_='serp-item__title-link serp-item__title').text
    tag_info = vacancy.find('span', class_='serp-item__title-link-wrapper')
    a_tag = tag_info.find('a')
    vac_link = a_tag['href']

    vac_resp = requests.get(vac_link, headers=gen_headers())
    desc_data = vac_resp.text
    desc_soup = bs4.BeautifulSoup(desc_data, "lxml")
    
    description = desc_soup.find('div', class_ = 'g-user-content').text
    pattern = "Django|Flask"

    words_list = re.findall(pattern, description, re.IGNORECASE)

    if len(words_list) < 1:
        continue
    else:
        id += 1
        money_tag = vacancy.find(class_='bloko-header-section-2')
        if money_tag == None:
            money = '?'
        else:
            money = money_tag.text
        
        company = vacancy.find('div', class_='vacancy-serp-item__meta-info-company').text
        
        address = vacancy.find('div', attrs={"data-qa": re.compile("address")}).text
        city = address.strip().split(',')[0]

        vacancy_dict[str(id)+' '+vac_name]={
            'link':vac_link, 'salary':money, 'company':company, 'city':city}

with open('hw\\6_3_scrapping\\py_vacancys.json', 'w', encoding='utf-8') as f:   
    json.dump(vacancy_dict, f, ensure_ascii=False)

# print(len(vacancy_dict))
