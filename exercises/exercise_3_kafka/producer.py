import json
from kafka import KafkaProducer

# Kafka Configuration
KAFKA_BROKER = "localhost:9092"  # Change if your Kafka is running elsewhere
TOPIC = "orders"

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")  # Serialize JSON
)

# Load Orders Data from File
with open("data/orders.json", "r") as file:
    orders_data = json.load(file)

# Send Orders to Kafka Topic
for order in orders_data:
    producer.send(TOPIC, order)  # Send each order as a JSON message
    print(f"Produced Order: {order['order_id']}")

# Close the producer
producer.flush()
producer.close()

