import os
import pandas as pd
import numpy as np
from nltk.probability import FreqDist
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt

LISTE_TOP = []
DATA_TOP = []

#Initialisation des fonctions
TOKENIZER = RegexpTokenizer(r'\w+')

def impression_graph(liste_mots):
    liste_util = os.listdir('../csv_trié')

    for name in liste_util:
        text = ""
        liste = ""
        csv = pd.read_csv('../csv_trié/' + name , sep=',')
        for row in csv['Contenu_mail']:
            text += row.lower()
        liste = TOKENIZER.tokenize(text)
        freq_dist = FreqDist(liste)
        top = freq_dist.most_common(10000)

        data_frame = pd.DataFrame(top, columns=['Mot', '''Nb d'apparition'''])
        LISTE_TOP.append(data_frame)


    for top in LISTE_TOP:
        word_values = []
        for word in liste_mots:
            nb_word = sum(top["Nb d'apparition"][top['Mot'].str.contains(word)])/len(top)
            word_values.append(nb_word)
        word_values = np.concatenate((word_values, [word_values[0]]))
        DATA_TOP.append(word_values)


    LABEL_PLACEMENT = np.linspace(start=0, stop=2*np.pi, num=len(word_values))
    plt.figure(figsize=(10, 10))
    plt.subplot(polar=True)
    for values in DATA_TOP:
        plt.plot(LABEL_PLACEMENT, values)


    LINES, LABELS = plt.thetagrids(np.degrees(LABEL_PLACEMENT), labels=liste_mots)
    plt.legend(labels=liste_util, loc=(0.95, 0.9))
    plt.show()


def impression_graph(liste_mots):
    liste_util = os.listdir('../csv_trié')
    data_frame_final = pd.DataFrame(columns=['Mot', '''Nb d'apparition'''])
    for name in liste_util:
        text = ""
        liste = ""
        csv = pd.read_csv('../csv_trié/' + name , sep=',')
        for row in csv['Contenu_mail']:
            text += row.lower()
        liste = TOKENIZER.tokenize(text)
        freq_dist = FreqDist(liste)
        top = freq_dist.most_common(10000)

        data_frame = pd.DataFrame(top, columns=['Mot', '''Nb d'apparition'''])
        data_frame_final = pd.concat([data_frame_final, data_frame])
        LISTE_TOP.append(data_frame_final)


    for top in LISTE_TOP:
        word_values = []
        for word in liste_mots:
            nb_word = sum(top["Nb d'apparition"][top['Mot'].str.contains(word)])/len(top)
            word_values.append(nb_word)
        word_values = np.concatenate((word_values, [word_values[0]]))
        DATA_TOP.append(word_values)

    LABEL_PLACEMENT = np.linspace(start=0, stop=2*np.pi, num=len(word_values))
    plt.figure(figsize=(10, 10))
    plt.subplot(polar=True)
    for values in DATA_TOP:
        plt.plot(LABEL_PLACEMENT, values)


    LINES, LABELS = plt.thetagrids(np.degrees(LABEL_PLACEMENT), labels=liste_mots)
    plt.legend(labels=liste_util, loc=(0.95, 0.9))
    plt.show()