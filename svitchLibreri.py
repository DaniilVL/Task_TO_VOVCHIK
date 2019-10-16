import os
def currentDirectory():
    odir = os.getcwd()
    print(odir)
def cengeDirectory():
    try:
        os.chdir(input())
    except:
        print("error")
def listFiles():
    try:
        files = os.listdir()
        print(files)
    except:
        print("error")
def createFile():
    try:
        file = open(input(),'x')
    except OSError:
        print("File name create")
def delFile():
    try:
        dontDelet=input()
        if (dontDelet=="Task_TO_VOVCHIK.py") or (dontDelet== "svitchLibreri.py"):
            print("PODUMOY")
        else:
            os.remove(dontDelet)

    except:
        print("error")
def Exit():
    exit()