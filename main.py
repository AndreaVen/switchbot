import time
from switchbot import Switchbot
from data_writer import Data_writer
sw=Switchbot()
writer = Data_writer()
i=0;
while True:
    sw.query_all_sensors()
    data=sw.sensor_dict
    writer.save_all(data)
    i=i+1
    time.sleep(120)






