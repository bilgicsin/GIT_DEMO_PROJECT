from faker import Faker
from faker.providers import DynamicProvider
from datetime import datetime
import json
from kafka import KafkaProducer
from time import sleep
from json import dumps

NumberOfRecordsPerSecond = 100
producer = None
while producer is None:
    try:
        producer = KafkaProducer(bootstrap_servers=['kafka:9094'],
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'))
    except:
         print('Kafka is not ready yet!')
         sleep(10)
         pass


fake = Faker('en_GB')

log_level_provider = DynamicProvider(
     provider_name="log_level",
     elements=["INFO", "DEBUG", "ERROR", "WARN", "TRACE", "FATAL"],
)
fake.add_provider(log_level_provider)

while True:
    for i in range(NumberOfRecordsPerSecond):
      city= fake.city() #city ve detail alanlarında aynı random şehir isminin gelmesi için eklendi.
      record= {
              'ts':   datetime.now().isoformat(sep=' ', timespec='milliseconds'),
              'log_level':fake.log_level(),
              'city':city,
              'detail':'Hello-from-' + city
              }

      producer.send('git-demo-topic', value=record)
      print(record)
      producer.flush()
    sleep(1)