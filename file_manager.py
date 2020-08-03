from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

from pathlib import Path

_maildir_path = Path("C:/Users/utilisateur/Desktop/maildir")

def get_mail_location():
    print("Indiquer l'emplacement de maildir")
    link = Path(input())
    return link

def get_text_from_list_file(list_file):
    sum_text = str()

    for file in list_file:
        sum_text += get_text(file)

    return sum_text

def get_text(path_object):
    return path_object.read_text()

def get_files(folder_path, liste_fichier=[]):
    """ Retourne la liste des fichiers contenues dans le dossier spécifié

    Args:
        path (str): path du dossier
        liste_fichier (list of str): liste de paths vers les fichiers
    """

    for path in folder_path.iterdir():
        # if path.is_dir():
        #     print("Exploration dossier ", path.name, " avec nbr elements ", len(list(path.iterdir())))

        if path.is_dir():
            get_files(path, liste_fichier)
        elif path.is_file():
            liste_fichier.append(path)
        else:
            print('truc chelou: ', )
            continue

    return liste_fichier


if __name__ == "__main__":

    

    path = Path("C:/Users/utilisateur/Desktop/maildir/arnold-j")

    # path = get_mail_location()

    liste_fichier = get_files(path)

    with open("arnold-j_mails.txt", "w", encoding="utf-8") as file:
        file.write(
            get_text_from_list_file(liste_fichier)
        )

    print(
        "total de mails: ", len(liste_fichier)
        )
