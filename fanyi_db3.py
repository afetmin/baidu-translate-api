# coding:utf-8
import requests
import hashlib
import sqlite3


def conn_sqlite(input):
    conn = sqlite3.connect('{}.db3'.format(input))
    cur = conn.cursor()
    cursor = cur.execute("select * from content order by id asc limit 0,10;")
    return cursor


def get_fanyi(q):
    salt = '123'
    appid = '20180115000115453'
    secret = 'AHYyafcYLzm3q0fkfQ7z'
    s = appid + q + salt + secret
    sign = string_to_md5(s)
    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?' \
          'q={}&from=zh&to=en&appid={}&salt={}&sign={}'.format(q, appid, salt, sign)
    r = requests.get(url)
    trans_result = r.json()['trans_result'][0]
    return trans_result


def string_to_md5(s):
    md5 = hashlib.md5(s.encode('utf-8')).hexdigest()
    return md5

def start():
    while 1:
        cursor = conn_sqlite('test')
        for each in cursor:
            *_, title, des = each
            trans_result = get_fanyi(title)

