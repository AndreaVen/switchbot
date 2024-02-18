import unittest
from unittest.mock import patch
from switchbot import Switchbot
from dotenv import load_dotenv

class switchbot_test(unittest.TestCase):


    def setUp(self):
        self.sw=Switchbot()

    def tearDown(self):
        pass

    def test_evaluate_response(self):
       with  self.assertRaises(TypeError):
           self.sw.evaluate_response("42")
       self.assertTrue(self.sw.evaluate_response({"statusCode":100}),True)





    @patch('switchbot.Switchbot.get_temp_hum')
    def test_temperature_hum_wrong_type(self,temp_hum):
        temp_hum.response['statusCode'] = 100
        self.assertTrue(self.sw.get_temp_hum('42'),True)

    def test_temperature_hum(self):
        import os
        load_dotenv()
        device_number = os.environ['device_number']
        temp,hum=self.sw.get_temp_hum(device_number)
        self.assertFalse(temp==None)
        self.assertFalse(hum==None)
        self.assertTrue(type(temp)==float)
        self.assertTrue(type(hum)==int)









    def test_set_correct_token_and_secret(self):
        load_dotenv()
        import os
        token = os.environ['token']
        secret = os.environ['secret_key']
        self.sw.set_token_and_secret()
        self.assertEqual(token,self.sw.token)
        self.assertEqual(secret,self.sw.secret)



    def test_get_device(self):
        empty_list=[]
        self.assertEqual(self.sw.get_devices(),None)
        self.sw.get_devices()
        devices=self.sw.device_list
        self.assertTrue(len(devices)>0)

    def test_query_all_sensors(self):
        self.sw.query_all_sensors()
        device_dict=self.sw.sensor_dict
        self.assertTrue(device_dict!=None)


















if __name__ == '__main__':
    unittest.main()