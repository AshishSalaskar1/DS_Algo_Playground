import json
import time
from kafka import KafkaProducer, producer

ORDER_KAFKA_TOPICS =  "order_details"
ORDER_LIMIT = 65

# initialize KafkaProducer object
producer = KafkaProducer(bootstrap_servers="localhost:29092")

print("Start generating orders..")
print("Generate orders every 5 seconds")



for i in range(ORDER_LIMIT):
    data = {
        "order_id": i,
        "user_id": f"tim{i}",
        "total_cost": i*2,
        "items": "burger, fries"
    }

    producer.send(
        topic=ORDER_KAFKA_TOPICS,
        value=json.dumps(data).encode("utf-8")
    )

    print(f"Sent order {i}......")
    time.sleep(1)


