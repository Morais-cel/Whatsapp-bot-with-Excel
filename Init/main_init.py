from selenium import webdriver
import os
from time import sleep
from datetime import date
from shutil import copy
import winshell

#------------------------------------------------------------------------------------------------------------------------------------------------
#Variáveis

data=str(date.today()).split("-")
year=data[0]

Nav_config=r"C:\Python\Bot_Whatsapp\Edge_User" #Manter as configurações do navegador já definidas
int_time=50#Tempo de espera para abrir o whatsapp

#------------------------------------------------------------------------------------------------------------------------------------------------
#Funções

def create_excel(): #Função que gera a pasta e os arquivos .xlsx
    global year
    cons_file=r"C:\Python\Bot_Whatsapp\Consultas"
    file_arch=os.path.dirname(os.path.abspath(__file__)) #Achando o local onde o arquivo está sendo executado
    #print(file_arch)
    if not os.path.exists(cons_file): #Cria uma pasta para destinar os arquivos excel 
        os.makedirs(cons_file)
    copy(os.path.join(file_arch,"Consultas(layout).xlsx"),os.path.join(cons_file,f"Consultas_{year}.xlsx")) #Cria uma cópia da estrutura das consultas
    create_lnk()

def create_lnk(): #Função que cria um atalho na área de trabalho para a pasta gerada
    desktop=winshell.desktop()
    cons_file=r"C:\Python\Bot_Whatsapp\Consultas"
    atalho_file=os.path.join(desktop,os.path.basename(cons_file)+".lnk")
    with winshell.shortcut(atalho_file) as atalho:
        atalho.path=cons_file
        atalho.working_directory=cons_file

def create_navconf(): #Cria a pasta config do navegador
    global Nav_config
    if not os.path.exists(Nav_config):
        os.makedirs(Nav_config)

#------------------------------------------------------------------------------------------------------------------------------------------------
#Estrutura do código

create_navconf()
create_excel()

opt=webdriver.EdgeOptions()
opt.add_argument(f"--user-data-dir={Nav_config}") #Definir local para salvar as configurações definidas ao navegador
opt.add_experimental_option("detach",True)

nav=webdriver.ChromiumEdge(options=opt)
nav.get("https://web.whatsapp.com")
