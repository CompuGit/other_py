from kafka import KafkaClient

#serv = input('enter server with port => ')
serv = 'localhost:9092'

client = KafkaClient(bootstrap_servers=serv)

future = client.cluster.request_update()
client.poll(future=future)

metadata = client.cluster
print(metadata.brokers())
print(metadata.topics())
