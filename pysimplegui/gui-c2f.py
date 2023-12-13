import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [
        [sg.Text('Celcius to Farenheit')],
        [sg.Text('Enter value for Celcius'), sg.InputText()],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]

window = sg.Window('Converter', layout)

def celcius2farenheit(celcius):
    celcius = float(celcius)
    return (celcius * (9/5)) + 32

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    celcius = values[0]
    farenheit = celcius2farenheit(celcius)
    print('You entered', celcius)
    popup_text = ("%s Celcius = %s Farenheit" % (celcius, farenheit))
    sg.popup(popup_text)

window.close()
