from kafka import KafkaConsumer
from json import loads,dumps
import json
import mysql.connector
import pymysql
#from pymysql import escape_string

mydb = mysql.connector.connect(
  host="localhost",
  user="demo_user",
  password="demo_user",
  database="demodb"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS demo_table (ts VARCHAR(255), log_level VARCHAR(255), city VARCHAR(255), message VARCHAR(255))")

consumer = KafkaConsumer(
    'git-demo-topic',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for record in consumer:
    record = record.value
    recordj = json.dumps(record)
    transaction_sql = (
        "insert into demo_table"
        "(ts,log_level,city,message)"
        "values (%(ts)s, %(city)s, %(log_level)s, %(message)s)")
    print(transaction_sql)
    mycursor.execute(transaction_sql, record)
    mydb.commit()
