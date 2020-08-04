import pandas as pd
import numpy as np
import nltk
import os
import nltk.corpus
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer


with open("C:/Users/David/Documents/GIT/ENRON/master/arnold-j_mails.txt", "r", encoding="utf-8") as file :
    text = file.read()

lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')
text = lemmatizer.lemmatize(text)
liste = tokenizer.tokenize(text)
fdist = FreqDist(liste)
top = fdist.most_common(5000)


with open("C:/Users/David/Documents/GIT/ENRON/master/nb_mots.txt", "w", encoding="utf-8") as file :
    file.write(str(top))