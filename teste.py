import flet as ft
import os
from time import sleep
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

    def but_animat_end(e):
        if e.control.width==30:
            e.control.content=ft.Icon(
                                    name=ft.Icons.INFO_OUTLINED,
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

    def inf_container(e):
        e.control.disabled=True
        e.control.opacity=0
        init.content.controls[0].content.controls[1].height=page.window.height-50
        init.content.controls[0].content.controls[1].content=ft.Image(
                                                                width=page.window.width,
                                                                src=os.path.join(imgs_folder,"exp_page2.png"),
                                                                scale=0.8,
                                                            )
        page.update()
        e.control.update()

    def change_bg(e):
        if e.control.data=="min_but": #Processo para realizar o carrossel de fotos tutoriais
            if main.num<=1: 
                main.num=3
            else:
                main.num-=1
        else:
            if main.num>=3:
                main.num=1
            else:
                main.num+=1
        #print(main.num)

        match main.num:
            case 2:
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
                page.update()
            case 1:
                init.content.controls[0].content=ft.Stack(
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
                                                                            on_click=inf_container
                                                                        )
                                                                ]
                                                        ),
                                                        ft.Container(
                                                            width=page.window.width,
                                                            height=0,
                                                            bottom=0,
                                                            bgcolor=ft.colors.WHITE60,
                                                            animate=ft.animation.Animation(600, "bouceOut"),
                                                            alignment=ft.alignment.bottom_right
                                                        )
                                                    ]
                )
                page.update()
            case 3:
                init.content.controls[0].content=ft.Stack(
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
                                                                            on_click=inf_container
                                                                        )
                                                                ]
                                                        ),
                                                        ft.Container(
                                                            width=page.window.width,
                                                            height=0,
                                                            bottom=0,
                                                            bgcolor=ft.colors.WHITE60,
                                                            animate=ft.animation.Animation(600, "bouceOut"),
                                                        )
                                                    ]
                )
                page.update()

    page.window.width=500
    page.window.height=300
    page.window.resizable=False
    page.window.icon=os.path.join(os.path.dirname(os.path.abspath(__file__)),"whatsapp.ico")
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