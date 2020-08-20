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


def login(user_id, user_pass):
    try:
        # パスワードをハッシュ化
        encode_pass = user_pass.encode()
        hash_pass = hashlib.sha256(encode_pass).hexdigest()
        # SQLを作成し実行
        sql = 'select * from user where user_id = "{}" and user_pass = "{}" limit 1'.format(
            user_id, hash_pass)
        c.execute(sql)
        if c.fetchone() is None:
            return 401, ''
        result_token = setter_token(user_id)
        if not result_token['isSuccess']:
            return 401, ''
        message = 'ログインしました'
        if record_log(user_id, message):
            return 200, result_token['token']
        else:
            return 401, ''
    except:
        return 401, ''


def auto_login(token):
    try:
        # SQLを作成し実行
        sql = 'select user_id,expiration_date from user where token = "{}" limit 1'.format(
            token)
        c.execute(sql)
        record = c.fetchone()
        user_id = record[0]
        expiration_date = record[1]
        now = datetime.now()
        diff = now - expiration_date
        if diff.days > 0:
            return 401, ''
        result_token = setter_token(user_id)
        if not result_token['isSuccess']:
            return 401, ''
        message = 'ログインしました'
        if record_log(user_id, message):
            return 200, result_token['token']
        else:
            return 401, ''
    except:
        return 401, ''


def setter_token(user_id):
    try:
        token = secrets.token_urlsafe(64)
        # SQLを作成し実行
        sql = 'update user set token = "{}", expiration_date = NOW() where user_id = "{}"'.format(
            token, user_id)
        c.execute(sql)
        conn.commit()
        return {
            'isSuccess': True,
            'token': token
        }
    except:
        return {
            'isSuccess': False
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

    if Method == 'POST':
        headers = event['headers']
        if 'Authorization' in headers:
            token = headers['Authorization']
            status, new_token = auto_login(token)
        else:
            body = json.loads(event['body'])
            user_id = body['user_id']
            user_pass = body['user_pass']
            status, new_token = login(user_id, user_pass)
    else:
        status = 401

    if status == 200:
        response['statusCode'] = 200
        response['body'] = json.dumps({'token': new_token})

    else:
        response['statusCode'] = 401
    return response
