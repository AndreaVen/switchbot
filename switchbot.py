# -*- coding: utf-8 -*-

import time
import hashlib
import hmac
import base64
import uuid
from dotenv import load_dotenv
import certifi
import os
import pycurl
from io import BytesIO

def header_list(token, secret):
    apiHeader = []
    nonce = uuid.uuid4()
    t = int(round(time.time() * 1000))
    string_to_sign = '{}{}{}'.format(token, t, nonce)

    string_to_sign = bytes(string_to_sign, 'utf-8')
    secret = bytes(secret, 'utf-8')

    sign = base64.b64encode(hmac.new(secret, msg=string_to_sign, digestmod=hashlib.sha256).digest())
    print('Authorization: {}'.format(token))
    print('t: {}'.format(t))
    print('sign: {}'.format(str(sign, 'utf-8')))
    print('nonce: {}'.format(nonce))

    # Build api header JSON
    apiHeader.append('Authorization: ' + token)
    apiHeader.append('Content-Type: ' + 'application/json')
    apiHeader.append('charset: ' + 'utf8')
    apiHeader.append('t :' + str(t))
    apiHeader.append('sign: ' + str(sign, 'utf-8'))
    apiHeader.append('nonce: ' + str(nonce))
    return apiHeader


load_dotenv()
token = os.environ['token']
secret = os.environ['secret_key']
mioHeader = header_list(token, secret)
headers = ["User-Agent: Python-PycURL", "Accept: application/json"]


device_number=os.environ['device_number']
buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, "https://api.switch-bot.com/v1.1/devices/{}/status".format(device_number))
c.setopt(pycurl.CAINFO, certifi.where())
c.setopt(c.HTTPHEADER, mioHeader)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
response = buffer.getvalue()
print(response.decode("utf-8"))
resp = response.decode("utf-8")
