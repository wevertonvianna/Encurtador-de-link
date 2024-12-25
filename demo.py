import pyshorteners # type: ignore
import PySimpleGUI as sg

# Tema da interface
sg.theme("Dark Blue 16")

# Layout da interface
interface = [
    [sg.Titlebar("Encurtador de link", icon=None, background_color="black")],
    [sg.Text("link:", size=(10, 1)), sg.Input(key="url", size=(50, 1))],
    [sg.Text("link curto", size=(10, 1)),sg.Text(key="link_curt", size=(50, 1)),sg.Button("Copiar", key="copy")],
    [sg.Button("converter", size=(10, 1))],
]
# Criação da janela
janela = sg.Window("Encurtador de link", interface)

while True:
    eventos, valores = janela.read()

    # Fechar a janela
    if eventos == sg.WINDOW_CLOSED:
        break
    
    # Evento de baixar
    if eventos == "converter":
        linkgrande = valores["url"]
        try:
            # Converter o link
            type_tiny = pyshorteners.Shortener()
            link_curt = type_tiny.tinyurl.short(linkgrande)
            janela["link_curt"].update(link_curt)
        except:
            sg.popup_error("Erro ao fazer a conversão:", linkgrande)
    if eventos == "copy":
        try:
            sg.clipboard_set(link_curt)
            sg.popup("Link copiado com sucesso!")
        except:
            sg.popup("Erro ao copiar o link", link_curt)