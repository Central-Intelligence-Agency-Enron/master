from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

from pathlib import Path

_maildir_path = Path("C:/Users/utilisateur/Desktop/maildir")

def mail_location(link=None):
    # print("Indiquer l'emplacement de maildir")
    # link = Path(input())
    return link

def get_text(file_path):
    raise NotImplementedError

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

    path = mail_location(_maildir_path)

    liste_fichier = get_files(path)

    print(
        "total de mails: ", len(liste_fichier)
        )

