pip install nltk
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """This is a sample sentence,
                showing off the stop words filtration."""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)



from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Sample dataset
dataset = ["The quick brown fox jumps over the lazy dog",
           "Python is a high-level programming language",
           "Data science is an interdisciplinary field"]

stemmer = PorterStemmer()

stemmed_dataset = []
for sentence in dataset:
    words = word_tokenize(sentence)
    stemmed_words = [stemmer.stem(word) for word in words]
    stemmed_sentence = " ".join(stemmed_words)
    stemmed_dataset.append(stemmed_sentence)

# Print the stemmed dataset
print(stemmed_dataset)


