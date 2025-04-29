import datetime
import openpyxl as xl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep
import flet as ft
import sys
#----------------------------------------------------------------------------------------------------------------
#Parte do código relativo a etapas desenvolvidas antes de abrir o navegador
#--------------------------
#Funções

def Row_cons(mes_inf): #Função que define em quais linhas da sheet analizada contém consultas para o dia seguinte
    row_cons=list()
    book_ncons=len(mes_inf["B"]) #Número de consultas existentes no mês
    for i in range(2,book_ncons+1):
        cell=str(mes_inf.cell(row=i,column=2).value)
        if cell==str(int(day)+1):
            row_cons.append(i)
    return row_cons

def Infs(day_row): #Função que adquire os dados do paciente presente em tal coluna i, das selecionadas anteriormente pela função Row_cons
    dict_inf=("Paciente","Médico","Telefone")
    cons=dict()
    consultas=list()
    for r in day_row:
        for c in range(0,3):
            cell=book_month.cell(row=r,column=c+3).value
            cons[dict_inf[c]]=cell
        consultas.append(cons.copy())
    return consultas

def Last_open(): #Função que sobrescreve o arquivo txt e informa quando foi a última abertura do aplicativo
    global day, month, year
    check_last()
    last_open_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"last_open.txt")
    with open(last_open_file,"w") as arq:
        arq.write(f"{day}.{month}.{year}")

def check_last(): #Função responsável por verificar se o programa já foi aberto no dia
    global day, month, year
    last_open_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"last_open.txt")
    att_day=f"{day}.{month}.{year}"
    with open(last_open_file,"r") as arq:
        inf_arq=arq.read()
        if inf_arq==att_day:
            open_error()

def open_error(): #Função que cria uma interação com o usuário para verificar se o mesmo deseja abrir o programa ou não
    open_error.aux=False #Variável que define se o programa será encerrado, ou não.
    def main(page: ft.Page):
        page.window.height=140
        page.window.width=320
        page.window.alignment=ft.alignment.center
        page.window.icon=os.path.join(os.path.dirname(os.path.abspath(__file__)),"whatsapp.ico")
        page.title="Verificação"

        def next_step(e): #Define,utilizando a data do botão selecionado, qual será a ação realizada a seguir, além de que fecha as janelas abertas pelo flet
            but=e.control.data
            if but=="CONT":
                page.window.close()
                open_error.aux=True
            else:
                page.window.close()

        inf=ft.Container(
            width=page.window.width,
            height=page.window.height/2,
            content=ft.Text(
                            value="O programa já foi iniciado no dia de hoje. Gostaria de abrí-lo mesmo assim?",
                            text_align=ft.TextAlign.CENTER
                    ),
            margin=-5,
            padding=3,
            
        )
        bot1=ft.ElevatedButton(
            text="ABRIR",
            width=100,
            style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        overlay_color=ft.colors.GREEN
                    ),
            data="CONT",
            on_click=next_step
        )
        bot2=ft.ElevatedButton(
            text="CANCELAR",
            width=100,
            style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        overlay_color=ft.colors.RED
                    ),
            data="STOP",
            on_click=next_step
        )
        bot=ft.Row(
            width=page.window.width,
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                    bot1,
                    bot2
            ]
        )
        init=ft.Container(
            width=page.window.width,
            height=page.window.height-50,
            content=ft.Column(
                            width=page.window.width,
                            height=page.window.height,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=-10,
                            controls=[
                                    inf,
                                    bot
                            ]
                        ),
            bgcolor=ft.colors.WHITE10,
            margin=-5,
            padding=5,
            border_radius=ft.border_radius.all(5)
        )
        page.add(init)
    ft.app(main)
    if not open_error.aux: #Definindo se o programa será encerrado, ou não.
        sys.exit()
#--------------------------
#--------------------------
#Programa

#Definição do dia atual
list_date=str(datetime.date.today()).split("-")
day=list_date[2]
month=list_date[1]
year=list_date[0]
#print(day,month,year)

#Input de informações de consultas do dia

arq_xl=xl.load_workbook(fr"C:\Python\Bot_Whatsapp\Consultas\Consultas_{year}.xlsx")
#print(arq_xl.sheetnames)
book_month=arq_xl[f"{month}"] #Selecionar worksheet do mês atual

row_cons=Row_cons(book_month) #Função que define quais linhas da sheet contêm consultas para o dia atual
#print(row_cons)

day_consult=Infs(row_cons) #Função que define uma lista que contêm as consultas que ocorrerão no dia seguindo o padrão (paciente,médico,telefone)
#print(day_consult)

Last_open()

#--------------------------
#----------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------
#Parte do código referente ao Selenium
#--------------------------
#Funções
def conv_start(inf_day):
    for p in inf_day:
        search1=nav.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div/div/div[1]/p')
        search1.send_keys(p["Telefone"])
        sleep(2)
        cont=nav.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[2]/div[1]/span/div/span/div/div[2]/div[3]/div[2]/div/div/span[1]')
        cont.click()
        send_msg(p)
        nconv=nav.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button/span') #Botão responsável por iniciar um novo chat
        nconv.click()
        sleep(1)

def send_msg(inf):
    global day,month
    month_str=("Jan.", "Fev.", "Mar.", "Abr.", "Mai.", "Jun.", "Jul.", "Ago.", "Set.", "Out.", "Nov.", "Dez.")
    msg=f"Bom dia, *{inf["Paciente"]}*. Tudo bem? Espero que sim. Passando para lembrar que sua consulta com o(a) doutor(a) *{inf["Médico"]}* está marcada para amanhã, *{str(int(day)+1)} de {month_str[int(month)+1]}*. Qualquer dúvida estou a disposição!!"
    chat=nav.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
    chat.send_keys(msg)
    sleep(0.5)
    chat.send_keys(Keys.ENTER)
    sleep(1)

#--------------------------
#--------------------------
#Variáveis

Nav_config=r"C:\Python\Bot_Whatsapp\Edge_User" #Manter as configurações do navegador já definidas
int_time=10 #Tempo de espera para abrir o whatsapp

#--------------------------

opt=webdriver.EdgeOptions()
opt.add_argument(f"--user-data-dir={Nav_config}") #Definir local para salvar as configurações definidas ao navegador



nav=webdriver.ChromiumEdge(options=opt)
nav.get("https://web.whatsapp.com")
sleep(int_time)

nconv=nav.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div/div[3]/header/header/div/span/div/div[1]/button/span') #Botão responsável por iniciar um novo chat
nconv.click()
sleep(1)

conv_start(day_consult)
nav.close()