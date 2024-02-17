import switchbot
from switchbot import *
from dotenv import load_dotenv

load_dotenv()

device_number=os.environ['device_number']
switchbot.get_temp_hum(device_number)



