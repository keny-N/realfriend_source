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


def update_favorable(user_id, friend_id, friend_name, result):
    try:
        # SQLを作成し実行
        sql = 'update friend set friend_favorable = friend_favorable + {} where friend_id = {};'.format(
            result, friend_id)
        c.execute(sql)
        if result > 0:
            message = '{}さんの好感度が上がりました'.format(friend_name)
        elif result < 0:
            message = '{}さんの好感度が下がりました'.format(friend_name)
        else:
            message = '{}さんの好感度には変化がありませんでした'.format(friend_name)
        if not record_log(user_id, message):
            raise Exception
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
        friend_list = check_auth(user_id)
        if friend_list == []:
            return {
                'status': 500
            }
        return {
            'status': 200,
            'user_id': user_id,
            'friend_list': friend_list
        }
    except:
        return{
            'status': 500
        }


def check_auth(user_id):
    try:
        sql = 'select friend_id from friend where user_id = "{}"'.format(
            user_id)
        c.execute(sql)
        friend_list = [friends_tuple[0] for friends_tuple in c.fetchall()]
        return friend_list
    except:
        return []


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

    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
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
    body = json.loads(event['body'])
    friend_id = body['friend_id']
    if friend_id not in session['friend_list']:
        response['statusCode'] = 401
        return response
    friend_name = body['friend_name']
    result = body['result']
    user_id = session['user_id']
    response['statusCode'] = update_favorable(
        user_id, friend_id, friend_name, result)
    return response
