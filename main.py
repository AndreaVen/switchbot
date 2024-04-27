import time
from switchbot import Switchbot
from data_writer import Data_writer
import logging
sw=Switchbot()
writer = Data_writer()
i=0;
while True:
    try:
        sw.query_all_sensors()
        data=sw.sensor_dict
        writer.save_all(data)
        i=i+1
    except Exception :
        logging.error("Unexprected error")
    time.sleep(120)






