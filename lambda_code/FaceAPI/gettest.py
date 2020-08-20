import requests as rs
import pprint
import json

# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/0024'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/pass'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/users/log'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/all'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one'
url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/one/93'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/counter'
# url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/friends/favorable'
post_data = {
    'user_id': 'Ryu',
    'user_name': 'RRyu',
    'user_pass': 'RRRyu',
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
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}
headers = {
    'Authorization': '5rvG0PIiPf61IQS6UgJ4UpZHqZoziNJhjRegepwbVu9-c_ojfZScF27aFIRea5kNK5L9CrElxxPeap7S1aitog'
}
response = rs.put(url, headers=headers, json=put_data)
pprint.pprint(response.status_code)
try:
    pprint.pprint(response.json())
except:
    print('error')
