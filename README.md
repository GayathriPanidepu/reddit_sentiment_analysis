# 📊 Real-Time Reddit Sentiment Analyzer using Kafka and Python

This project performs **real-time sentiment analysis** on Reddit posts using Python, Apache Kafka, and TextBlob. It streams posts from a specific subreddit using Reddit's API, sends them to a Kafka topic, and then a consumer processes and stores the sentiment analysis results in a CSV file.

---

## 📁 Project Structure

```
Real_time_reddit_sentiment/
├── reddit_producer.py         # Streams Reddit posts and sends to Kafka
├── reddit_consumer.py         # Consumes posts and analyzes sentiment
├── sentiment_results.csv      # Output CSV with sentiment results
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Requirements

- Python 3.6 or higher
- Apache Kafka & Zookeeper
- Reddit Developer Account
- Kafka topic: `reddit-stream`

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/reddit-sentiment-analyzer.git
cd reddit-sentiment-analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

---

## 🔐 Reddit API Setup

1. Go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)
2. Click **"Create another app"**
3. Fill the form:
   - **Name**: `SentimentApp`
   - **Type**: `script`
   - **Redirect URI**: `http://localhost`
4. Submit the form and note:
   - `client_id`
   - `client_secret`
   - `username`
   - `password`
5. Add these credentials into `reddit_producer.py` accordingly.

---

## 🚀 Run the Application

### Step 1: Start Zookeeper & Kafka server

In Kafka directory:

```bash
.in\windows\zookeeper-server-start.bat config\zookeeper.properties
.in\windows\kafka-server-start.bat config\server.properties
```

### Step 2: Create Kafka topic

```bash
.in\windows\kafka-topics.bat --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic reddit-stream
```

### Step 3: Start Consumer

```bash
python reddit_consumer.py
```

### Step 4: Start Producer

```bash
python reddit_producer.py
```

---

## 🧠 Sentiment Analysis

- We use **TextBlob** to analyze the polarity of post titles.
  - `polarity > 0` → Positive
  - `polarity < 0` → Negative
  - `polarity == 0` → Neutral

---

## 📄 Output Example (`sentiment_results.csv`)

| title                | url                            | sentiment |
|---------------------|----------------------------------|-----------|
| Python is awesome!  | https://reddit.com/xyz          | Positive  |
| I hate bugs         | https://reddit.com/abc          | Negative  |
| It’s just okay      | https://reddit.com/123          | Neutral   |

---

## 📌 Features

- Real-time Reddit post streaming
- Kafka producer-consumer model
- CSV logging of sentiment results
- Modular, extensible code

---

## 📈 Future Enhancements

- Add timestamps to CSV
- Analyze comments and post bodies (`selftext`)
- Deploy on Docker with Kafka container
- Use more advanced NLP models for sentiment (e.g. Vader, BERT)

---

## 👩‍💻 Author

**Princess Princess**  
> Real-time data enthusiast | Python & Kafka beginner | Loves building cool data-driven apps 💻✨

---

## 📃 License

MIT License

## Outputs 

**Producer.py**
![image](https://github.com/user-attachments/assets/bb577817-673b-4808-9915-26e1c7573802)

**Consumer.py**
![image](https://github.com/user-attachments/assets/e91fb111-c951-4426-877e-2d615a6783c2)

