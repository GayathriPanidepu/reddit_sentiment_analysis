import praw
from kafka import KafkaProducer
import json
import time

# Kafka Producer Setup
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Reddit API credentials (replace with your real ones)
reddit = praw.Reddit(
    client_id='phGviyifOd5iFpLaezrv-A',
    client_secret='bkGcEsIkPQi5sfmnjeNHOgLe1R03vA',
    user_agent="windows:SentimentApp:v1.0 (by u/Impossible_Guard2188)",
    username='Impossible_Guard2188',
    password='12qwaszx-@'
)

def stream_reddit_posts(subreddit_name):
    subreddit = reddit.subreddit(subreddit_name)
    print(f"⏳ Listening to r/{subreddit_name}...")
    for submission in subreddit.stream.submissions(skip_existing=True):
        data = {
            'title': submission.title,
            'selftext': submission.selftext,
            'url': submission.url
        }
        print(f"✅ Sending post to Kafka: {submission.title}")
        try:
            producer.send('reddit-stream', value=data)
            producer.flush()
        except Exception as e:
            print(f"❌ Error sending to Kafka: {e}")
        time.sleep(1)

if __name__ == "__main__":
    stream_reddit_posts('news')  # Use a busy subreddit
