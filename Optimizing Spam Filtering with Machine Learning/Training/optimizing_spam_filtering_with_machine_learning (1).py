# -*- coding: utf-8 -*-
"""Optimizing Spam Filtering with Machine Learning

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Pvv-KcVS3TrZP9eGG77jpnXaLpLbnk9a

Importing the libraries
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import  CountVectorizer
from sklearn.tree import DecisionTreeClassifier
import imblearn
from imblearn.over_sampling import SMOTE
import re
import pickle
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

"""Read the Dataset"""

import csv
from scipy.sparse import data
data = pd.read_csv(r'/content/sample_data/mnist_test.csv')
data

df= pd.read_csv("spam.csv",encoding="latin")
df.head()

"""Handling missing values"""

df.info()

df.isna().sum()

df.rename({"v1":"label","v2":"text"},inplace=True,axis=1)

df

df.tail()

""" Handling Categorical Values"""

le = LabelEncoder()
df['label'] = le.fit_transform(df['label'])

x = df['text']
y = df['label']

vectorizer = CountVectorizer()

x_transformed = vectorizer.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x_transformed, y, test_size=0.2, random_state=42)

"""Handling Imbalance Data"""

from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test = train_test_split(x,y,test_size = 0.20,random_state = 0)

print("Before oversampling, count of label '1': {}".format(sum(y_train == 1)))
print("Before oversampling, count of label '0': {}".format(sum(y_train == 0)))

smote = SMOTE(random_state=42)

X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

print("After OverSampling, count of label '1': {}" .format(sum(y_resampled == 1 )))
print("After OverSampling, count of label '0': {}" .format(sum(y_resampled == 0 )))

"""Cleaning the text data"""

nltk.download("stopwords")

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

import re
corpus = []
length = len(df)

for i in range(0,length):
    text = re.sub("[^a-zA-Z0-9]"," ",df["text"][i]) 
    text = text.lower()
    text = text.split()
    pe = PorterStemmer()
    stopword = stopwords.words("english")
    text = [pe.stem(word) for word in text if not word in set(stopword)]
    text =" ".join(text)
    corpus.append(text)

corpus

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=35000)
X = cv.fit_transform(corpus).toarray()

import pickle
pickle.dump(cv, open('cv1.pk1','wb'))

"""Descriptive Statistical"""

df.describe()

df.shape

"""Univariate Analysis"""

df["label"].value_counts().plot(kind="bar",figsize=(12,6))
plt.xticks(np.arange(2), ('Non spam', 'spam'),rotation=0);

from tkinter.font import names
x_bal = [[1, 2], [3, 4], [5, 6]]
names = ['label', 'text']

"""Scaling the Data"""

sc=StandardScaler()
x_bal_scaled = sc.fit_transform(x_bal)

print(x_bal_scaled)

"""Splitting data into train and test"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.20, random_state = 0)

"""Decision Tree Model"""

from sqlalchemy.sql.functions import mode
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train_res,y_train_res)

"""Random Forest Model"""

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(x_train_res, y_train_res)

""" Naïve Bayes model"""

from operator import mod
from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()

print('Naive Bayes accuracy:', accuracy)

model.fit(x_train_res, y_train_res)

""" ANN model"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = Sequential()

x_train.shape

model.add(Dense(units = x_train_res.shape[1],activation = "relu",kernel_initiallizers = "random_unifrom"))

model.add(Dense(units=100,activation="relu",kernel_initializer="random_uniform"))

model.add(Dense(units=100,activation="relu",kernel_initializer="random_uniform"))

model.add(Dense(units=1,activation="sigmoid"))

model.compile(optimizer="adam",loss="binary_crossentropy",metrics=['accuracy'])

from numpy.random import Generator
generator = model.fit(x_train_res,y_train_res,epochs=10,steps_per_epoch=len(x_train_res)//64)

from nltk.translate import metrics
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential
#Create an ANN modelneith one hidden layer and an output layer
model = Sequential()
model.add(Dense(10, input_dim=X.shape[i], activation='relu'))
model.add(Dense(1, activation+'sigmoid'))

#Complie the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

#Train the model on the training data
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

#Evaluate the accuracy of the model on the testing data
accuracy = model.Evaluate(X_test, y_test, verbose=0)[1]
print('Ann accuracy:', accuracy)

""" Testing the model

"""

y_pred=model.predict(x_test)
y_pred

y_pr = np.where(y_pred>0.5,1,0)
y_test

y_test

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pr)
score = accuracy_score(y_test, y_pr)

print('Confusion Matrix:')
print(cm)
print('Accuracy Score Is: ' , score*100, '$')

from tables.file import File
import pickle

def new_review(new_review_text):
    with open('/content/cv1.pk1', 'rb') as file:
         cv = pickle.load(File)

"""In ANN we first have to save the model to the test the inputs"""

import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def new_review(new_review):
  new_review = new_review
  new_review = re.sub('[^a-zA-Z]', ' ', new_review)
  new_review = new_review.lower()
  new_review = new_review.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  all_stopwords.remove('not')
  new_review = [ps.stem(word)for word in new_review if not word in set(all_stopwords)]
  new_review = ' '.join(new_review)
  new_corpus = [new_review]
  new_X_test = cv.transform(new_corpus).toarray()
  print(new_X_test)
  new_y_pred = model.predict(new_X_test)
  print(new_y_pred)
  new_X_pred = np.where(new_y_pred>0,5,1,0)
  return new_y_pred

new_review=new_review(str(input("Enter new review...")))

"""Compare The Model"""

y_pred_binary = np.where(y_pred > 0.5, 1, 0)
cm = confusion_matrix(y_test, y_pred_binary)
score = accuracy_score(y_test, y_pred_binary)
print(cm)
print('accuracy score for naive bayes:', score * 100)

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test,y_pred)
score=accuracy_score(y_test,y_pred)
print(cm)
print('accuracy score is:-',score*100)

y_pred_binary = np.where(y_pred > 0.5, 1, 0)

cm = confusion_matrix(y_test, y_pred)
/score=accuracy_score(y_test,y_pred)
print(cm)
print('Accuracy_Score Is:- ' ,score*100)

cm1 = confusion_matrix(y_test, y_pred1)
score1 = accuracy_score(y_test,y_pred1)
print(cm1)
print('Accuracy Score Is:- ' ,score*100)

from sklearn.metrics import confusion_matrix,accuracy_score
cm=confusion_matrix(y_test,y_pred)
score=accuracy_score(y_test,y_pred)
print(cm)
print('accuracy score is:-',score*100)

"""Comparing model accuracy before & after applying
hyperparameter tuning
"""

cm=confusion_matrix(y_test,y_pred)
score=accuracy_score(y_test,y_pred)
print(cm)
print('Accuracy Score Is:-',score*100)

"""Saving our model"""

pickle.dump(cv,open('spam.pkl','wb'))

model.save('spam.h5')