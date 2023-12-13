import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [
        [sg.Text('Farenheit to Celcius')],
        [sg.Text('Enter value for Farenheit'), sg.InputText()],
        [sg.Button('OK'), sg.Button('Cancel')]
    ]

window = sg.Window('Converter', layout)

def farenheit2celcius(farenheit):
    farenheit = float(farenheit)
    return (farenheit - 32) * (5/9)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    farenheit = values[0]
    celcius = farenheit2celcius(farenheit)
    print('You entered', farenheit)
    popup_text = ("%s Farenheit = %s Celcius" % (farenheit, celcius))
    sg.popup(popup_text)

window.close()
