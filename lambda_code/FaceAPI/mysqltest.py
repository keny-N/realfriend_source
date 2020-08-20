import requests as rs
import pprint
import json

# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/0024'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/pass'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/log'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/login'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/logout'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/all/1'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/77'
url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/counter'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/favorable'

# file = open('./FaceAPI/human.jpg', 'br')
# b64_img = base64.b64encode(file.read())
post_data = {
    'user_id': 'Mattsun',
    'user_name': 'Takahiro',
    'user_pass': 'pass',
    'friend_name': 'Rein',
    'friend_img': '/friend/Rein_img',
}
post_data2 = {
    'user_id': 'MA',
    'user_name': 'RRyu',
    'user_pass': 'MA',
    'friend_name': 'Rein',
    'friend_img': '/friend/Rein_img',
}
put_data = {
    'user_id': 'Fujiie',
    'user_name': 'FFujie',
    'user_pass': 'FFFujie',
    'friend_name': 'RIRI',
    'friend_img': '/friend/RIRI_img',
}
fav_data = {
    'friend_id': 77,
    'friend_name': 'Rein',
    'result': 1
}

counter_data = {
    'login_count': 1,
    'autoLogin_count': 1,
    'camera_count': 1,
    'news_count': 1
}
headers = {
    'Authorization': 'CCixm0X9MpHVovG02Rlrc_a_HWzkBZRLq2VuPEkEYDHVtIwkvNWHASeV5619Da5BXTW5DUQfvZLThyYuQ4NaoQ'
}
# sql = 'insert into friend values (0,"{}","{}",{},0)'.format('a', 'b', 'c')
# print(sql)
# response = rs.get(url, headers=headers)
# response = rs.post(url, json=post_data)
# response = rs.post(url, headers=headers)
# response = rs.put(url, headers=headers, json=put_data)
# response = rs.delete(url, headers=headers)
# response = rs.post(url, json=counter_data)
# response = rs.post(url, headers=headers, json=fav_data)
response = rs.post(url, json=counter_data)
pprint.pprint(response.status_code)
try:
    pprint.pprint(response.json()['counts'])
except:
    print('Empty')
