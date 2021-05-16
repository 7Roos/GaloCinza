# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:22:46 2021

@author: mathe
"""

import PySimpleGUI as sg
import os

sg.theme('DarkGrey2')
class WindowPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Local', size=(8, 0)), sg.Input(
                key='folder'), sg.FolderBrowse()],
            [sg.Text('Extensão', size=(8, 0)), sg.Input(key='extension')],
            [sg.Text('Álbum', size=(8, 0)), sg.Input(key='album')],
            [sg.Text('Ano', size=(8, 0)), sg.Input(key='year')],
            [sg.Text('Cidade', size=(8, 0)), sg.Input(key='city')],
            [sg.Button('Gerar txt')],
        ]
        # Janela
        self.Window = sg.Window("Galo Cinza").layout(layout)

    def Start(self):
        while True:
            # Extrair os dados da tela
            self.button, self.values = self.Window.Read()
            if self.button == sg.WINDOW_CLOSED:
                break
            # Header
            folder = self.values["folder"]
            extension = self.values["extension"]
            album = self.values["album"]
            year = self.values["year"]
            city = self.values["city"]

            # Creates the file and writes the header
            archive = open(str(folder) + "\\" + str(album) +
                           " " + str(year) + " informação.txt", 'w')
            archive.write(str(album) + " (" + str(year) +
                          ") \n" + str(city) + "\n \n")

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


Window = WindowPython()
Window.Start()

# To create an .exe with this script, just type in the terminal: pyinstaller --onefile .\GaloCinza1.pyw
