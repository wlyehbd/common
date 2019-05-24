"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/2/22
@Desc    :

"""
import json
from kafka import KafkaConsumer

server_list = ["60.205.137.135:9092", "101.201.28.48:9092", "101.201.213.132:9092"]
# server_list = ["10.24.202.63:9092", "10.24.200.54:9092", "10.24.200.23:9092"]

consumer = KafkaConsumer('spider_beijing-beike-complex_details', group_id='complex_etl',
                         bootstrap_servers=server_list, auto_offset_reset='earliest')

if __name__ == '__main__':
    for message in consumer:
        print(message.offset)
        info = json.loads(message.value)
        print(info)
