import unittest

from data_writer import Data_writer
class Test_data_writer(unittest.TestCase):


    def test_constructor(self):
        data_writer=Data_writer()

    def test_writer(self):
        data_writer=Data_writer()
        data_writer.write_data(10.5,2,'test','000')

    def test_writer_invalid_data(self):
        data_writer = Data_writer()
        with  self.assertRaises(Exception):
            data_writer.write_data(10.5,2,'test','')
            data_writer.write_data(10.5,2,'test',)



    def test_is_connected(self):
        data_writer=Data_writer()
        self.assertTrue(data_writer.is_connected())
        
        
    def test_save_all(self):
        data_writer=Data_writer()
        self.assertTrue(data_writer.save_all({}))









