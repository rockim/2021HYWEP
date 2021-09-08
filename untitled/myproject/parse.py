import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myproject.settings")
import django
django.setup()
from mysite.models import Webtoon


def parse_webtoon():
    week = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    webtoons= []
    for day in week:
        req = requests.get('https://comic.naver.com/webtoon/weekdayList?week=' + day)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        # 웹툰 제목 크롤링
        webtoons_titles = soup.select(
            'dl > dt'
        )
        # 웹툰 작가명 크롤링
        webtoons_authors = soup.select(
            'dl > dd.desc'
        )
        # 웹툰 평점 크롤링
        webtoons_rates = soup.select(
            'div > strong'
        )
        for i in range(3, len(webtoons_titles)):
            #배열로 추가 [ [title,author,rate]...]
            webtoons.append([webtoons_titles[i].text.replace("\n", ""), webtoons_authors[i].text.replace("\n", ""),
                  webtoons_rates[i].text.replace("\n", "")])
    return webtoons
if __name__=='__main__':
    webtoon_datas = parse_webtoon()
    for webtoon_data in webtoon_datas:
        (t,a,r) = webtoon_data
        #print(t,a,r)
        Webtoon(title=t,author = a,rate=r).save()



