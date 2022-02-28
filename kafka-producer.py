#!/usr/bin/env python
# coding: utf-8


from kafka import KafkaProducer
from kafka.errors import KafkaError
import msgpack
import json



# create a KafkaProducer
#producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    log.error('I am an errback', exc_info=excp)
    # handle exception


# it worrked as well on kafka consumer
if __name__ == "__main__":
	print("sensor sending data")
	#producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
	producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
	producer.send('quick-events', {'sensor_2': 25}).add_callback(on_send_success).add_errback(on_send_error)
	producer.flush()
	
