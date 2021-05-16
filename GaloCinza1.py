import os

# Header
folder = input("Qual é o local? ")
extension = input("Qual é a extensão? ")
album = input("Qual é o álbum/festival? ")
year = input("Qual é o ano? ")
city = input("Qual é a cidade? ")

# Creates the file and writes the header
archive = open(str(folder) + "\\" + str(album) + " " +
               str(year) + " informação.txt", 'w')
archive.write(str(album) + " (" + str(year) + ") \n" + str(city) + "\n \n")


def separator(extension, folder):
    lista = []
    for file in os.listdir(folder):
        if file.endswith(str(extension)):
            lista.append(file)
    return lista


def ListTitles():
    names = []
    music = separator(extension, folder)
    for i in range(len(music)):
        names.append(str(music[i]) + "\n")
    return archive.writelines(names)


ListTitles()
archive.close()
