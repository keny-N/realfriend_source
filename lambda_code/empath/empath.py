import ast
import requests
import base64
import io
import json


def run(event, context):
    print(event)
    a = event['body']
    # string型をdict型に変換
    dic = ast.literal_eval(a)
    voice = dic['wav']
    # voice = a['wav']
    decode_voice = base64.b64decode(voice)
    a = io.BytesIO(decode_voice)
    url = 'https://api.webempath.net/v2/analyzeWav'
    response = requests.post(url, {"apikey": "g-cFuBm5bStySlQjnyTGZEOtkLFvu17SlTh3bTccYXY"},
                             files={'wav': a.read()})
    return {
        'statusCode': 200,
        'body': json.dumps(response.json())
    }
