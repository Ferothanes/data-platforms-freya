from pathlib import Path  # Path is used to create & manipulate file & directory paths
import json  # json allows working with JSON data, including reading, writing, and parsing JSON files.
from pprint import pprint  # pprint provides a more readable (formatted) output.
from quixstreams import Application  # Application(from QuixStreams library) used to interact with Kafka streams for producing and consuming messages.

# Get the absolute path to the "data" folder. .parents[1](one level up from this scr & back into "data")
data_path = Path(__file__).parents[1] / "data"
# Print resolved path to the "data" folder to ensure it's correctly located
print(data_path)

# Open the "jokes.json" file and load its contents into a Python dictionary(in "r" read mode)
with open(data_path / "jokes.json", "r") as file:
    # Load and parse the JSON file content into a Python dictionary
    jokes = json.load(file)

pprint(jokes) # Display the loaded jokes in a readable format(pretty-print)

# Initialize a Quix Application to connect to a Kafka broker at localhost:9092
# summerized: Set up a connection to Kafka (message broker) running on localhost
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

# Create or connect to a Kafka topic named "jokes", that stores data in JSON format
jokes_topic = app.topic(name="jokes", value_serializer="json")


# PRODUCER:-------------------------------SERIALIZE KEY & VALUE

def main():  # Define the main function, which acts as the entry point for this part of the program.
    with app.get_producer() as producer: # Get a Kafka producer (used to send messages)

        for joke in jokes: # For every joke in jokes - follow requirments 
            kafka_msg = jokes_topic.serialize(key=joke["joke_id"], value=joke)  
            # Prepare the message for Kafka (assign each joke an ID as a key)
            # (Serialize the joke into a format compatible with the Kafka topic. # `key` is the unique joke ID, and `value` is the full joke data.)

            # Print the key and value of the serialized message for debugging or confirmation.
            print(f"Produce event with key = {kafka_msg.key}, value = {kafka_msg.value}")

            # Sends the message to the Kafka topic "jokes"
            producer.produce(
                topic=jokes_topic.name,  # Specify the Kafka topic name where the message will be sent.
                key=str(kafka_msg.key), # Convert the joke ID to a string
                value=kafka_msg.value  # Use the serialized value (the joke).
            )  # Send the joke data


# Run the main function only if this script is executed directly
if __name__=="__main__":
    main()
