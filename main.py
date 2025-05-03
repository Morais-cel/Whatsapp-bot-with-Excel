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

    def create_last():
        if not os.path.exists(r"C:\Python\Bot_Whatsapp\last_open.txt"):
            with open(r"C:\Python\Bot_Whatsapp\last_open.txt","w") as arq:
                arq.write("")

    def config():
        create_navconf()
        create_excel()
        create_last()

    def tutorial_func(): #Interface FLET feita para iniciar um tutorial para o usuário
        def main(page: ft.Page):
            imgs_folder=fr"{os.path.dirname(os.path.abspath(__file__))}\Img"
            main.num=0

            def hover_but_inf(e):
                if e.data=="true":
                    e.control.width=230
                    e.control.right=page.window.width/2-115
                    e.control.content=ft.Text(
                                            value="Clique para ver as informações",
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                            max_lines=1,
                                            color=ft.colors.BLACK,
                                            style=ft.TextStyle(
                                                            weight=ft.FontWeight.BOLD
                                            )
                    )
                else:
                    e.control.width=30
                    e.control.right=page.window.width/2-25
                e.control.update()

            def hover_but_inf2(e):
                if e.data=="true":
                    e.control.width=250
                    e.control.content=ft.Text(
                                            value="Clique para ocultar as informacoes",
                                            overflow=ft.TextOverflow.ELLIPSIS,
                                            max_lines=1,
                                            color=ft.colors.BLACK,
                                            style=ft.TextStyle(
                                                            weight=ft.FontWeight.BOLD
                                            )
                    )
                else:
                    e.control.width=30
                e.control.update()

            def but_animat_end(e):
                if e.control.width==30:
                    if not e.control.data=="back_but":
                        e.control.content=ft.Icon(
                                                name=ft.Icons.INFO_OUTLINED,
                                                color=ft.colors.BLACK
                        )
                    else:
                        e.control.content=ft.Icon(
                                                name=ft.Icons.ARROW_DOWNWARD_ROUNDED,
                                                color=ft.colors.BLACK
                        )
                    e.control.update()

            def change_button(e):
                if e.data=="true":
                    if e.control.data=="min_but":
                        e.control.content.color=ft.colors.RED
                        e.control.bgcolor=ft.colors.BLACK38
                    else:
                        e.control.content.color=ft.colors.GREEN
                        e.control.bgcolor=ft.colors.BLACK38
                else:
                    if e.control.data=="min_but":
                        e.control.content.color=ft.colors.RED
                    else:
                        e.control.content.color=ft.colors.GREEN
                    e.control.bgcolor=ft.colors.TRANSPARENT
                e.control.update()

            def inf_container_show(e):
                if e.control.data=="inf_but2":
                    src_val=os.path.join(imgs_folder,"exp_page2.png")
                    scale_val=0.8
                else:
                    src_val=os.path.join(imgs_folder,"exp_page3.png")
                    scale_val=0.8
                if e.control.data=="inf_but2" or e.control.data=="inf_but3":
                    init.content.controls[0].content.controls[0].controls[1].opacity=0
                    init.content.controls[0].content.controls[1].height=page.window.height-50
                    init.content.controls[0].content.controls[1].content=ft.Column(
                                                                                width=page.window.width-30,
                                                                                height=page.window.height-50,
                                                                                spacing=0,
                                                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                                                controls=[
                                                                                    ft.Container(
                                                                                            width=30,
                                                                                            height=30,
                                                                                            alignment=ft.alignment.center,
                                                                                            content=ft.Icon(
                                                                                                        name=ft.Icons.ARROW_DOWNWARD_ROUNDED,
                                                                                                        color=ft.colors.BLACK,
                                                                                            ),
                                                                                            bgcolor=ft.colors.BLACK38,
                                                                                            margin=5,
                                                                                            border_radius=ft.border_radius.all(5),
                                                                                            animate=ft.animation.Animation(600, "bouceout"),
                                                                                            on_hover=hover_but_inf2,
                                                                                            on_click=inf_container_show,
                                                                                            on_animation_end=but_animat_end,
                                                                                            data="back_but"
                                                                                    ),
                                                                                    ft.Image(
                                                                                        width=page.window.width,
                                                                                        src=src_val,
                                                                                        scale=scale_val
                                                                                    )
                                                                                ]
                    )
                else:
                    init.content.controls[0].content.controls[0].controls[1].opacity=1
                    init.content.controls[0].content.controls[1].height=0
                    init.content.controls[0].content.controls[1].content=ft.Text("")

                page.update()
                e.control.update()

            def change_bg(e):
                if e.control.data=="min_but": #Processo para realizar o carrossel de fotos tutoriais
                    if main.num<=1: 
                        main.num=4
                    else:
                        main.num-=1
                else:
                    if main.num>=4:
                        main.num=1
                    else:
                        main.num+=1
                #print(main.num)

                match main.num:
                    case 1:
                        init.content.controls[0].content=ft.Row(
                                                            alignment=ft.MainAxisAlignment.CENTER,
                                                            spacing=5,
                                                            width=page.window.width/2,
                                                            height=page.window.height-60,
                                                            controls=[
                                                                ft.Image(
                                                                    src=os.path.join(imgs_folder,"Tela_what.png")
                                                                ),
                                                                ft.Container(
                                                                    width=page.window.width/2-10,
                                                                    height=page.window.height-60,
                                                                    content=ft.Text(
                                                                        value="Ao utilizar o aplicativo pela primeira vez você irá se deparar com a tela de login apresentada na imagem. Essa tela se deve ao fato de que o aplicativo utiliza novos arquivos do navegador para realizar o processo de abertura do Whatsapp.\nRealize o login de forma normal e, logo após, feche a janela do navegador para evitar possíveis problemas.\nFique tranquilo, esse processo será necessário somente uma vez.",
                                                                        size=12,
                                                                        text_align=ft.TextAlign.JUSTIFY
                                                                    ),
                                                                    bgcolor=ft.colors.WHITE10,
                                                                    border_radius=ft.border_radius.all(5),
                                                                    padding=5,
                                                                    alignment=ft.alignment.center
                                                                )
                                                            ]
                        )
                    case 2:
                        init.content.controls[0].content=ft.Stack(
                                                            width=page.window.width,
                                                            controls=[
                                                                ft.Stack(
                                                                        controls=[
                                                                                ft.Image(
                                                                                    width=page.window.width,
                                                                                    height=page.window.height,
                                                                                    src=os.path.join(imgs_folder,"Pastas_essenc.png"),
                                                                                    fit=ft.ImageFit.FILL
                                                                                ),
                                                                                ft.Container(
                                                                                    width=30,
                                                                                    height=30,
                                                                                    content=ft.Icon(
                                                                                        name=ft.Icons.INFO_OUTLINED,
                                                                                        color=ft.colors.BLACK
                                                                                    ),
                                                                                    bgcolor=ft.colors.WHITE24,
                                                                                    right=page.window.width/2-25,
                                                                                    bottom=5,
                                                                                    border_radius=ft.border_radius.all(5),
                                                                                    animate=ft.animation.Animation(600, "bouceOut"),
                                                                                    animate_position=ft.animation.Animation(600, "bouceOut"),
                                                                                    on_animation_end=but_animat_end,
                                                                                    alignment=ft.alignment.center,
                                                                                    on_hover=hover_but_inf,
                                                                                    on_click=inf_container_show,
                                                                                    data="inf_but2"
                                                                                )
                                                                        ]
                                                                ),
                                                                ft.Container(
                                                                    width=page.window.width,
                                                                    height=0,
                                                                    bottom=0,
                                                                    bgcolor=ft.colors.WHITE60,
                                                                    animate=ft.animation.Animation(600, "bouceOut"),
                                                                    alignment=ft.alignment.center_left
                                                                )
                                                            ]
                        )
                    case 3:
                        init.content.controls[0].content=ft.Stack(
                                                            width=page.window.width,
                                                            controls=[
                                                                ft.Stack(
                                                                        controls=[
                                                                                ft.Image(
                                                                                    width=page.window.width,
                                                                                    height=page.window.height,
                                                                                    src=os.path.join(imgs_folder,"Desktop.png"),
                                                                                    fit=ft.ImageFit.FILL
                                                                                ),
                                                                                ft.Container(
                                                                                    width=30,
                                                                                    height=30,
                                                                                    content=ft.Icon(
                                                                                        name=ft.Icons.INFO_OUTLINED,
                                                                                        color=ft.colors.BLACK
                                                                                    ),
                                                                                    bgcolor=ft.colors.WHITE24,
                                                                                    right=page.window.width/2-25,
                                                                                    bottom=5,
                                                                                    border_radius=ft.border_radius.all(5),
                                                                                    animate=ft.animation.Animation(600, "bouceOut"),
                                                                                    animate_position=ft.animation.Animation(600, "bouceOut"),
                                                                                    on_animation_end=but_animat_end,
                                                                                    alignment=ft.alignment.center,
                                                                                    on_hover=hover_but_inf,
                                                                                    on_click=inf_container_show,
                                                                                    data="inf_but3"
                                                                                )
                                                                        ]
                                                                ),
                                                                ft.Container(
                                                                    width=page.window.width,
                                                                    height=0,
                                                                    bottom=0,
                                                                    bgcolor=ft.colors.WHITE60,
                                                                    animate=ft.animation.Animation(600, "bouceOut"),
                                                                    alignment=ft.alignment.center_left
                                                                )
                                                            ]
                        )
                    case 4:
                        init.content.controls[0].content=ft.Stack(
                                                            width=page.window.width,
                                                            controls=[
                                                                ft.Stack(
                                                                        controls=[
                                                                                ft.Image(
                                                                                    width=page.window.width,
                                                                                    height=page.window.height,
                                                                                    src=os.path.join(imgs_folder,"Fim_tutorial.png")
                                                                                )
                                                                        ]
                                                                )
                                                            ]
                        )
                page.update()

            page.window.width=500
            page.window.height=300
            page.window.resizable=False
            page.window.icon=os.path.join(imgs_folder,"whatsapp.ico")
            page.title="Tutorial inicial"
            page.window.alignment=ft.alignment.center

            but1=ft.ElevatedButton(
                        content=ft.Icon(
                                name=ft.Icons.ARROW_BACK_ROUNDED,
                                size=40,
                                color=ft.colors.RED,
                                opacity=0.6
                        ),
                        width=60,
                        height=100,
                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                            shadow_color=ft.colors.TRANSPARENT,
                                            overlay_color=ft.colors.TRANSPARENT,
                                            alignment=ft.alignment.center_left
                                    ),
                        bgcolor=ft.colors.TRANSPARENT,
                        on_hover=change_button,
                        on_click=change_bg,
                        data="min_but",
            )

            but2=ft.ElevatedButton(
                        content=ft.Icon(
                                name=ft.Icons.ARROW_FORWARD_ROUNDED,
                                size=40,
                                color=ft.colors.GREEN,
                                opacity=0.6
                        ),
                        width=60,
                        height=100,
                        style=ft.ButtonStyle(
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                            shadow_color=ft.colors.TRANSPARENT,
                                            overlay_color=ft.colors.TRANSPARENT,
                                            alignment=ft.alignment.center_right
                                    ),
                        bgcolor=ft.colors.TRANSPARENT,
                        on_hover=change_button,
                        on_click=change_bg,
                        data="mor_but"
            )

            msg_init=ft.Image(
                width=page.window.width,
                src=os.path.join(imgs_folder,"Init.png"),
                scale=0.9
            )

            init=ft.Container(
                    width=page.window.width,
                    height=page.window.height-50,
                    content=ft.Stack(
                                controls=[
                                        ft.Container(
                                            width=page.window.width,
                                            height=page.window.height-50,
                                            content=msg_init
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            spacing=0,
                                            width=page.window.width-20,
                                            height=page.window.height,
                                            controls=[
                                                but1,
                                                but2,
                                            ]
                                        )
                                ]
                    ),
                    bgcolor=ft.colors.WHITE10,
                    margin=-5,
                    border_radius=ft.border_radius.all(5)
                )

            page.add(init)
        ft.app(main)


    #----------------------------------------------------------------------------------
    #Estrutura do código

    config()

    opt=webdriver.EdgeOptions()
    opt.add_argument(f"--user-data-dir={prog_inicial.Nav_config}") #Definir local para salvar as configurações definidas ao navegador
    opt.add_experimental_option("detach",True)

    nav=webdriver.ChromiumEdge(options=opt)
    nav.get("https://web.whatsapp.com")

    tutorial_func()

