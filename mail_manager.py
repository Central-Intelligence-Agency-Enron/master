from pathlib import Path
import email


class mail():

    def __init__(self, mail_file):
        self.message = self._parse_mail(mail_file.read())
        self.header = self._get_header()
        self.content = self._get_content()

    def _parse_mail(self, text):
        return email.message_from_string(text)

    def _get_header(self):
        return self.message.items()

    def _get_content(self):
        return self.message.get_payload()


class mail_manager():

    def __init__(self, folder_path):
        self.list_mail = []
        self.folder_path = folder_path

        self._build_list_mail()

    def _build_list_mail(self):
        for file in self._get_files(self.folder_path):
            self.list_mail.append(mail(file))

    @staticmethod
    def get_mail_location():
        print("Indiquer l'emplacement de maildir")
        link = Path(input())
        return link

    @classmethod
    def _get_files(cls, folder_path, liste_fichier=[]):
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
