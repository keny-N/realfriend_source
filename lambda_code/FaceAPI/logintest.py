import requests as rs
import pprint
import json

url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login'

post_data = {
    'user_id': 'Ryu',
    'user_name': 'RRyu',
    'user_pass': 'RRRyu',
    'friend_name': 'Rein',
    'friend_img': '/friend/Rein_img',
}
headers = {
    'Authorization': 'zuV8TQSNsifNnea9TFCDVtmjJnOQySO-gUMaWuPstjnJWSpUpZT2P8rg-ywQ0bV2iNbo3FcLXYP0hg0Jb6cCzA'
}
response = rs.post(url, headers=headers)
pprint.pprint(response.status_code)
try:
    pprint.pprint(response.json())
except:
    print('error')
