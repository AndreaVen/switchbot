import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os


class Data_writer:
  def __init__(self):
    self.connect()



  def write_data(self,temperature,humidity,id):
    if (id==None or id==''):
      raise Exception
    else:
      sql = "INSERT INTO switchbot.sensor_values (temperature,humidity,sensor_id,timestamp) VALUES (%s, %s,%s,%s)"
      # current date and time
      now = datetime.now()
      timestamp_id = str(now) + '-' + id
      val = (temperature,humidity,id,now)
      self.mycursor.execute(sql, val)
      self.mydb.commit()
      print( "record inserted.")



  def save_all(self,sensor_dict):
    for key in sensor_dict:
      record=sensor_dict[key]
      id=record['body']['deviceId']
      type=record['body']['deviceType']
      if (type=='WoIOSensor'):
        humidity = record['body']['humidity']
        temperature = record['body']['temperature']
        self.write_data(temperature,humidity,id)
    return True



  def connect(self):
    load_dotenv()
    psw = os.environ['db_psw']
    self.mydb = mysql.connector.connect(
      host="192.168.1.215",
      user="root",
      password=psw,
      database="switchbot"
    )
    self.mycursor = self.mydb.cursor()


  def is_connected(self):
    return self.mydb.is_connected()


  def reconnect(self):
    if  self.is_connected()==False:
      self.connect()


  def disconnect(self):
    self.mydb.close()
