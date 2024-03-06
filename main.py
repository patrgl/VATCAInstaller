from GitHubDownloader import Downloader
import PySimpleGUI as sg


##get files from github
def install_main(dest_path):
    try:
        downloader = Downloader("https://github.com/patrgl/VATCA")
        downloader.download(dest_path + "/VATCA","*",True)
        window["Download"].update(visible=False)
        window['-FEEDBACK-'].update("Download Complete!", visible=True, text_color='#62f202')
    except:
        window['-FEEDBACK-'].update("Download Failed!", visible=True, text_color='red')
        pass

##columns

middle = [
    [sg.In(size=(25,1), enable_events=True, expand_y=True, key='-FOLDER-'), sg.FolderBrowse(button_color=('#DCDCDC', '#656565'))],
    [sg.Button("Download", visible=False, button_color=('#DCDCDC', '#656565')), sg.Text("", text_color='#DCDCDC', background_color='#3B3B3B', key='-FEEDBACK-', font=('Helvetica', 18))],
]

bottom = [
    [sg.Text("v1.0", text_color='#DCDCDC', font=('Helvetica', 12), background_color='#3B3B3B')]
]

layout = [
    [sg.VPush(background_color='#3B3B3B')],
    [sg.Column(middle, background_color='#3B3B3B')],
    [sg.VPush(background_color='#3B3B3B')],
    [sg.Column(bottom, element_justification="right", background_color='#3B3B3B')],
]

##options
sg.set_options(font=('Helvetica', 18))
sg.set_options(button_color=('#DCDCDC', '#656565'))
sg.set_options(border_width='0')
sg.set_options(text_element_background_color='#3B3B3B')
sg.set_options(element_background_color='#3B3B3B')

window = sg.Window("VATCA Installer", layout, element_justification='center', background_color='#3B3B3B', resizable=True, size=(800,400))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: #user closes window
        break
    if event == '-FOLDER-':
        window['-FEEDBACK-'].update("")
        folder = values['-FOLDER-']
        if folder != "":
            window["Download"].update(visible=True)
    if event == "Download" and values['-FOLDER-'] != "":
        install_main(folder)
    if event == "Download" and values['-FOLDER-'] == "":
        window["Download"].update(visible=False)
        window['-FEEDBACK-'].update("Destination Path is Empty!", visible=True, text_color='orange')