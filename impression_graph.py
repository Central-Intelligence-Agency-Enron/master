import pandas as pd
import numpy as np
import nltk
from pathlib import Path
import os
import nltk.corpus
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import matplotlib.pyplot as plt


i = 0
liste_personnes = ["kean-s", "shackleton-s", "dasovich-j", "cash-m", "farmer-d"]
liste_mots= ["dollar", "buy", "sell", "trade", "agreement", "transaction"]
liste_top = []
data_top = []

#Initialisation des fonctions
stopW = stopwords.words('english')
tokenizer = RegexpTokenizer(r'\w+')


for name in liste_personnes:
    text = ""
    liste = ""
    csv = pd.read_csv('s_user_csv/' + name + ".csv", sep=',')
    for row in csv['content']:
        text += row.lower()
    liste = tokenizer.tokenize(text)
    liste = [word for word in liste if word not in stopW]
    freq_dist = FreqDist(liste)
    top = freq_dist.most_common(10000)

    data_frame = pd.DataFrame(top, columns = ['Mot', '''Nb d'apparition'''])
    liste_top.append(data_frame)


for top in liste_top:
    word_values = []
    for word in liste_mots :
        nb_word = sum(top["Nb d'apparition"][top['Mot'].str.contains(word)])/len(top)
        word_values.append(nb_word)
    word_values = np.concatenate((word_values, [word_values[0]]))
    data_top.append(word_values)

label_placement = np.linspace(start=0, stop=2*np.pi, num=len(word_values))
plt.figure(figsize=(10, 10))
plt.subplot(polar=True)
for values in data_top:
    plt.plot(label_placement, values)

lines, labels = plt.thetagrids(np.degrees(label_placement), labels=liste_mots)
plt.legend(labels=liste_personnes)

plt.show()