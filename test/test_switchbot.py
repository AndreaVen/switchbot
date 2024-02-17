import unittest
from unittest.mock import patch
from switchbot import Switchbot
from dotenv import load_dotenv

class switchbot_test(unittest.TestCase):


    def setUp(self):
        self.sw=Switchbot()

    def tearDown(self):
        pass

    def test_generic_error(self):
       with  self.assertRaises(TypeError):
           self.sf.evaluete_response("42")

    @patch('switchbot.Switchbot.get_temp_hum')
    def test_temperature(self,temp_hum):
        temp_hum.response['statusCode'] = 100
        self.assertTrue(self.sw.get_temp_hum('42'),True)








if __name__ == '__main__':
    unittest.main()