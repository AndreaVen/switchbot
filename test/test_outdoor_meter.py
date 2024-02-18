
import time
import unittest
from outdoor_meter import Outdoor_meter
class Test_outdoor_meter(unittest.TestCase):


    def test_constructor_class(self):
        var=Outdoor_meter()
        hum=var.humidity
        temp=var.temperature
        timestamp=var.timestamp
        self.assertEqual(hum,None)
        self.assertEqual(temp,None)
        self.assertEqual(timestamp,None)

        t = time.time()
        var=Outdoor_meter(22,10,t)
        hum = var.humidity
        temp = var.temperature
        timestamp = var.timestamp
        self.assertEqual(hum,10)
        self.assertEqual(temp,22)
        self.assertEqual(timestamp,t)


    def test_valid_values(self):
        from datetime import datetime
        t=time.time()
        var=Outdoor_meter(22.4,10,t)
        var.validate_input()












