import requests as req
import json
import pandas as pd

url = 'https://tutorney.com/api/search/case?category=%E5%85%A8%E9%83%A8&page=1&address=220%E5%8F%B0%E7%81%A3%E6%96%B0%E5%8C%97%E5%B8%82%E6%9D%BF%E6%A9%8B%E5%8D%80%E5%85%89%E6%AD%A3%E8%A1%979%E5%B7%B72%E5%BC%842%E8%99%9F'
headers = {'user-agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

names = []
gender = []
pays = []
skills = []
days = []
froms = []
tos = []

for pg in range(1,6):
#    print(pg)
    full_url = 'https://tutorney.com/api/search/case?category=%E5%85%A8%E9%83%A8&address=234%E5%8F%B0%E7%81%A3%E6%96%B0%E5%8C%97%E5%B8%82%E6%B0%B8%E5%92%8C%E5%8D%80%E4%BF%9D%E7%A6%8F%E8%B7%AF%E4%BA%8C%E6%AE%B588%E5%B7%B714%E8%99%9F&page=' +  str(pg) 
#    print(full_url)
    if full_url.split('.')[0] == ('https://tutorney'):
        r = req.get(full_url, headers = headers)
        j = json.loads(r.text)
        main = j['results']
        
        for w in main:
            m = w[:24]
            j = json.loads(r.text)
            full = j['results'][m]
            g = full['name']
            Man = full['isMale']
            if Man == False:
                gender.append('女')
            else:
                gender.append('男')

            p = full['pay']
            s = full['skill']['subject']
            d = full['times'][0]['day']
            f = full['times'][0]['from']
            t = full['times'][0]['to']
            
            
            names.append(g)
            pays.append(p)
            skills.append(s)
            days.append(d)
            froms.append(f)
            tos.append(t)
            
data = [names, gender, pays, skills, days, froms, tos]
dex = ['名字', '性別', '時薪', '所需技能', '日期', '幾點開始', '幾點結束']
df = pd.DataFrame(data, index = dex, columns = list(range(1, len(names)+1)))

df.to_excel('Tutorney.xlsx')