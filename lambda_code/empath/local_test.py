# import
# import pprint
# url = 'https://api.webempath.net/v2/analyzeWav'
# response = requests.post(url,{"apikey":"g-cFuBm5bStySlQjnyTGZEOtkLFvu17SlTh3bTccYXY"}, files = {'wav':open('./rec_02.wav','rb')})
# pprint.pprint(response.json())
import base64
import requests
import pprint
import io


def lambda_handler(event, context):
    voice = event
    decode_voice = base64.b64decode(voice)
    a = io.BytesIO(decode_voice)
    url = 'https://api.webempath.net/v2/analyzeWav'
    response = requests.post(url, {"apikey": "g-cFuBm5bStySlQjnyTGZEOtkLFvu17SlTh3bTccYXY"},
                             files={'wav': a.read()})
    pprint.pprint(response.json())