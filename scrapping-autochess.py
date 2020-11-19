from bs4 import BeautifulSoup
import requests
import lxml

ac = 'https://www.zizouqi.com/charactor?lan=en&mobile=false'
wf = 'https://wandi-frog.firebaseapp.com'
baseUrl = 'https://www.zizouqi.com'

source = requests.get(ac).text
soup = BeautifulSoup(source, 'lxml')

result = soup.find('ul', class_='charactor-head-ul')

arr = []

url = result.find_all('a')
for x in url:
  # print(x.text, x['href'])
  arr.append({
    'name': x.text,
    'url': baseUrl + x['href'],
  })

print(1, arr[0]['name'])
arrList = ''
# for a in arr:
  # arrList += a.url + '\n'

chessList = []

from googletrans import Translator

def translateToEN(str):
  str = str.replace('\n', '').replace(' ', '')
  translator = Translator()
  return translator.translate(str).text

def removeTrim(str):
  return str.replace('\n', '').replace(' ', '')

for data in arr[0:len(arr)]:
  source = requests.get(data['url']).text
  soup = BeautifulSoup(source, 'lxml')
  
  try:
    result = 'dummy'
    name = data['name'] or 'ERROR'
    cost = soup.find('span', class_='value').text or 'ERROR'
    chessClass = soup.select('li.race span')[0].text or 'ERROR'
    race = soup.select('li.career span')[0].text or 'ERROR'
  except:
    print("An exception occurred")

  # chessClass = translator.translate(chessClass).text

  chess = {
    'name': name,
    'class': translateToEN(chessClass),
    'race': translateToEN(race),
    'cost': cost,
  }
  print(chess)
  chessList.append(chess)

import json
with open('data.json', 'w') as outfile:
  json.dump(chessList, outfile)

# print(arrList)
# with open('do_re_mi.txt', 'w') as f:
#     f.write(arrList)
