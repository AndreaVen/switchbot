import switchbot
from switchbot import Switchbot
from dotenv import load_dotenv
import os

load_dotenv()
device_number=os.environ['device_number']
sw=Switchbot()
temp,hum=sw.get_temp_hum(device_number)
sw.query_all_sensors()
data=sw.sensor_dict



