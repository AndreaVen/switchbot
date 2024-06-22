import time
from switchbot import Switchbot
from data_writer import Data_writer
import logging
logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('log.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
sw=Switchbot()
writer = Data_writer()
logger.addHandler(file_handler)

i=0;
while True:
    logger.info("start application")

    try:
        sw.query_all_sensors()
        data=sw.sensor_dict
        writer.save_all(data)
        i=i+1
    except Exception :
        logger.error("Unexprected error")
    time.sleep(120)






