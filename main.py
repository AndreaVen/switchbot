import switchbot
from switchbot import Switchbot
from dotenv import load_dotenv
import os

load_dotenv()
device_number=os.environ['device_number']
sw=Switchbot()
sw.get_temp_hum(device_number)



