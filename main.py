import datetime
import openpyxl as xl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from datetime import date
from time import sleep
import flet as ft
import sys
import winshell
from shutil import copy

folder1=r"C:\Python\Bot_Whatsapp\Consultas"
folder2=r"C:\Python\Bot_Whatsapp\Edge_User"
def prog_inicial():
    #----------------------------------------------------------------------------------
    #Variáveis

    data=str(date.today()).split("-")
    prog_inicial.year=data[0]
    prog_inicial.Nav_config=r"C:\Python\Bot_Whatsapp\Edge_User" #Manter as configurações do navegador já definidas

    #----------------------------------------------------------------------------------
    #Funções

    def create_excel(): #Função que gera a pasta e os arquivos .xlsx
        cons_file=r"C:\Python\Bot_Whatsapp\Consultas"
        file_arch=os.path.dirname(os.path.abspath(__file__)) #Achando o local onde o arquivo está sendo executado
        #print(file_arch)
        if not os.path.exists(cons_file): #Cria uma pasta para destinar os arquivos excel 
            os.makedirs(cons_file)
        copy(os.path.join(file_arch,"Consultas(layout).xlsx"),os.path.join(cons_file,f"Consultas_{prog_inicial.year}.xlsx")) #Cria uma cópia da estrutura das consultas
        create_lnk()

    def create_lnk(): #Função que cria um atalho na área de trabalho para a pasta gerada
        desktop=winshell.desktop()
        cons_file=r"C:\Python\Bot_Whatsapp\Consultas"
        atalho_file=os.path.join(desktop,os.path.basename(cons_file)+".lnk")
        with winshell.shortcut(atalho_file) as atalho:
            atalho.path=cons_file
            atalho.working_directory=cons_file

    def create_navconf(): #Cria a pasta config do navegador
        if not os.path.exists(prog_inicial.Nav_config):
            os.makedirs(prog_inicial.Nav_config)

    #----------------------------------------------------------------------------------
    #Estrutura do código

    create_navconf()
    create_excel()

    opt=webdriver.EdgeOptions()
    opt.add_argument(f"--user-data-dir={prog_inicial.Nav_config}") #Definir local para salvar as configurações definidas ao navegador
    opt.add_experimental_option("detach",True)

    nav=webdriver.ChromiumEdge(options=opt)
    nav.get("https://web.whatsapp.com")

def prog_principal():
    #----------------------------------------------------------------------------------
    #Definição do dia atual
    list_date=str(datetime.date.today()).split("-")
    prog_principal.day=list_date[2]
    prog_principal.month=list_date[1]
    prog_principal.year=list_date[0]
    #print(day,month,year)

    #--------------------------

    #--------------------------
    #Funções

    def Row_cons(mes_inf): #Função que define em quais linhas da sheet analizada contém consultas para o dia seguinte
        row_cons=list()
        book_ncons=len(mes_inf["B"]) #Número de consultas existentes no mês
        for i in range(2,book_ncons+1):
            cell=str(mes_inf.cell(row=i,column=2).value)
            if cell==str(int(prog_principal.day)+1):
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
        check_last()
        last_open_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"last_open.txt")
        with open(last_open_file,"w") as arq:
            arq.write(f"{prog_principal.day}.{prog_principal.month}.{prog_principal.year}")

    def check_last(): #Função responsável por verificar se o programa já foi aberto no dia
        last_open_file=os.path.join(os.path.dirname(os.path.abspath(__file__)),"last_open.txt")
        att_day=f"{prog_principal.day}.{prog_principal.month}.{prog_principal.year}"
        with open(last_open_file,"r") as arq:
            inf_arq=arq.read()
            if inf_arq==att_day:
                open_error()

    def open_error(): #Função que cria uma interação com o usuário para verificar se o mesmo deseja abrir o programa ou não
        open_error.aux=False #Variável que define se o programa será encerrado, ou não.
        def main(page: ft.Page):
            page.window.height=140
            page.window.width=320
            page.window.resizable=False
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

    arq_xl=xl.load_workbook(fr"C:\Python\Bot_Whatsapp\Consultas\Consultas_{prog_principal.year}.xlsx") #Carregar a planilha que contém as consultas do ano atual
    #print(arq_xl.sheetnames)
    book_month=arq_xl[f"{prog_principal.month}"] #Selecionar worksheet do mês atual

    row_cons=Row_cons(book_month) #Função que define quais linhas da sheet contêm consultas para o dia atual
    #print(row_cons)

    day_consult=Infs(row_cons) #Função que define uma lista que contêm as consultas que ocorrerão no dia seguindo o padrão (paciente,médico,telefone)
    #print(day_consult)

    Last_open()

    #--------------------------

    #----------------------------------------------------------------------------------

    #----------------------------------------------------------------------------------
    #Parte do código referente ao Selenium

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
        month_str=("Jan.", "Fev.", "Mar.", "Abr.", "Mai.", "Jun.", "Jul.", "Ago.", "Set.", "Out.", "Nov.", "Dez.")
        msg=f"Bom dia, *{inf["Paciente"]}*. Tudo bem? Espero que sim. Passando para lembrar que sua consulta com o(a) doutor(a) *{inf["Médico"]}* está marcada para amanhã, *{str(int(prog_principal.day)+1)} de {month_str[int(prog_principal.month)+1]}*. Qualquer dúvida estou a disposição!!"
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
    #Programa

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

if not os.path.exists(folder1) or not os.path.exists(folder2):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"last_open.txt"),"w") as arq:
        arq.write("")
    prog_inicial()
else:
    prog_principal()