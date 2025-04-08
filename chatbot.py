import pandas as pd
import numpy as np
import nltk
import random

f = open("E:/amogh  visual studio/CHATBOT/chatbot.txt", "r", encoding="utf-8")  # Ensure correct encoding
text = f.read()
f.close()

print(text)  # Print the content of the file
nltk.download('punkt')  # Example: Tokenizer data

text=text.lower()
word_token=nltk.word_tokenize(text)
sent_token=nltk.sent_tokenize(text)

