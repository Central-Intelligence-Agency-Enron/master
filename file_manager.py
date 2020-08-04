from pathlib import Path

from mail_parser import mail_parser
from text_functions import CleanText

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

    path = Path("../maildir/arnold-j")

    # path = get_mail_location()

    liste_fichier = get_files(path)

    text_sum = str()
    for file in liste_fichier:
        with open(file, 'r') as mail_file:
            message = mail_parser(mail_file)
            message_cleaned = CleanText(message.content).preprocessing()
            text_sum += message_cleaned

    with open("cleaned_arnold-j_mails.txt", "w", encoding="utf-8") as file:
        file.write(
            text_sum
        )

    print(
        "total de mails: ", len(liste_fichier)
        )
