import PySimpleGUI as sg
import threading
from utilities  import text_to_audio

sg.theme('Topanga')

layout = [
    [sg.Text('Clique no botão Browse para escolha quais arquivos seram convertidos')],
    [sg.Input(key='Arquivos', size=(49,1)), sg.FilesBrowse(target='Arquivos', file_types=(('Arquivos de texto','*.txt'),))],
    [sg.Button('Converter')],
    [sg.Output(size=(49,3), key='Atualizacao')]
]

window = sg.Window('Convertendo para áudio', layout)

def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == 'Converter':
            window['Converter'].update(disabled=True)
            funcao = threading.Thread(target=text_to_audio, args=(window,values['Arquivos'],'pt-br'),daemon=True)
            funcao.start()
        elif event == 'Finalizado':
            funcao.join()
            window['Converter'].update(disabled=False)
            window['Arquivos'].update('')
            print(values['Finalizado'])
        elif event == 'erro':
            window['Converter'].update(disabled=False)
            window['Arquivos'].update('')
            sg.popup_error('Arquivo não encontrado!!')
            window['Atualizacao'].update('')

if __name__ == '__main__':
    main()