import os
import json
import base64
import requests
import cognitive_face as CF
from io import BytesIO
from datetime import datetime


def face_api(image):
    # FaceAPI利用に必要なKeyとURLを変数に代入
    face_api_key = os.environ['FACE_API_KEY']
    face_api_url = os.environ['FACE_API_URL']
    CF.Key.set(face_api_key)
    CF.BaseUrl.set(face_api_url)
    # FaceAPI処理
    try:
        # FaceAPI呼び出す
        faces = CF.face.detect(image, face_id=False,
                               landmarks=False, attributes='emotion')
        if faces == []:
            return {
                'statusCode': 500
            }
        # 感情に関係ある部分のみを取り出す
        emotion = faces[0]['faceAttributes']['emotion']
        # 1番の感情を取り出す
        top_emotion = sorted(
            emotion.items(), key=lambda x: x[1], reverse=True)[0]
        # 感情の正負判定
        # 正の感情
        if top_emotion[0] in ('happiness', 'surprise'):
            result = top_emotion[1]
        # 負の感情
        elif top_emotion[0] in ('anger', 'contempt', 'disgust', 'fear', 'sadness'):
            result = top_emotion[1] * -1
        # 無感情
        else:
            result = 0
        return {
            'statusCode': 200,
            'result': result * 5
        }
    # エラー時
    except:
        return {
            'statusCode': 500,
        }


def empath(voice):
    # Empath利用に必要なKeyとURLを変数に代入
    key = os.environ['EMPATH_KEY']
    url = os.environ['EMPATH_URL']
    # Empath処理
    response = requests.post(url, {"apikey": key},
                             files={'wav': voice.read()})
    response_body = json.loads(response.text)
    response_error = response_body['error']

    # empath成功時
    if response_error == 0:
        # 1番の感情を取り出す
        top_emotion = sorted(response_body.items(),
                             key=lambda x: x[1], reverse=True)[0]
        attribute = top_emotion[0]
        response = {
            'statusCode': 200
        }

        # 感情の正負判定
        # 正の感情
        if attribute == 'joy' or attribute == 'energy':
            response['result'] = top_emotion[1] / 5
        # 負の感情
        elif attribute == 'anger' or attribute == 'sorrow':
            response['result'] = (top_emotion[1] / 5) * -1
        # 無感情
        else:
            response['result'] = 0

        return response
    # エラー時
    else:
        return {
            'statusCode': 500,
        }


def create_request(face_result, empath_result):
    if face_result['statusCode'] != 200:
        return face_result['statusCode'], 0
    elif empath_result['statusCode'] != 200:
        return empath_result['statusCode'], 0
    else:
        result = face_result['result'] + empath_result['result']
        return 200, result


def main(event, context):
    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }
    headers = event['headers']
    if 'Authorization' not in headers:
        response['statusCode'] = 401
        return response
    token = headers['Authorization']
    try:
        body = json.loads(event['body'])
        body_img = body['image']
        b64_img = base64.b64decode(body_img)
        image = BytesIO(b64_img)
        face_result = face_api(image)
        body_voice = body['voice']
        b64_voice = base64.b64decode(body_voice)
        voice = BytesIO(b64_voice)
        empath_result = empath(voice)
        response['statusCode'], result = create_request(
            face_result, empath_result)
        if response['statusCode'] != 200:
            return response
        url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/favorable'
        head = {
            'Authorization': token
        }
        post_data = {
            'friend_id': body['friend_id'],
            'friend_name': body['friend_name'],
            'result': result,
        }
        request_res = requests.post(url, headers=head, json=post_data)
        response['statusCode'] = request_res.status_code
        if response['statusCode'] != 200:
            return response
        response['body'] = json.dumps({'result': result})
    except:
        response['statusCode'] = 500
    return response
