from kafka import KafkaConsumer
from kafka import TopicPartition
import logging
#logging.basicConfig(level=logging.DEBUG)

consumer = KafkaConsumer("launchpad.web.logs", bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
for m in consumer:
    print("Message {msg}".format(msg=m))
    if m is not None:
        print(m)
