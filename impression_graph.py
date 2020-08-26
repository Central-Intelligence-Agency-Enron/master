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
LISTE_PERSONNES = ["kean-s", "shackleton-s", "dasovich-j", "cash-m", "farmer-d", "stokley-c", "harris-s"]
LISTE_MOTS = ["dollar", "buy", "sell", "trade", "agreement", "transaction", "exchange", "concluded"]
LISTE_TOP = []
DATA_TOP = []

#Initialisation des fonctions
TOKENIZER = RegexpTokenizer(r'\w+')


for name in LISTE_PERSONNES:
    text = ""
    liste = ""
    csv = pd.read_csv('s_user_csv/' + name + ".csv", sep=',')
    for row in csv['content']:
        text += row.lower()
    liste = TOKENIZER.tokenize(text)
    freq_dist = FreqDist(liste)
    top = freq_dist.most_common(10000)

    data_frame = pd.DataFrame(top, columns=['Mot', '''Nb d'apparition'''])
    LISTE_TOP.append(data_frame)


for top in LISTE_TOP:
    word_values = []
    for word in LISTE_MOTS:
        nb_word = sum(top["Nb d'apparition"][top['Mot'].str.contains(word)])/len(top)
        word_values.append(nb_word)
    word_values = np.concatenate((word_values, [word_values[0]]))
    DATA_TOP.append(word_values)

LABEL_PLACEMENT = np.linspace(start=0, stop=2*np.pi, num=len(word_values))
plt.figure(figsize=(10, 10))
plt.subplot(polar=True)
for values in DATA_TOP:
    plt.plot(LABEL_PLACEMENT, values)

LINES, LABELS = plt.thetagrids(np.degrees(LABEL_PLACEMENT), labels=LISTE_MOTS)
plt.legend(labels=LISTE_PERSONNES)
plt.show()

