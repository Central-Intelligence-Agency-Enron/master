import os

def list_folder(link):

    if not link:
        link = r"C:\\Users\\utilisateur\\Desktop\\maildir\\"
    dirList = os.listdir(link)
    for dir in dirList:
        if os.path.isdir(link + dir) == True:
            print(dir)
        else:
            print(dir, " n'es pas un fichier")

if __name__ == "__main__":
    print("Indiquer l'emplacement des mails")
    list_folder(input())
