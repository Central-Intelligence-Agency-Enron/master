from pathlib import Path
import os
import csv
import email
import pandas as pd
from mail_manager import mail_manager
from joblib import load, dump
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

from joblib import load

import random
import math

def get_mails(MAILDIR_PATH):
    """Return a list of Enron users with their mail at format:
    [
        [name, email]
        , [name, email]
        , [name, email]
    ]

    Args:
        MAILDIR_PATH (string): link to maildir folder

    Returns:
        array: array that contains name and email for each user
    """
    list_user_mail = []
    for path in MAILDIR_PATH.iterdir():
        for p in path.iterdir():
            if p.name == "sent" or p.name == "_sent_mail" or p.name == "sent_items":
                user_file = Path(p.as_posix() + '/' + os.listdir(p.absolute())[0])
                user_mail = email.message_from_string(
                    user_file.open().read()
                ).get('From')

                list_user_mail.append([
                    p.parent.name
                    , user_mail
                ])
                break

    # Utilisateur sans boite "sent"
    list_user_mail.append([
        "harris-s"
        , "steven.harris@enron.com"
    ])
    list_user_mail.append([
        "stokley-c"
        , "chris.stokley@enron.com"
    ])

    list_user_mail.sort(key=get_name)
    return list_user_mail

def get_name(user_mail):
    """Used for automatic sort in get_mails()

    Args:
        user_mail (list): list that contains name and mail of a user

    Returns:
        string: name of the user sent in list
    """
    return user_mail[0]

def matrice(list_user_mail):
    list_user = []

    for user_mail in list_user_mail:
        list_user.append(user_mail[0])

    dict_user = {}
    for user in list_user:
        dict_user.update({user: [0]*len(list_user), })

    return pd.DataFrame(dict_user, index = list_user)

def get_files_by_name(maildir, name):
    list_mails = []

    for path in maildir.iterdir():
        if path.name == name:
            list_mails = mail_manager.get_files(path,list_mails)
            return list_mails

    raise Exception("Aucun dossier trouvé au nom de " + name)

def increment_dataframe(df_user, current_user, list_mail, list_user_mail):
    
    rand = hex(math.floor(random.random()*1000000000000000000))

    for mail in list_mail:
        recognized = False
        for user_mail in list_user_mail:
            if mail == user_mail[1]:
                df_user.loc[user_mail[0]][current_user] += 1
                # nbr mails que user_mail[0] a reçu de current_user
                recognized = True
                break
                
        # if not recognized:
        #     print(rand, " Mail non reconnu: " + mail)

def get_weight(maildir, df_user, list_user_mail):

    # print(df_user.iloc[0].name)

    for index in range(len(df_user)):
        current_user = df_user.iloc[index].name
        list_mails = get_files_by_name(
            maildir, 
            current_user
        )

        # for test purpose
        print("exploration des mails du user ", current_user)
        print("Le user ", current_user, " a ", len(list_mails), " mails")

        for mail in list_mails:
            message = email.message_from_file(mail.open())

            from_mail = message.get('From')
            to_mails = (message.get_all('To') if message.get_all('To') else []) + (message.get_all('cc') if message.get_all('cc') else [])

            # filter data from message object
            to_mails = split_mail(to_mails)
            to_mails = clean_mail(to_mails)

            for user_mail in list_user_mail:
                if user_mail[1] == from_mail and user_mail[0] == current_user:
                    increment_dataframe(df_user, current_user, to_mails, list_user_mail)
                    break

        # Sauvegarde du dataframe
        dump(df_user, 'df_user_poi.joblib')
        print(df_user.loc[:,current_user])
        print()

    return df_user

def split_mail(list_mail):
    splitted_list = []
    for mail in list_mail:
        for splitted_mail in mail.split(", "):
            splitted_list.append(splitted_mail)

    return splitted_list

def clean_mail(list_mail):
    return [mail.replace("\n\t", "") for mail in list_mail]

def social_network(df_weight):
    G_weighted = nx.Graph()

    limit = np.mean(df_weight.quantile(0.9999))
    print(limit)

    for sender in df_weight.columns:

        for receiver in df_weight.index:
            weight = df_weight.loc[receiver][sender]
            if weight <= limit:
                G_weighted.add_edge(sender,receiver, weight=weight)

    pos = nx.spring_layout(G_weighted)  # positions for all nodes

    elarge = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] > limit*2]
    esmall = [(u, v) for (u, v, d) in G_weighted.edges(data=True) if d["weight"] <= limit*2]

    nx.draw_networkx_nodes(G_weighted, pos, node_size=50)
    nx.draw_networkx_edges(G_weighted, pos, edgelist=elarge, width=1)
    nx.draw_networkx_edges(
        G_weighted, pos, edgelist=esmall, width=0.5, edge_color="b", style="dashed"
    )
    nx.draw_networkx_labels(G_weighted, pos, font_size=3, font_family="sans-serif")

    plt.axis("off")
    # nx.draw_circular(G_weighted, with_labels=True)
    
    plt.savefig("social_network.png")
    plt.show()


if __name__ == '__main__':
    # maildir = Path("../maildir")
    # list_user_mail = get_mails(maildir)

    # df_user = matrice(list_user_mail)
    # df_weight = get_weight(maildir, df_user, list_user_mail)

    # print("Weight count finished")
    # print(df_weight)
    # social_network(df_weight)

    ################# Ou avec le fichier df_user_poi déjà généré #################
    
    df_weight = load('df_user_poi.joblib')
    social_network(df_weight)
    