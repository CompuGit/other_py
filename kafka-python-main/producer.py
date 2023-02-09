from kafka import KafkaProducer
import json
import pickle

'''KAFKA_SERVER = input('enter server with port => ')
Topic = input('Enter Topic name : ')'''

KAFKA_SERVER = 'localhost:9092'
Topic = 'topic1'

producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

data = json.load(open('./sample.json'))
p = pickle.dumps(data)
producer.send(Topic, p)

'''
data = json.load(open('./sample.json'))
producer.send(Topic, bytes(str(data), 'utf-8'))
'''

'''while (msg:=input().lower())!='exit':
    producer.send(Topic, bytes(msg, 'utf-8'))'''

producer.flush()
