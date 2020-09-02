""" Recuperation des mails contenant
un ou plusieurs mots de la liste qui lui est inférée
"""

import os
import pandas as pd
import numpy as np


def recup_mails(liste_mots):
    """recherche des mots dans les fichiers csv

    Args:
        liste_mots (liste): liste des mots a rechercher dans les mails
    """

    liste_util = os.listdir('./s_user_csv')
    for util in liste_util:
        data_frame_resultat = pd.DataFrame(columns=['Nom_utilisateur', 'Contenu_mail'])
        csv = pd.read_csv('./s_user_csv/' + util)
        for row in csv['content']:
            for word in liste_mots:
                if word in row:
                    ar_mail = np.array([[util, row]])
                    morceau_data_frame = pd.DataFrame(ar_mail,
                                                      columns=['Nom_utilisateur', 'Contenu_mail'])
                    data_frame_resultat = pd.concat([data_frame_resultat, morceau_data_frame])
        data_frame_resultat = data_frame_resultat.drop_duplicates(subset=['Contenu_mail'])
        data_frame_resultat.to_csv('../csv_trié/' + util)
