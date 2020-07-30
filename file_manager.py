import os

def list_folder(link):

    if not link:
        link = r"C:\\Users\\utilisateur\\Desktop\\maildir\\"

    dirList = os.scandir(link)
    for dir in dirList:
        if os.path.isdir(dir) == True:
            print(dir.path, '\t\t', dir.name)
        else:
            print(dir.path, " n'es pas un fichier")

if __name__ == "__main__":
    print("Indiquer l'emplacement des mails")
    list_folder(input())
