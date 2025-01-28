from pathlib import Path  # Path is used to create and manipulate file and directory paths in an OS-independent way.
import json  # json allows working with JSON data, including reading, writing, and parsing JSON files.
from pprint import pprint  # pprint provides a more readable (formatted) output for complex data structures like dictionaries.
from quixstreams import Application  # Application is part of the Quix Streams library, used to interact with Kafka streams for producing and consuming messages.

# Define the path to the "data" folder by navigating up one directory from the script's current location
data_path = Path(__file__).parents[1] / "data"
# Print the resolved path to the "data" folder to ensure it's correctly located
print(data_path)

# Open the "jokes.json" file located in the "data" folder in read mode
with open(data_path / "jokes.json", "r") as file:
    # Load and parse the JSON file content into a Python dictionary
    jokes = json.load(file)

# Pretty-print the jokes dictionary for easier reading
pprint(jokes)

# Initialize a Quix Application to connect to a Kafka broker at localhost:9092, using the consumer group "text-splitter"
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

# Create or connect to a Kafka topic named "jokes", with JSON data as its value serializer
jokes_topic = app.topic(name="jokes", value_serializer="json")
#print(jokes_topic)

def main():  # Define the main function, which acts as the entry point for this part of the program.
    with app.get_producer() as producer:  # Get a Kafka producer from the `app` object and use it within a context manager.
        # print(producer)  # (Optional) Uncomment this line to inspect the producer object.

        for joke in jokes:  # Iterate through the list of jokes loaded from the JSON file.
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)  
            # Serialize the joke into a format compatible with the Kafka topic.
            # `key` is the unique joke ID, and `value` is the full joke data.

            # Print the key and value of the serialized message for debugging or confirmation.
            print(f"Produces message: key = {kafka_msg.key}, value = {kafka_msg.value}")

            producer.produce(
                topic="jokes",  # Specify the Kafka topic name where the message will be sent.
                key=str(kafka_msg.key),  # Use the serialized key (converted to a string).
                value=kafka_msg.value  # Use the serialized value (the joke).
            )  # Send the message to the Kafka topic.



# run this code only when executing and not when importing this module
if __name__=="__main__":
    #pprint(jokes)
    main()
