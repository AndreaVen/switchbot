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
import json
class Switchbot:
    token=''
    key=''

    def __init__(self):
       self.set_token_and_secret()
       self.device_list=[]
       self.sensor_dict={}


    def set_token_and_secret(self):
        load_dotenv()
        token = os.environ['token']
        secret = os.environ['secret_key']
        self.token = token
        self.secret = secret






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



    def get_devices(self):
        header = self.generate_header(self.token, self.secret)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, "https://api.switch-bot.com/v1.1/devices")
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.HTTPHEADER, header)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        response = json.loads(buffer.getvalue().decode("utf-8"))
        if self.evaluate_response(response):
            device_list=[]
            for device in response['body']['deviceList']:
                device_list.append(device)
            self.device_list=device_list
        else:
            Exception


    def get_temp_hum(self,device_id):
        response=self.query_sensor(device_id)
        if self.evaluate_response(response):
            data=response['body']
            hum=data['humidity']
            temp=data['temperature']
            return temp,hum

        else:
            raise Exception

    def query_sensor(self,device_id):
        header = self.generate_header(self.token, self.secret)
        buffer = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, "https://api.switch-bot.com/v1.1/devices/{}/status".format(device_id))
        c.setopt(pycurl.CAINFO, certifi.where())
        c.setopt(c.HTTPHEADER, header)
        c.setopt(c.WRITEDATA, buffer)
        c.perform()
        c.close()
        response = json.loads(buffer.getvalue().decode("utf-8"))
        return response





    def evaluate_response(self, response):
        try:
            status=response['statusCode']
            if (status==100):
                return True
            elif(status==190):
                return False
            else:
                return False


        except :
            raise TypeError



    def query_all_sensors(self):
        if len(self.device_list)==0:
            self.get_devices()

        for device in self.device_list:
            try:
                response=self.query_sensor(device['deviceId'])
                response['body']['deviceName']=device['deviceName']
                self.sensor_dict[response['body']['deviceId']]=response
            except :
                Exception