def prog_principal():
    #----------------------------------------------------------------------------------
    #Definição do dia atual
    list_date=str(datetime.date.today()).split("-")
    prog_principal.day_today=list_date[2]
    if int(prog_principal.day_today)>=10:
        prog_principal.day_cons=prog_principal.day_today
    else:
        prog_principal.day_cons="0"+str(int(prog_principal.day_today)+1)
    prog_principal.month=list_date[1]
    prog_principal.year=list_date[0]
    print(int(list_date[2]))
    #print(prog_principal.day,prog_principal.month,prog_principal.year)

    #--------------------------

    #--------------------------
    #Funções

    def Row_cons(mes_inf): #Função que define em quais linhas da sheet analizada contém consultas para o dia seguinte
        row_cons=list()
        book_ncons=len(mes_inf["B"]) #Número de consultas existentes no mês
        for i in range(2,book_ncons+1):
            cell=str(mes_inf.cell(row=i,column=2).value)
            print(cell)
            print(f"{prog_principal.day_cons}.{prog_principal.month}.{prog_principal.year}")
            if cell==f"{prog_principal.day_cons}.{prog_principal.month}.{prog_principal.year}":
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
        last_open_file=os.path.join(r"C:\Python\Bot_Whatsapp","last_open.txt")
        with open(last_open_file,"w") as arq:
            arq.write(f"{prog_principal.day_today}.{prog_principal.month}.{prog_principal.year}")

    def check_last(): #Função responsável por verificar se o programa já foi aberto no dia
        last_open_file=os.path.join(r"C:\Python\Bot_Whatsapp","last_open.txt")
        att_day=f"{prog_principal.day_today}.{prog_principal.month}.{prog_principal.year}"
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
            page.window.icon=os.path.join(fr"{os.path.dirname(os.path.abspath(__file__))}\Img","whatsapp.ico")
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
    print(row_cons)

    day_consult=Infs(row_cons) #Função que define uma lista que contêm as consultas que ocorrerão no dia seguindo o padrão (paciente,médico,telefone)
    print(day_consult)

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
        msg=f"Bom dia, *{inf["Paciente"]}*. Tudo bem? Espero que sim. Passando para lembrar que sua consulta com o(a) doutor(a) *{inf["Médico"]}* está marcada para amanhã, *{prog_principal.day_cons} de {month_str[int(prog_principal.month)+1]}*. Qualquer dúvida estou a disposição!!"
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
    if os.path.exists(os.path.join(r"C:\Python\Bot_Whatsapp","last_open.txt")):
        with open(os.path.join(r"C:\Python\Bot_Whatsapp","last_open.txt"),"w") as arq:
            arq.write("")
    else:
        prog_inicial()
else:
    prog_principal()