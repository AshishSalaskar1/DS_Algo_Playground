import json
from kafka import KafkaConsumer

ORDER_CONFIRMED_TOPIC = "order_confirmed"
consumer = KafkaConsumer(
    ORDER_CONFIRMED_TOPIC,
    bootstrap_servers="localhost:29092"
)

total_revenue = 0
total_customers_prcessed = set()

print(f"Started listening to kafka topic {ORDER_CONFIRMED_TOPIC}....")
while True:
    for message in consumer:
        read_msg = json.loads(message.value.decode())

        total_revenue += float(read_msg['total_cost'])
        total_customers_prcessed.add(read_msg['customer_mail'])

        print(
            f"Updated Stats: \nRevenue: {total_revenue}, total_customers: {len(total_customers_prcessed)}")
