import base64
import requests
import local_test
import pprint
import json
import io
import lib

url = 'https://23gjh3gnd7.execute-api.ap-northeast-1.amazonaws.com/empath/mastuo_lamda_test'
a = open('./empath/rec_02.wav', 'rb')
b = str(base64.b64encode(a.read()).decode('utf-8'))
# b = str(base64.b64encode(a.read()))
data = {'wav': b}
response = requests.post(url, json=data, headers={
    'Content-Type': 'application/json'})
c = response.json()
pprint.pprint(c)
# post.lambda_handler(b,1)

# import json
# import ast
# import requests
#
#
# def lambda_handler(event, context):
#     # #渡されたデータを習得しようとするとエラーが発生
#     # a = event['body']
#     # #string型をdict型に変換
#     # dic = ast.literal_eval(a)
#     # print(type(dic))
#     # return {
#     #     'statusCode': 200,
#     #     'body': json.dumps(dic['png'])
#     # }
#
#     a = event['body']
#     # string型をdict型に変換
#     dic = ast.literal_eval(a)
#     voice = dic['wav']
#     decode_voice = base64.b64decode(voice)
#     a = io.BytesIO(decode_voice)
#     url = 'https://api.webempath.net/v2/analyzeWav'
#     response = requests.post(url, {"apikey": "g-cFuBm5bStySlQjnyTGZEOtkLFvu17SlTh3bTccYXY"},
#                              files={'wav': a.read()})
#     return {
#         'statusCode': 200,
#         'body': response.json
#     }
