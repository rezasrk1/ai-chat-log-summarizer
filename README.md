
# AI Chat Log Summarizer

This Python tool reads chat logs between a user and an AI, parses the conversation, and generates a summary including message counts and frequently used keywords.

---

## Features

- Parses chat logs separating User and AI messages  
- Counts total messages and messages by speaker  
- Extracts top 5 keywords excluding common stop words  
- Prints a concise summary of the conversation  

---

## Requirements

- Python 3.x  
- nltk library  

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/rezasrk1/ai-chat-log-summarizer.git
cd ai-chat-log-summarizer
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download necessary NLTK data (run once):

```python
import nltk
nltk.download('stopwords')
```

---

## Usage

Make sure you have a chat log file at `sample_chat_logs/chat.txt` formatted like:

```
User: Hello!
AI: Hi! How can I assist you today?
User: Can you explain what machine learning is?
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.
```

Run the summarizer script:

```bash
python chat_summarizer.py
```

---

## Sample Output

```
Summary:
- The conversation had 6 exchanges.
- User sent 3 messages; AI responded with 2.
- Most common keywords:  python, use, hi, tell, sure
```
![Screenshot (3)](https://github.com/user-attachments/assets/258f598c-4497-41e5-a705-2c8710ed4630)

---


