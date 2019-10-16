import os

# Ткущая деректория
# odir = os.getcwd()
# print(odir)
# Сменить текущую деректорию
# try:
#     dir=os.chdir(input())
# except:
#     print("error")
# Выводит все файлы в текщей деректории
# list files in current directory
# create a file
# print(os.listdir())
# file=open('input','r')
# delete a file
# os.remove
# sys.exit()
from svitchLibreri import *

while True:
    print(""" Введите число
1. Вывод текущей директории 
2. Сменить текущую дректорию
3. Все файлы в текщей деректории
4. Создать файл
5. Удалить файл
6. Выйти""")
    try:
        number = input()
        if number =='1':
            currentDirectory()
        elif number == '2':
            cengeDirectory()
        elif number == '3':
            listFiles()
        elif number == "4":
            createFile()
        elif number == "5":
            delFile()
        elif number == "6":
            Exit()
    except:
        print('hur')
        exit()




