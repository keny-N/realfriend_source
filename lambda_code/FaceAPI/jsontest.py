import secrets
import requests as rs
import pprint
from datetime import datetime

url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/test'
url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login'

n = 64

a = secrets.token_urlsafe(n)
# b = secrets.token_bytes(n)
# c = secrets.token_hex(n)
# print(a)
# print(type(a))
# print(len(a))
# print(b)
# print(type(b))
# print(len(b))
# print(c)
# print(type(c))
# print(len(c))

headers = {
    'Authorization': 'IlNlikSQdjwl6ma5q8yl0metmzCfClsw1qeTCC5kOOHnecY_bW6Z6v8cgJrY-1-Xt-ghsguVCJbEcDOTo7udGA'
}

# response = rs.get(url)
post_data = {
    'user_id': 'Ryu',
    'user_name': 'RRyu',
    'user_pass': 'RRRyu',
}
# response = rs.post(url, json=post_data)
response = rs.post(url, headers=headers)
pprint.pprint(response.status_code)
# if response.status_code != 200:
#     print(response.status_code)
# else:
#     pprint.pprint(response.json())

# friends = [friends_tuple[0] for friends_tuple in c.fetchall]

# now = datetime.now()
# create_date = datetime(2020, 8, 1, 3, 1, 55)
# diff = now-create_date
# if diff.days > 0:
#     print('1日経過しています')
# if diff.seconds > 179:
#     print('三分経過しています')
