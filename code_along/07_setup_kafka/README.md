## Vad är Apache Kafka?

Apache Kafka är en **öppen källkodsplattform** som används för att hantera och bearbeta **real-time data streams**. Det används ofta för att samla in, överföra, lagra och analysera stora mängder data från olika källor i realtid.

(Används i många branscher där snabb och skalbar datahantering är kritisk, som finans, e-handel, IoT och logghantering.)


### Grundläggande funktioner
- **Meddelandehantering (Message Broker):** Kafka fungerar som en "message broker" som tar emot data (meddelanden) från olika källor och distribuerar den till konsumenter (t.ex. applikationer).

**Distribuerad och skalbar:** Kafka är byggt för att fungera i kluster, vilket innebär att det kan hantera stora datamängder och är skalbart över flera servrar.

**Hög genomströmning och låg latens:** Kafka är optimerat för att hantera miljontals meddelanden per sekund med minimal fördröjning.

**Lagring av data:** Kafka lagrar inkommande data på disk, vilket gör att konsumenter kan läsa data när det passar dem, utan att tappa några meddelanden.

---
### Hur fungerar Apache Kafka?

**Topics:**

Topics är som "postlådor" där **events** sorteras och kategoriseras.
Varje topic har ett namn, t.ex. user_activity eller sensor_data, så att konsumenter (de som hämtar data) vet var de ska leta.
Tänk dig att varje topic är en specifik hylla i postkontoret där posten för olika kategorier sparas.
**Exempel**:
- sensor_data
- user_logs

**Producenter och konsumenter:**
- Producers send data to Kafka. En producer är en enhet (t.ex. en app eller en tjänst) som skickar data till Kafka. Tänk på en producer som någon som lägger brev (meddelanden) i en postlåda (Kafka topic).

- Consumers read data from Kafka. Consumer är en enhet som läser data från Kafka. Tänk på en consumer som en person som hämtar och läser breven från postlådan (topic).

**Broker**: Är en server med massa topics 

- En broker tar emot events från producenter(producer) och placerar dem i rätt topic (den rätta "postlådan").
- När en konsumenter(consumer) vill hämta data, hjälper brokern att leverera rätt meddelanden från rätt topic.
- Om det finns flera brokers i ett kluster (flera Kafka-servrar som samarbetar), så delar de upp ansvaret för att lagra och skicka data.
- I Docker används brokers ofta i system som Apache Kafka för att hantera och distribuera events.

**Events (händelser):**

- Ett event är en bit data eller information som beskriver att något har hänt, till exempel en ny order i en webbutik eller att en sensor registrerat en temperatur ("användare klickade på en knapp" eller "temperaturen är 25°C")
- I ett eventdrivet system skickar producenter (den som genererar eventet) detta vidare via brokern, och konsumenter tar emot och bearbetar eventet.
- Dessa events skickas av producenter (t.ex. en app, en sensor, eller en databas) till Kafka.

**Partitioner**:
- Varje topic är uppdelat i partitioner, vilket möjliggör parallellism och hög prestanda. Varje partition lagrar en sekventiell logg av meddelanden.

**Konsumentgrupper**:
- Flera konsumenter kan läsa från samma topic i grupper, vilket möjliggör skalbar bearbetning av data.

---
![alt text](07_setup_kafka/images/image.png)




