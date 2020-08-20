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


def select_all(user_id):
    try:
        # SQLを作成し実行
        sql = 'select friend_id,friend_name,friend_img,friend_favorable from friend where user_id = "{}"'.format(
            user_id)
        c.execute(sql)
        friend_info = []
        # 0:フレンドID,1:ユーザID,2:フレンド名,3:フレンド画像,4:フレンド感情値
        for record in c.fetchall():
            friend_info.append(record)
        friends = friend_info
        return 200, friends
    except:
        return 500, []


def select_one(friend_id):
    try:
        # SQLを作成し実行
        sql = 'select friend_id,friend_name,friend_img,friend_favorable from friend where friend_id = {}'.format(
            friend_id)
        c.execute(sql)
        # 0:フレンドID,1:ユーザID,2:フレンド名,3:フレンド画像,4:フレンド感情値
        friends = list(c.fetchone())
        return 200, friends
    except:
        return 500, friends


def insert(user_id, friend_name, friend_img):
    try:
        # SQLを作成し実行
        sql = 'insert into friend values (0,"{}","{}","{}",0)'.format(
            user_id, friend_name, friend_img)
        c.execute(sql)
        message = '{}さんをフレンド登録しました'.format(
            friend_name)
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
    except:
        return 500


def update(friend_name, friend_img, friend_id, user_id):
    try:
        # SQLを作成し実行
        sql = 'update friend set friend_name = "{}",friend_img = "{}" where friend_id = {}'.format(
            friend_name, friend_img, friend_id)
        c.execute(sql)
        message = '{}さんの情報を更新しました'.format(
            friend_name)
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
    except:
        return 500


def delete(friend_id, friend_name, user_id):
    try:
        sql = 'delete from friend where friend_id = {}'.format(
            friend_id)
        c.execute(sql)
        message = '{}さんをフレンドから削除しました'.format(
            friend_name)
        if record_log(user_id, message):
            return 200
        else:
            raise Exception
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
        if friend_list is None:
            return {
                'status': 500
            }
        elif friend_list == []:
            return {
                'status': 200,
                'user_id': user_id,
            }
        return {
            'status': 200,
            'user_id': user_id,
            'friend_list': friend_list
        }
    except:
        return{
            'status': 401
        }


def check_auth(user_id):
    try:
        sql = 'select friend_id from friend where user_id = "{}"'.format(
            user_id)
        c.execute(sql)
        friend_list = [friends_tuple[0] for friends_tuple in c.fetchall()]
        return friend_list
    except:
        return None


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
            # 'Access-Control-Allow-Origin': 'https://realfriend.online'
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

    if Method == 'GET':
        flg = event['path'].split('/')[2]
        if flg == 'all':
            response['statusCode'], friend_info = select_all(
                session['user_id'])
        else:
            friend_id = int(event['pathParameters']['friendid'])
            if friend_id not in session['friend_list']:
                response['statusCode'] = 401
                return response
            response['statusCode'], friend_info = select_one(friend_id)
        if response['statusCode'] == 200:
            response['body'] = json.dumps({'friends': friend_info})
    elif Method == 'POST':
        body = json.loads(event['body'])
        user_id = session['user_id']
        friend_name = body['friend_name']
        friend_img = body['friend_img']
        response['statusCode'] = insert(user_id, friend_name, friend_img)
    elif Method == 'PUT':
        body = json.loads(event['body'])
        friend_name = body['friend_name']
        friend_img = body['friend_img']
        friend_id = int(event['pathParameters']['friendid'])
        if friend_id not in session['friend_list']:
            response['statusCode'] = 401
            return response
        user_id = session['user_id']
        response['statusCode'] = update(
            friend_name, friend_img, friend_id, user_id)
    elif Method == 'DELETE':
        body = json.loads(event['body'])
        friend_id = int(event['pathParameters']['friendid'])
        friend_name = body['friend_name']
        user_id = session['user_id']
        if friend_id not in session['friend_list']:
            response['statusCode'] = 401
        response['statusCode'] = delete(friend_id, friend_name, user_id)
    else:
        response['statusCode'] = 403

    return response
