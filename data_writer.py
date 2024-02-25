import mysql.connector
from datetime import datetime
from dotenv import load_dotenv
import os


load_dotenv()
psw=os.environ['db_psw']
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=psw,
  database="switchbot"
)




mycursor = mydb.cursor()

sql = "INSERT INTO sensor_data (humidity, temperature,timestamp,id_timestamp,id,name,date) VALUES (%s, %s,%s, %s,%s, %s,%s)"

# current date and time
now = datetime.now()
val = (0,0.0,now,'id univoco4','id sensore','nome sensore',now)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


