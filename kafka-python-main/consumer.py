from kafka import KafkaConsumer
import json
import sys
import pickle

'''my_serv = input('enter server with port => ')
Topic = input('Enter topic name : ')'''

my_serv = 'localhost:9092'
Topic = 'topic1'

if __name__ == "__main__":
    print('kafka consumer applicaltion started...')
    try :
        consumer = KafkaConsumer(
            Topic,
            bootstrap_servers = my_serv,
            enable_auto_commit = True,
            auto_offset_reset = 'latest')

        
        for msg in consumer :
            print(json.dumps(pickle.loads(msg.value), indent=2))
        
        '''for msg in consumer :
            print(json.dumps(eval(msg.value.decode('utf-8')))) '''

        '''for msg in consumer:
            print('message :', msg.value.decode('utf-8')) '''
            

    except :
        print('failed to print messages')
        print('[!] error :',sys.exc_info()[1])
