from nltk.corpus import stopwords
import nltk
from nltk.stem import LancasterStemmer
from nltk.tokenize import word_tokenize


stop_words = set(stopwords.words('english'))

doc_dict = [
    ["d1", "Welcome to hotel heaven such a lovely place"],
    ["d2", "She is buying a stairway to heaven"],
    ["d3", "Don't make it bad"],
    ["d4", "Take me to the heaven"]
]

doc_with_exact_match= []
doc_with_best_match= []
querry = input()
for key, val in doc_dict:
    
    querry1 = word_tokenize(querry)
    word_tokens = word_tokenize(val)

    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    flag = 0
    for word in filtered_sentence:
        
        for w in querry1:
            
            if word.lower() == w.lower():
                flag = 1
                break;
                
    if flag == 1:
        doc_with_best_match.append(key)
    
    exact_match = 1
    for w in querry1:
            flag = 0
            for word in filtered_sentence:
                
                if word.lower() == w.lower():
                    flag = 1
                    
            if flag == 0:
                exact_match = 0
                break
    if exact_match == 1:
        doc_with_best_match.remove(key)
        doc_with_exact_match.append(key)
        
print("Following documents found with the best match for querry", doc_with_best_match)
print("Following documents found with the exact match for querry", doc_with_exact_match)
