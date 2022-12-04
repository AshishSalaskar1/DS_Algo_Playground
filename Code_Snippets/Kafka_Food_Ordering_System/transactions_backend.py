import json

from kafka import KafkaProducer, KafkaConsumer

ORDER_KAFKA_TOPIC =  "order_details"
ORDER_CONFIRMED_TOPIC = "order_confirmed"


# Since consumer keeps on listening on start, you need to give topic to listen to
consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
    bootstrap_servers="localhost:29092"
)

# Topic is not passeed here, its passed when writing data to a specific topic
producer = KafkaProducer(
    bootstrap_servers="localhost:29092"
)


print(f"Started listening to kafka topic {ORDER_KAFKA_TOPIC}....")
while True:
    for message in consumer:
        print("Ongoing transaction.....")
        read_msg = json.loads(message.value.decode())
        print(read_msg)

        write_data = {
            "customer_id": read_msg["user_id"],
            "customer_mail": f"{read_msg['user_id']}@somemail.com",
            "total_cost": read_msg["total_cost"]
        }

        print(f"Transaction {read_msg['order_id']} processed....")
        producer.send(
        topic=ORDER_CONFIRMED_TOPIC,
        value=json.dumps(write_data).encode("utf-8")
    )