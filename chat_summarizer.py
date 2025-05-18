import os
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import TreebankWordTokenizer  # Changed here
import string

def parse_chat_log(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    user_msgs, ai_msgs = [], []
    for line in lines:
        if line.startswith("User:"):
            user_msgs.append(line[len("User:"):].strip())
        elif line.startswith("AI:"):
            ai_msgs.append(line[len("AI:"):].strip())

    return user_msgs, ai_msgs

def count_messages(user_msgs, ai_msgs):
    return len(user_msgs) + len(ai_msgs), len(user_msgs), len(ai_msgs)

def extract_keywords(messages, top_n=5):
    stop_words = set(stopwords.words('english'))
    tokenizer = TreebankWordTokenizer()  # Updated tokenizer
    all_words = tokenizer.tokenize(" ".join(messages).lower())
    filtered_words = [w for w in all_words if w.isalnum() and w not in stop_words]
    return [word for word, _ in Counter(filtered_words).most_common(top_n)]

def summarize_chat(file_path):
    user_msgs, ai_msgs = parse_chat_log(file_path)
    total, user_count, ai_count = count_messages(user_msgs, ai_msgs)
    all_msgs = user_msgs + ai_msgs
    keywords = extract_keywords(all_msgs)

    print("Summary:")
    print(f"- The conversation had {total} exchanges.")
    print(f"- User sent {user_count} messages; AI responded with {ai_count}.")
    print(f"- Most common keywords: {', '.join(keywords)}")

if __name__ == "__main__":
    chat_file = "sample_chat_logs/chat.txt"
    summarize_chat(chat_file)
