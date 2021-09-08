import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","myproject.settings")
import django
django.setup()
from selenium import webdriver
from mysite.models import SpecificWebtoon, BestComment

base_url = 'https://comic.naver.com/webtoon/weekday'
os.chdir('C:/Users/yjm29/Downloads/chromedriver_win32')

def drive(url):
    driver = webdriver.Chrome('./chromedriver') # drive 객체 불러오기
    driver.implicitly_wait(1) # 3초 후 작동
    driver.get(url) #url 접속
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    return driver, soup
def make_link(webtoon_url, page_count):
    return webtoon_url + '&page=' + str(page_count)
def comment_crawler(titleid, no):
    driver, _ = drive(base_url)
    """
    comment_url = make_link(base_url,no)
    headr = {
        "Host" : ""
    }
    """
    comment_url = 'https://comic.naver.com/comment/comment?titleId=' + str(titleid) + '&no=' + str(no)
    driver.get(comment_url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    best_comments = []
    best_comments += list(map(lambda x: x.text, soup.select('.u_cbox_contents')))
    driver.close()
    return best_comments
def episode_count(titleid,day):
    req = requests.get("https://comic.naver.com/webtoon/list?titleId=" + str(titleid) + "&weekday=" + day)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    no = soup.select(
        'td > a'
    )
    # 웹툰 나온 횟수 크롤링
    for n, i in enumerate(no):
        if n == 3:
            no = int((i['href'].split("=")[2].split("&")[0]))
            break
    return no
def parse_comment(titleid,day):
    star_point_list = []
    best_comments = []
    no = episode_count(titleid,day)
    for n in range(1,no+1):
        req = requests.get("https://comic.naver.com/webtoon/detail?titleId="+str(titleid)+"&no="+str(n)+"&weekday="+day)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        date = soup.select(
            'dl > dd.date'
        )[0].text
        star_point = soup.select(
            'span > strong'
        )[0].text
        star_point_list += [[n,star_point,date]]
        best_comments += comment_crawler(titleid,n)

"""
    for star_p in star_point_list:
        n,s,d = star_p
        SpecificWebtoon(no=n,star_point = s,date = d).save()
    for best_c in best_comments:
        BestComment(best_comment=best_c).save()
"""