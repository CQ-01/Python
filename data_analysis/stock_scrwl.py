# -*- coding: utf-8 -*-
"""Colab_1주차.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Uf1vIXwggcvVoO6sHMfXVXMXPnFJHlpO
"""

a = 2
b = 3

a + b

a_list = ['사과', '배', '감', '수박']
a_list[0]

a_list.append('딸기')
a_list

a_list = [{'name' : '철수', 'age':15}, {'name':'영희', 'age':25}]
print(a_list)
print(a_list[0]['age'])

def sum(a, b):
  print('결과는?: ')
  return a + b

result = sum(2, 3)
result

def is_adult(age):
  if age > 20:
    print('성인')
  else:
    print('청소년')

is_adult(20)
is_adult(50)

ages = [15, 25, 30, 8, 13]

for age in ages:
  is_adult(age)

!pip install bs4 requests

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime


def get_news(keyword):
  wb = Workbook()
  sheet = wb.active

  headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
  data = requests.get(f'https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}',headers=headers)

  soup = BeautifulSoup(data.text, 'html.parser')

  lis = soup.select('#main_pack > section > div > div.group_news > ul > li')

  a = lis[0].select_one('a.news_tit')

  for li in lis:
    a = li.select_one('a.news_tit')
    row = [a.text, a['href']]
    sheet.append(row)

  today = datetime.today().strftime("%Y-%m-%d")

  wb.save(f"news/{today}_{keyword}.xlsx")
  wb.close()





keywords = ['삼성전자','LG에너지솔루션','SK하이닉스','NAVER','삼성바이오로직스','삼성전자우','카카오','삼성SDI','현대차','LG화학','기아','POSCO홀딩스','KB금융','카카오뱅크','셀트리온','신한지주','삼성물산','현대모비스','SK이노베이션','LG전자','카카오페이','SK','한국전력','크래프톤','하나금융지주','LG생활건강','HMM','삼성생명','하이브','두산중공업','SK텔레콤','삼성전기','SK바이오사이언스','LG','S-Oil','고려아연','KT&G','우리금융지주','대한항공','삼성에스디에스','현대중공업','엔씨소프트','삼성화재','아모레퍼시픽','KT','포스코케미칼','넷마블','SK아이이테크놀로지','LG이노텍','기업은행']

for keyword in keywords:
  print(keyword)
  get_news(keyword)

!zip -r /content/files.zip /content

import os

path = '/content'
files = os.listdir(path)

for name in files:
  new_name = name.split('.')[0] + '(뉴스).xlsx
  os.rename(f'/content/{name}', f'/content/{new_name}')

import urllib.request

url = 'https://ssl.pstatic.net/imgfinance/chart/item/area/year3/005930.png'
urllib.request.urlretrieve(url, "삼성전자.png")

import openpyxl
import urllib.request

wb = openpyxl.load_workbook('관리종목.xlsx')
sheet = wb['종목']

new_rows = list(sheet.rows)[1:]

for row in new_rows:
  img = row[1].value
  stk = row[0].value
  url = "https://ssl.pstatic.net/imgfinance/chart/item/area/year3/" + f"{img}.png"
  png = f"{stk}.png"
  urllib.request.urlretrieve(url, png)