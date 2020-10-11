from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from MySQL import *

app = Flask(__name__)
host = '127.0.0.1'
username = 'root'
password = '123qw456'
db = 'weather_data'


@app.route('/', methods=['get', 'post'])
def index():
    return render_template('/index.html')


@app.route('/month', methods=['post', 'get'])
def month():
    month_time = request.args.get('month')
    spell = request.args.get('city')
    helper = MysqlHelper(host=host, username=username, password=password, db=db)
    sql = 'select * from weather_list where DATE_FORMAT(weather_date, \'%%Y%%m\') = %s and spell = %s'
    params = [month_time, spell]
    result = helper.get_all(sql=sql, params=params)
    print(month_time, spell)
    return jsonify(result)


@app.route('/day', methods=['post', 'get'])
def day():
    day_time = request.args.get('day')
    spell = request.args.get('city')
    helper = MysqlHelper(host=host, username=username, password=password, db=db)
    sql = 'select * from weather_list where DATE_FORMAT(weather_date, \'%%Y%%m%%d\') = %s and spell = %s'
    params = [day_time, spell]
    result = helper.get_one(sql=sql, params=params)
    print(day_time, spell)
    return jsonify(result)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)
