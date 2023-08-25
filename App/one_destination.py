import PySimpleGUI as sg
import re
import shutil
import os
import smtplib
from email.message import EmailMessage
from time import sleep
import imghdr
import pyautogui as bot
import webbrowser

def _main():
    if os.path.exists("arq.png"):
        os.remove("arq.png")

    FONT_TITULO = "inter 14"
    COLOR_TITULO = "#383838"
    BACKGROUND_COLOR = "WHITE"
    EMAIL_ADDRESS = "contatosamudev@gmail.com"
    EMAIL_PASSWORD = "llwgttnqhgjwcgmu"

    tela_notificacao = [
        sg.Image(
            filename="Img\\barra de notificacao.png",
            background_color=BACKGROUND_COLOR,
            pad=(0, (0, 0)),
        )
    ]
    ajudar = [
        sg.Text("", background_color=BACKGROUND_COLOR, pad=(170, (30, 0))),
        sg.Image(
            filename="Img\\ajudar.png",
            background_color=BACKGROUND_COLOR,
            pad=(0, (30, 0)),
            enable_events=True,
            key="ajudar",
        ),
    ]
    destinatario = [
        [
            sg.Text(
                "Destinatário",
                font=FONT_TITULO,
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                justification="l",
                key="title_Destinatario",
                pad=(40, (0, 0)),
                expand_x=True,
            )
        ],
        [
            sg.Input(
                "a@gmail.com",
                focus=True,
                expand_x=True,
                justification="l",
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                pad=(43, (15, 0)),
                key="destinatario",
                font="inter 11 bold",
                border_width=0,
            )
        ],
        [sg.HSep(pad=(43, (0, 40)))],
    ]
    titulo = [
        [
            sg.Text(
                "Titulo",
                font=FONT_TITULO,
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                justification="l",
                pad=(40, (0, 0)),
                expand_x=True,
            )
        ],
        [
            sg.Input(
                "",
                expand_x=True,
                justification="l",
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                pad=(43, (15, 0)),
                key="titulo",
                font="inter 11 bold",
                border_width=0,
            )
        ],
        [sg.HSep(pad=(43, (0, 20)))],
    ]
    mensagem = [
        [
            sg.Text(
                "Mensagem",
                font=FONT_TITULO,
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                justification="l",
                pad=(40, (0, 20)),
                expand_x=True,
            )
        ],
        [
            sg.Multiline(
                "",
                expand_x=True,
                justification="l",
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                pad=(43, (0, 20)),
                size=(20, 20),
                k="mensagem",
                sbar_arrow_width=0,
                sbar_background_color="black",
                sbar_arrow_color="black",
                sbar_width=0,
                border_width=0.5,
            )
        ],
    ]
    anexo = [
        [
            sg.Text(
                "Anexo",
                font=FONT_TITULO,
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                justification="l",
                pad=(40, (0, 0)),
                expand_x=True,
            )
        ],
        [
            sg.Input(
                "",
                expand_x=True,
                justification="l",
                background_color=BACKGROUND_COLOR,
                text_color=COLOR_TITULO,
                pad=(43, (15, 0)),
                key="anexo",
                font="inter 11 bold",
                border_width=0,
                disabled=True,
                disabled_readonly_background_color=BACKGROUND_COLOR,
                disabled_readonly_text_color=COLOR_TITULO,
                s=(15, 10),
            ),
            sg.Image(
                filename="Img\\anexo.png",
                background_color=BACKGROUND_COLOR,
                pad=(0, (0, 0)),
                enable_events=True,
                k="btn_anexo",
                size=(0, 0),
            ),
            sg.Text(
                "",
                background_color=BACKGROUND_COLOR,
                pad=(20, (0, 0)),
            ),
        ],
        [sg.HSep(pad=(43, (0, 20)))],
    ]
    rodape = [
        sg.Image(
            filename="Img\\enviaroff.png",
            background_color=BACKGROUND_COLOR,
            pad=(50, (0, 0)),
            enable_events=True,
            key="enviar",
        )
    ]

    layout = [tela_notificacao, ajudar, destinatario, titulo, mensagem, anexo, rodape]

    window = sg.Window(
        "OptiMail",
        layout=layout,
        size=(390, 840),
        margins=(0, 0),
        background_color="white",
        icon="Img\\logo.ico",
    )

    while True:
        event, values = window.read(timeout=1)

        if event == sg.WIN_CLOSED:
            break
        destinatario = values["destinatario"]
        titulo = str(values["titulo"]).strip()
        mensagem = str(values["mensagem"]).strip()
        anexo = str(values["anexo"]).strip()
        validar_email(window, destinatario)

        if event == "btn_anexo":
            file = sg.popup_get_file("", no_window=True, icon="Img\\logo.ico")
            window["anexo"].update(file)
        if event == 'ajudar':
            webbrowser.open_new_tab("https://github.com/samuelflm")
        if bool(destinatario) and bool(titulo) and bool(mensagem) and bool(anexo):
            window["enviar"].update(filename="Img\\enviaron.png")
            if event == "enviar":
                mail = EmailMessage()
                mail["Subject"] = titulo
                mail["From"] = EMAIL_ADDRESS
                mail["To"] = destinatario
                mail.add_header("Content-Type", "text/html")
                mail.set_payload(mensagem.encode("utf-8"))
                if bool(anexo) and anexo[-4] in ".png":
                    nome_arquivo = f"arq.png"
                    shutil.copy2(anexo, nome_arquivo)
                    with open(nome_arquivo, 'rb') as arquivo:
                        dados = arquivo.read()
                        extensao_imagem = imghdr.what(arquivo.name)
                        nome_arquivo = arquivo.name
                        mail.add_attachment(dados, maintype='imagem', subtype=extensao_imagem, filename=nome_arquivo)
                else: pass 
                #Fazer parte de anexar arquivos
                    # shutil.copy2(anexo, anexo)
                    # with open(anexo, 'rb') as arquivo:
                    #     dados = arquivo.read()
                    #     extensao_imagem = imghdr.what(arquivo.name)
                    #     anexo = arquivo.name
                    #     mail.add_attachment(dados, maintype='imagem', subtype=extensao_imagem, filename=anexo)
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as email:
                    email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    email.send_message(mail)
                    sleep(1)
                    bot.confirm(title="ENVIADO", text="E-MAIL ENVIADO COM SUCESSO!", buttons=['OK'])
                    
        else:
            window["enviar"].update(filename="Img\\enviaroff.png")


def validar_email(window, email):
    padrao = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,3}$"
    resultado = re.match(padrao, email)
    if bool(resultado):
        window["title_Destinatario"].update("Destinatário", text_color="#383838")
        return True
    else:
        window["title_Destinatario"].update("*Erro", text_color="red")
