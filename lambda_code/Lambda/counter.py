import os
import json
import pymysql.cursors

conn = None
c = None

# DBの初期設定


def setting_db():
    conn = pymysql.connect(
        user=os.environ['DB_USER'],
        passwd=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        db=os.environ['DB_NAME']
    )
    c = conn.cursor()
    return conn, c


def setter_count(login, auto, camera, news):
    try:
        # SQLを作成し実行
        sql = 'insert into counter (login_count,autoLogin_count,camera_count,news_count) values ({},{},{},{});'.format(
            login, auto, camera, news)
        c.execute(sql)
        conn.commit()
        return 200
    except:
        return 500


def getter_count():
    try:
        # SQLを作成し実行
        sql = 'select sum(login_count),sum(autoLogin_count),sum(camera_count),sum(news_count) from counter;'
        c.execute(sql)
        counter = c.fetchone()
        counts = {
            'login_count': int(counter[0]),
            'autoLogin_count': int(counter[1]),
            'camera_count': int(counter[2]),
            'news_count': int(counter[3])
        }
        return 200, json.dumps({'counts': counts})
    except:
        return 500, []


def main(event, context):

    global conn
    global c
    conn, c = setting_db()

    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    Method = event['requestContext']['httpMethod']
    if Method == 'GET':
        response['statusCode'], body = getter_count()
        if response['statusCode'] == 200:
            response['body'] = body
    elif Method == 'POST':
        body = json.loads(event['body'])
        login = body['login_count']
        auto = body['autoLogin_count']
        camera = body['camera_count']
        news = body['news_count']
        response['statusCode'] = setter_count(login, auto, camera, news)
    else:
        return {
            'statusCode': 403,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
    return response
