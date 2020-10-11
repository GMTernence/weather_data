from MySQL import MysqlHelper
from util import get_soup
from util import date_range
from util import get_all


class Spider(object):
    def __init__(self, host='localhost', username='root', password='123qw456', db='weather_data', start_time='201501',
                 end_time='201912'):
        self.start_time = start_time
        self.end_time = end_time
        self.base_url = 'http://www.tianqihoubao.com/'
        self.history_url = 'http://www.tianqihoubao.com/lishi/%s/month/%s.html'
        self.mysql = MysqlHelper(host=host, username=username, password=password, db=db)

    def get_city(self):
        content = get_soup(self.base_url)
        province_list = content.find_all(name='table')[-1]
        province_list = province_list.find_all(name='td')
        for index, province in enumerate(province_list):
            href = province.find(name='a')
            province_name = href.get_text()
            content = get_soup(self.base_url + href.get('href'))
            content = content.find(name='div', id='content')
            city_list = content.find(name='table').find_all(name='td')
            for city in city_list:
                city_href = city.find(name='a')
                city = city_href.get_text()
                spell = city_href.get('href').split('.')[0].split('/')[-1]
                sql = 'INSERT INTO city_list(province, city, spell) values (%s, %s, %s)'
                params = [province_name, city, spell]
                print(params)
                self.mysql.insert(sql, params)
                self.get_weather(province_name, city, spell)

    def get_weather(self, province, city, spell):
        month_list = date_range(self.start_time, self.end_time)
        for month in month_list:
            url = self.history_url % (spell, month)
            print(url)
            weather_list = get_soup(url).find(name='div', id='content').find_all(name='tr')
            # remove the first element
            del (weather_list[0])
            for weather in weather_list:
                detail = weather.find_all(name='td')
                date = detail[0].find(name='a').get('href').split('.')[0].split('/')[-1]
                date = get_all(date)
                state = detail[1].get_text()
                state = get_all(state)
                temperature = detail[2].get_text()
                temperature = get_all(temperature)
                wind = detail[3].get_text()
                wind = get_all(wind)
                print(province, city, date, state, temperature, wind)
                sql = 'INSERT INTO weather_list(weather_date, province, city, spell, state, temperature, wind) ' \
                      'values (%s, %s, %s, %s, %s, %s, %s)'
                params = [date, province, city, spell, state, temperature, wind]
                self.mysql.insert(sql=sql, params=params)

    def run(self):
        self.get_city()
