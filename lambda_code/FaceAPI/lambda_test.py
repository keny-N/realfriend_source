import requests as rs
import pprint
import json

url = 'https://abwp9ub4n8.execute-api.ap-northeast-1.amazonaws.com/realfriend/test'
response = rs.post(url)
pprint.pprint(response.json())
