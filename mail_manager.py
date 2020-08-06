from pathlib import Path
import email
from pandas import DataFrame
import pandas as pd
import time


class mail():

    def __init__(self, box_type, mail_file):
        self.box_type = box_type
        self.message = self._parse_mail(mail_file.read())
        self.header = self._get_header()
        self.content = self._get_content()

    def get(self, item):
        list_values = self.message.get_all(item)
        if list_values:
            return '|'.join(list_values)
        else:
            return ''

    def _parse_mail(self, text):
        return email.message_from_string(text)

    def _get_header(self):
        return self.message.items()

    def get_csv(self):
        self.message.get

    def _get_content(self):
        return self.message.get_payload()

class user_mail():

    def __init__(self, user, mail_path):
        self.user = user
        self.list_mail = self._build_list_mail(mail_path)

    def _build_list_mail(self, mail_path):
        list_mail = []
        print('exploration du dossier user ' + mail_path.name)
        for mail_file in mail_manager.get_files(mail_path):
            with open(mail_file, "r") as f:
                list_mail.append(
                    mail(mail_file.parent.name, f)
                )
        return list_mail
    
    def export_csv(self):
        #data = DataFrame()
        list_from_address = []
        list_from_name = []
        list_to_address = []
        list_to_name = []
        list_cc = []
        list_bcc = []
        list_content = []
        list_title = []
        list_date = []
        list_origin = []
        list_file = []

        for mail in self.list_mail:
            list_from_address.append(mail.get("From"))
            list_from_name.append(mail.get("X-From"))
            list_to_address.append(mail.get("To"))
            list_to_name.append(mail.get("X-To"))
            list_cc.append(mail.get("X-cc"))
            list_bcc.append(mail.get("X-bcc"))
            list_content.append(mail.content)
            list_title.append(mail.get('Subject'))
            list_date.append(mail.get('Date'))
            list_origin.append(mail.get('X-Origin'))
            list_file.append(mail.get('X-Folder') + mail.get('X-FileName'))
            
        dict_email = {
            'from_address': list_from_address
            , 'from_name': list_from_name
            , 'to_address': list_to_address
            , 'to_name': list_to_name
            , 'cc': list_cc
            , 'bcc': list_bcc
            , 'content': list_content
            , 'title': list_title
            , 'date': list_date
            , 'origin': list_origin
            , 'file': list_file
        }

        df_mail = DataFrame.from_dict(dict_email)
        df_mail.to_csv('user_csv/' + self.user + '.csv')

class mail_manager():

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.list_user = self._build_user_mail(folder_path)

    def _build_user_mail(self, folder_path):
        list_user = []
        for path in folder_path.iterdir():
            # list_user.append(
            user_mail(path.name, path).export_csv()
            # )
        return list_user

    def export_csv(self):
        for user in self.list_user:
            user.export_csv()

    @staticmethod
    def get_mail_location():
        print("Indiquer l'emplacement de maildir")
        link = Path(input())
        return link

    @classmethod
    def get_files(cls, folder_path, liste_fichier=[]):
        """ Retourne la liste des fichiers contenus dans le dossier spécifié

        Args:
            path (str): path du dossier
            liste_fichier (list of str): liste de paths vers les fichiers
        """

        for path in folder_path.iterdir():
            # if path.is_dir():
            #     print("Exploration dossier ", path.name, " avec nbr elements ", len(list(path.iterdir())))

            if path.is_dir():
                cls.get_files(path, liste_fichier)
            elif path.is_file():
                liste_fichier.append(path)
            else:
                print('truc chelou: ', )
                continue

        return liste_fichier


if __name__ == '__main__':
    maildir = Path("../maildir")
    manager = mail_manager(maildir)
    manager.export_csv()
