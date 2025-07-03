from kafka import KafkaConsumer
import json
from textblob import TextBlob
import csv
import os

# Kafka Consumer Setup
consumer = KafkaConsumer(
    'reddit-stream',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # Read from beginning
    enable_auto_commit=True,
    group_id='reddit-consumer-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# CSV File Setup
csv_file = 'sentiment_results.csv'
csv_columns = ['title', 'url', 'sentiment']

# Create CSV and write header if not exists
if not os.path.isfile(csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writeheader()

# Sentiment Analysis + Save to CSV
print("🟢 Consumer started. Listening to Kafka topic...")
for message in consumer:
    post = message.value
    title = post.get('title', '')
    url = post.get('url', '')
    blob = TextBlob(title)
    polarity = blob.sentiment.polarity
    sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'

    print(f"📥 Received: {title} --> Sentiment: {sentiment}")

    # Save to CSV
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=csv_columns)
        writer.writerow({
            'title': title,
            'url': url,
            'sentiment': sentiment
        })
