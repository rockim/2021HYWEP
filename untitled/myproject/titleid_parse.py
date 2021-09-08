import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myproject.settings")
import django
django.setup()
from mysite.models import Titleid

def parse_titleid():
    week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    title_ids = []
    for day in week:
        req = requests.get('https://comic.naver.com/webtoon/weekdayList?week=' + day)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # 웹툰 제목 크롤링

        webtoons_titles = soup.select(
            'dl > dt'
        )

        for n, i in enumerate(webtoons_titles):
            if n < 3:  # 중복 데이터 제거를 위한 넘기기
                continue
            for j in i.select('a[href]'):  # href에 적혀있는 titleid와 제목 매칭 ex ) { 'title' : [ titleid , day]}
                title_ids.append({i.text: [int(j['href'].split("/")[-1].split("=")[1].split("&")[0]),day]})
    return title_ids
if __name__=='__main__':
    titleid_data = parse_titleid()
    for titleid_dict in titleid_data:
        for t,day_id in titleid_dict.items():
            #print(t,day_id[1])
            Titleid(title=t,day = day_id[1],title_id=day_id[0],).save()

