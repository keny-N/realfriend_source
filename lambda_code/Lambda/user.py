import os
import json
import pymysql.cursors
import hashlib
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


def select(user_id):
    try:
        # SQLを作成し実行
        sql = 'select user_id,user_name from user where user_id = "{}" limit 1'.format(
            user_id)
        c.execute(sql)
        user = list(c.fetchone())
        return 200, user
    except:
        return 500, []


def insert(user_id, user_name, user_pass):
    try:
        # パスワードをハッシュ化
        encode_pass = user_pass.encode()
        hash_pass = hashlib.sha256(encode_pass).hexdigest()
        # SQLを作成し実行
        sql = 'insert into user values ("{}","{}","{}",NULL,NULL)'.format(
            user_id, user_name, hash_pass)
        c.execute(sql)
        message = '登録が完了しました'
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
    except:
        return 500


def update_profile(user_id, user_name):
    try:
        print(48)
        # SQLを作成し実行
        sql = 'update user set user_name = "{}" where user_id = "{}"'.format(
            user_name, user_id)
        c.execute(sql)
        message = 'プロフィール情報を更新しました'
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
    except:
        return 500


def update_password(user_id, user_pass):
    try:
        # パスワードをハッシュ化
        encode_pass = user_pass.encode()
        hash_pass = hashlib.sha256(encode_pass).hexdigest()
        # SQLを作成し実行
        sql = 'update user set user_pass = "{}" where user_id = "{}"'.format(
            hash_pass, user_id)
        c.execute(sql)
        message = 'パスワードを更新しました'
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
    except:
        return 500


def delete(user_id):
    try:
        # SQLを作成し実行
        sql = 'delete from friend where user_id = "{}"'.format(
            user_id)
        c.execute(sql)
        sql = 'delete from log where user_id = "{}"'.format(
            user_id)
        c.execute(sql)
        sql = 'delete from user where user_id = "{}"'.format(
            user_id)
        c.execute(sql)
        conn.commit()
        return 200
    except:
        return 500


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
            'status': 500
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
    if 'Authorization' in headers:
        token = headers['Authorization']
        session = token_exists(token)
        if session['status'] != 200:
            response['statusCode'] = session['status']
            return response

    elif Method != 'POST':
        response['statusCode'] = 401
        return response

    if Method == 'GET':
        user_id = session['user_id']
        response['statusCode'], user_info = select(user_id)
        if response['statusCode'] == 200:
            response['body'] = json.dumps({'user': user_info})
    elif Method == 'POST':
        body = json.loads(event['body'])
        user_id = body['user_id']
        user_name = body['user_name']
        user_pass = body['user_pass']
        response['statusCode'] = insert(user_id, user_name, user_pass)
    elif Method == 'PUT':
        body = json.loads(event['body'])
        try:
            path = event['path'].split('/')[2]
        except:
            path = None
        user_id = session['user_id']
        if path == 'pass':
            user_pass = body['user_pass']
            response['statusCode'] = update_password(user_id, user_pass)
        else:
            user_name = body['user_name']
            response['statusCode'] = update_profile(user_id, user_name)
    elif Method == 'DELETE':
        user_id = session['user_id']
        response['statusCode'] = delete(user_id)
    else:
        response['statusCode'] = 403

    return response
