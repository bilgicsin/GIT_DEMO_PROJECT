from kafka import KafkaConsumer
from json import loads,dumps
import json
import mysql.connector
import pymysql
#from pymysql import escape_string
from time import sleep

mydb = None
while mydb is None:
    try:
        mydb = mysql.connector.connect(
        host="mysqldb",
        user="demo_user",
        password="demo_user",
        database="demodb"
)
    except:
         print('demodb database is not ready yet!')
         sleep(10)
         pass

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS demo_table (ts VARCHAR(255), log_level VARCHAR(255), city VARCHAR(255), detail VARCHAR(255))")

consumer = KafkaConsumer(
    'git-demo-topic',
     bootstrap_servers=['kafka:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     value_deserializer=lambda x: loads(x.decode('utf-8')))

for record in consumer:
    record = record.value
    recordj = json.dumps(record)
    transaction_sql = (
        "insert into demo_table"
        "(ts,log_level,city,detail)"
        "values (%(ts)s, %(city)s, %(log_level)s, %(detail)s)")
    mycursor.execute(transaction_sql, record)
    mydb.commit()
