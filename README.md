# kafka-producer_backend
This is a kafka-python producer, just to sent formated data to kafka consumer

# Setting

We should have topic name, in our case it is quick-events. 

And then we just have to add events to that topic using Python-kafka Producer. The events can be messages to be stored in kafka consumer.

The message would be the Produce JSON messages. This format is easy to handle with any type of data.

```
# options:
#     -bootstrap_servers : the producer should contact 
#     to bootstrap initial cluster metadata. This does not have to be the full node list. It just needs to have at 
#     least one broker that will respond to a Metadata API Request. Default port is 9092. 
#     -value_serializer : to convert user-supplied message values to bytes.


producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
producer.send('quick-events', {'sensor': 25})
producer.flush()
```
