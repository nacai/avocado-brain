from conversation.api import docomo_api_key

import requests
import json

KEY = docomo_api_key.KEY

URL = 'https://api.apigw.smt.docomo.ne.jp/dialogue/v1/dialogue?APIKEY=' + KEY

context = ''

def get_reply(text):
    global context
    payload = {'utt': text, 'context': context}
    headers = {'Content-type': 'application/json'}

    r = requests.post(URL, data=json.dumps(payload), headers=headers)
    data = r.json()

    response = data['utt']
    context = data['context']
    return response

