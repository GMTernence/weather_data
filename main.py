"""
author: Yann Liu
target: scrawl the weather data from http://www.tianqihoubao.com/
usage:
    host: the ip of mysql， default 127.0.0.1
    username: the user of mysql, default root
    password：the password of mysql
    db: database that store weather data
    start_time: when to spider, default Jan,2015
    end_time: when to end, default Dec,2019
"""
from Spider import *

if __name__ == '__main__':
    spider = Spider(host='127.0.0.1', username='root', password='123qw456',
                    db='weather_data', start_time='201501', end_time='201912')
    spider.run()
