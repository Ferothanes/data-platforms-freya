from quixstreams import Application

#bygger application
app = Application(
    broker_address="localhost:9092",# The address of the Kafka server (where it’s running)
    consumer_group="text_splitter", # The name of the group that will consume messages from Kafka
    auto_offset_reset="earliest"       # How to handle reading messages (e.g., "reset" means to start reading from the beginning)
)

#deserializera till binary för att kunna skicka
jokes_topic = app.topic(name="jokes", value_deserializer="json")

sdf = app.dataframe(topic=jokes_topic) #SDF -Streaming dataframe
print(sdf) #(sdf represents a real-time stream of data from Kafka)

sdf.update(lambda message: print(f"Input message: {message}")) #motsvarar nedan (undviker med lambda)

            #def print_message(message):
                #print(message)
            #sdf.update(print_message)

def split_words(message):
    return [word for word in message["joke_text"].split()]

sdf = sdf.apply(split_words, expand =True)
sdf.update(lambda words: print(f"Output: {words}"))

sdf = sdf.apply()

if __name__== '__main__':
    app.run()

