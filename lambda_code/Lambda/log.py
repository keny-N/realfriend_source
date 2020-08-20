import os
import json
import pymysql.cursors
from datetime import datetime

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


def token_exists(token):
    try:
        sql = 'select user_id,expiration_date from user where token = "{}" limit 1'.format(
            token)
        c.execute(sql)
        record = c.fetchone()
        user_id = record[0]
        expiration_date = record[1]
        now = datetime.now()
        diff = now - expiration_date
        if diff.days > 0:
            return {
                'status': 401
            }
        return {
            'status': 200,
            'user_id': user_id
        }
    except:
        return{
            'status': 401
        }


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
    headers = event['headers']
    if 'Authorization' in headers:
        token = headers['Authorization']
        session = token_exists(token)

        if session['status'] != 200:
            response['statusCode'] = session['status']
            return response

    else:
        response['statusCode'] = 401
        return response

    try:
        sql = 'select data,logged_in from log where user_id = "{}" order by logged_in desc limit 20'.format(
            session['user_id'])
        c.execute(sql)
        logs = []
        # 0:ログ内容,1:ログ記録時間
        for record in c.fetchall():
            message = record[0]
            date = record[-1].strftime('%Y-%m-%d %H:%M:%S')
            logs.append([message, date])
        response['statusCode'] = 200
        response['body'] = json.dumps({'logs': logs})
    except:
        response['statusCode'] = 500
    return response
