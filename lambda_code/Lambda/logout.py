import os
import json
import pymysql.cursors
import hashlib
import secrets
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


def logout(user_id):
    try:
        # SQLを作成し実行
        sql = 'update user set token = NULL where user_id = "{}";'.format(
            user_id)
        c.execute(sql)
        conn.commit()
        message = 'ログアウトしました'
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
        return 200
    except:
        return 500


def token_exists(token):
    try:
        sql = 'select user_id from user where token = "{}" limit 1'.format(
            token)
        c.execute(sql)
        record = c.fetchone()
        user_id = record[0]
        return {
            'statusCode': 200,
            'user_id': user_id,
        }
    except:
        return{
            'statusCode': 401
        }


def record_log(user_id, message):
    try:
        # SQLを作成し実行
        sql = 'insert into log (log_num,user_id,data) values (0,"{}","{}");'.format(
            user_id, message)
        c.execute(sql)
        conn.commit()
        return True
    except:
        return False


def main(event, context):

    global conn
    global c
    conn, c = setting_db()

    Method = event['requestContext']['httpMethod']
    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    headers = event['headers']
    if Method == 'POST':
        if 'Authorization' in headers:
            token = headers['Authorization']
            session = token_exists(token)
        if session['statusCode'] == 200:
            response['statusCode'] = logout(session['user_id'])
        else:
            response['statusCode'] = session['statusCode']
    else:
        response['statusCode'] = 403

    return response
