""" Extraction des textes des fichiers csv des personnes conetnues dans liste_personnes
Comptage des mots présent dans les mails et création du top 10 000 des mots
Impression d'un graphique montrant le ratio des mots présents dans liste_mots par mail et par personne
"""

import pandas as pd
import numpy as np
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt


i = 0
liste_personnes = ["kean-s", "shackleton-s", "dasovich-j", "cash-m", "farmer-d", "stokley-c", "harris-s"]
liste_mots = ["dollar", "buy", "sell", "trade", "agreement", "transaction", "exchange", "concluded"]
liste_top = []
data_top = []

#Initialisation des fonctions
tokenizer = RegexpTokenizer(r'\w+')


for name in liste_personnes:
    text = ""
    liste = ""
    csv = pd.read_csv('s_user_csv/' + name + ".csv", sep=',')
    for row in csv['content']:
        text += row.lower()
    liste = tokenizer.tokenize(text)
    freq_dist = FreqDist(liste)
    top = freq_dist.most_common(10000)

    data_frame = pd.DataFrame(top, columns=['Mot', '''Nb d'apparition'''])
    liste_top.append(data_frame)


for top in liste_top:
    word_values = []
    for word in liste_mots:
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

