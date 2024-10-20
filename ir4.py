import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

spam_df = pd.read_csv("spam.csv")

spam_df

spam_df.groupby('Category').describe()

spam_df['spam'] = spam_df['Category'].apply(lambda x: 1 if x == 'spam' else 0)

spam_df

x_train, x_test, y_train, y_test = train_test_split(spam_df.Message, spam_df.spam, test_size = 0.25)

x_train

cv = CountVectorizer()
x_train_count = cv.fit_transform(x_train.values)

x_train_count

model = MultinomialNB()
model.fit(x_train_count, y_train)

email_ham = ["Hey how are you?"]
email_ham_count = cv.transform(email_ham)
model.predict(email_ham_count)

email_spam = ["gift "]
email_spam_count = cv.transform(email_spam)
model.predict(email_spam_count)

x_test_count = cv.transform(x_test)
model.score(x_test_count, y_test)
