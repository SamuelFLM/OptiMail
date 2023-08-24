import PySimpleGUI as sg


def _front():
    FONT_TITULO = "inter 14"
    COLOR_TITULO = "#383838"
    BACKGROUND_COLOR = "WHITE"

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
                pad=(40, (0, 0)),
                expand_x=True,
            )
        ],
        [
            sg.Input(
                "",
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
            sg.FileBrowse(
                "Anexar",
                pad=(0, (0, 0)),
                button_color=("#142918", "#4BED13"),
                font="inter 10 bold",
                auto_size_button=True,
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


_front()
