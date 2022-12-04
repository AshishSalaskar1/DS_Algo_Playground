import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_TOPIC = "order_confirmed"
consumer = KafkaConsumer(
    ORDER_CONFIRMED_TOPIC,
    bootstrap_servers="localhost:29092"
)

print(f"Started listening to kafka topic {ORDER_CONFIRMED_TOPIC}....")
while True:
    for message in consumer:
        read_msg = json.loads(message.value.decode())

        print(f"Sending mail to user {read_msg['customer_id']} having email {read_msg['customer_mail']}....")
        print("Sent email.....")
