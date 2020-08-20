import requests

URL = 'https://23gjh3gnd7.execute-api.ap-northeast-1.amazonaws.com/empath/matsuo_form_data_test'
header = {'Content-Type':'image/jpeg'}
filename = 'test.jpg'
image = open(filename,'rb')
mimetype = 'image/jpeg'
files = {'param_name':(filename,image,mimetype)}
response = requests.post(url=URL,headers=header,files=files)
print(response.content)
