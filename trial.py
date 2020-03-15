# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 09:23:21 2020

@author: eib17gf
"""


import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import names
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing


class MyClassifier(object):
    def __init__(self):
        pass

    def word_feats(self, words):
        return dict([(word, True) for word in words])

    def main(self, sentence):

        positive = []
        negative = []
        target = []
        first = []
        count = 0
        
        with open('sentimentaldataset.csv', 'r') as file:
            reader = csv.reader(file)
            list = []
            for row in reader:
                count +=1
                if count <=1:
                    first = row
                if count>1 and count<206941:
                    row = row[0:3]
                    for i in row[2].split(' '):
                        newword = [row[0], row[1], i]
                        list.append(newword)
                        if len(row[0]) > 1:
                            positive.append(i)
                        elif len(row[1]) >1:
                            negative.append(i)

        
        positive_vocab = positive
        negative_vocab = negative
   
        
        for pos in positive_vocab:
            positive_features = [(self.word_feats(pos), 'pos')]
        negative_features = [(self.word_feats(neg), 'neg') for neg in negative_vocab]

        train_set = negative_features + positive_features
        classifier = NaiveBayesClassifier.train(train_set)

        # Predict
        neg = 0
        pos = 0

        sentence = sentence.lower()
        words = sentence.split(' ')
        for word in words:
            classResult = classifier.classify( self.word_feats(word))
            if classResult == 'neg':
                neg = neg + 1
            if classResult == 'pos':
                pos = pos + 1

        return {"text" : sentence,
                "positive": float(pos)/len(words),
                "negative": float(neg)/len(words)}

def word_feats(words):
        return dict([(word, True) for word in words])

positive = []
negative = []
words = []
target = []
first = []
count = 0

with open('sentimentaldataset.csv', 'r') as file:
    reader = csv.reader(file)
    
    list = []
    for row in reader:
        count +=1
        if count <=1:
            first = row
        if count>1 and count<206941:
            row = row[0:3]
            for i in row[2].split(' '):
                newword = [row[0], row[1], i]
                list.append(newword)
                words.append(i)
                
                if len(row[0]) > 1:
                    positive.append(i)
                elif len(row[1]) >1:
                    negative.append(i)

positive_vocab = positive
negative_vocab = negative

positive_features = [(word_feats(pos), 'pos') for pos in positive_vocab]
negative_features = [(word_feats(neg), 'neg') for neg in negative_vocab]

train_set = negative_features + positive_features
classifier = NaiveBayesClassifier.train(train_set)

def sentiment(sentence):
    myClassifier = MyClassifier()
    return (myClassifier.main(sentence))