## **What is Apache Kafka?**
Apache Kafka is an open-source software that helps handle and process large amounts of data in real-time. Think of it like a messaging system that allows different applications to send, receive, and store data efficiently. It is widely used for streaming data, logs, and event-driven applications.


## **How Does Kafka Work?**

Kafka works like a message broker, meaning it sits in the middle of different systems and helps them talk to each other. It consists of:

- **Producers** – These send data (messages) to Kafka. Example: A website sending user activity logs.
- **Topics** – Think of these as categories where messages are stored. Example: A topic for “user_logins.”
- **Brokers** – Kafka servers that store and manage the messages.
- **Consumers** – Applications that read data from Kafka. Example: An analytics system that processes login data.
- **ZooKeeper** – A helper tool that keeps Kafka running smoothly.

---

## **Theory Questions**

### a) What is Apache Kafka, and how does it work?
Apache Kafka is a distributed event streaming platform designed to handle large volumes of real-time data. It works by using producers to send messages (events) to topics, which are stored in partitions within a Kafka broker. Consumers read messages from these topics. Kafka provides high availability, fault tolerance, and scalability by distributing data across multiple brokers in a cluster.

### b) What is a Kafka topic?
A Kafka topic is a logical channel where messages (events) are stored and categorized. Producers send messages to a topic, and consumers subscribe to it to read messages. Topics are divided into partitions, which help distribute data and parallelize processing.

### c) How does the Kafka broker, cluster, and partitions relate to each other?
- **Kafka Broker**: A server that stores data and serves client requests (producers and consumers). Each broker in a cluster holds partitions of topics.
- **Kafka Cluster**: A group of brokers working together to distribute and manage topics.
- **Partition**: A subset of a topic stored on a broker, allowing Kafka to scale horizontally and process messages in parallel.

### d) What are Kafka producers and consumers and the publish-subscribe model?
- **Kafka Producer**: An application that sends messages (events) to Kafka topics.
- **Kafka Consumer**: An application that reads messages from Kafka topics.
- **Publish-Subscribe Model**: A messaging pattern where multiple consumers can subscribe to a topic and receive messages published by producers. This allows real-time data distribution to multiple systems.

### e) How does Kafka guarantee message ordering?
Kafka guarantees message ordering **within a partition**. Each partition maintains a strict order, and messages are assigned an incremental offset. If a producer sends messages with the same key, they go to the same partition, ensuring order. However, across partitions, Kafka does not guarantee ordering.

### f) What is key-based partitioning in Kafka?
Key-based partitioning is a method where a message is assigned a **key**, and Kafka uses this key to determine which partition the message should be stored in. This ensures that all messages with the same key go to the same partition, preserving order for a specific entity (e.g., all events related to a user go to the same partition).

### g) How do you set up Kafka locally?
To set up Kafka locally, follow these steps:
1. **Download Kafka**:  
   - Get the latest version from the [Apache Kafka website](https://kafka.apache.org/downloads).

2. **Start Zookeeper** (Kafka requires Zookeeper to manage brokers):  
   ```sh
   bin/zookeeper-server-start.sh config/zookeeper.properties

3. Start Kafka Broker:
    bin/kafka-server-start.sh config/server.properties

4. Create a Topic:
    bin/kafka-topics.sh --create --topic test-topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

5. Start a Producer (to send messages):
    bin/kafka-console-producer.sh --topic test-topic --bootstrap-server localhost:9092

6. Start a Consumer (to read messages):
    bin/kafka-console-consumer.sh --topic test-topic --from-beginning --bootstrap-server localhost:9092

7. Verify Kafka is Running:
    Send a message from the producer, and it should appear in the consumer.