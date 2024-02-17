# -*- coding: utf-8 -*-

import time
import hashlib
import hmac
import base64
import uuid
import certifi
import pycurl
from io import BytesIO
from dotenv import load_dotenv
import os

class Switchbot:
    token=''
    key=''

    def __init__(self):
        load_dotenv()
        token = os.environ['token']
        secret = os.environ['secret_key']
        self.token=token
        self.secret=secret




    def generate_header(self,token, secret):
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



    def get_temp_hum(self,device_id):

        header=self.generate_header(self.token,self.secret)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, "https://api.switch-bot.com/v1.1/devices/{}/status".format(device_id))
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.HTTPHEADER, header)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        response = eval(buffer.getvalue().decode("utf-8"))
        if response['statusCode']==100:
            return True

        else:
             Exception


    def evaluete_response(self,response):
        try:
            status=response['statusCode']
            # status=100

            if (status==100):
                return True
            elif(status==190):
                Exception("Device internal error due to device states not synchronized with server")
            else:
                Exception("Http 401 Error. User permission is denied due to invalid token.")

        except Exception:
            raise TypeError

