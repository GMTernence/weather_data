from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
import random

headers = {
    'User_Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 '
                  'Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zen-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'close',
    'Cookie': '__gads=ID=8c728d21376f646e:T=1602231314:S=ALNI_MZvA6O9-r-KadzZVJEw-SnZ8XvmsQ; __51cke__=; '
              'Hm_lvt_f48cedd6a69101030e93d4ef60f48fd0=1602231319,1602231563,1602231574,1602231611; '
              'ASP.NET_SessionId=io3t2xf4ihbusa45lvj3jcz2; bdshare_firstime=1602232900153; '
              'Hm_lpvt_f48cedd6a69101030e93d4ef60f48fd0=1602241725; '
              '__tins__4560568=%7B%22sid%22%3A%201602241725208%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A'
              '%201602243525208%7D; __51laig__=45 '
}


def get_soup(url):
    try:
        response = requests.get(url=url, headers=headers, timeout=None)
        soup = BeautifulSoup(response.text, 'lxml')
        time.sleep(random.randint(30, 50))
        return soup
    except requests.exceptions.ConnectionError:
        print('web error')
        time.sleep(100)
        get_soup(url)


def date_range(start_time, end_time):
    result = []
    date_list = list(pd.date_range(start=start_time + '01', end=end_time + '01', freq='M'))
    for date in date_list:
        result.append(date.strftime('%Y%m'))
    result.append(end_time)
    return result


# remove blank and space
def get_all(destination):
    return destination.replace("\n", "").replace("\r", "").replace(" ", "")
