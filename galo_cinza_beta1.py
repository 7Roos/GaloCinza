# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:22:46 2021

@author: mathe
"""

import PySimpleGUI as sg
import os

class TelaPython:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('Local'),sg.Input(key='folder'),sg.FolderBrowse()],
            [sg.Text('Extensão'),sg.Input(key='extensao')],
            [sg.Text('Álbum'),sg.Input(key='album')],
            [sg.Text('Ano'),sg.Input(key='year')],
            [sg.Text('Cidade'),sg.Input(key='city')],
            [sg.Button('Gerar txt')]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        
        
    def Iniciar(self):
        # Extrair os dados da tela
        while True:
            self.button, self.values = self.janela.Read()
            pasta = self.values["folder"]
            extensao = self.values["extensao"]
            album = self.values["album"]
            year = self.values["year"]
            city = self.values["city"]
            arquivo = open(str(pasta) + "\\" + str(album) + " " + str(year) + " informação.txt",'w')
            arquivo.write(str(album) + " (" + str(year) + ") \n" + str(city) + "\n \n")
            def ler(extensao,pasta):
                lista = []
                for file in os.listdir(pasta): 
                    if file.endswith(str(extensao)):
                        lista.append(file)
                return lista
        
            def separa():
                frases = []
                music = ler(extensao,pasta)
                for i in range(len(music)):
                    frases.append(str(music[i]) + "\n")
                return arquivo.writelines(frases)
            separa()
            arquivo.close()

        print(self.values)
        
tela = TelaPython()
tela.Iniciar()
