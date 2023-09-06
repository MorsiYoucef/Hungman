import nltk
from nltk.corpus import words
import random

# Download the words corpus if you haven't already
nltk.download('words')

# Get the list of English words
english_words = words.words()

# Create a list of 1000 random words
random_word_list = random.sample(english_words, k=100)
random_word = random.choice(random_word_list)
# Print the list of random words

