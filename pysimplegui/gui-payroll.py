import PySimpleGUI as sg

WTAX_RATE = 0.14        # 14%
PHILHEALTH_RATE = 0.04  # 4
PAGIBIG_RATE = 0.02     # 2%
SSS_RATE = 0.045        # 4.5%

def compute_gross_pay(hours, rate):
    return rate * hours


def compute_tax_deduction(gross_amount):
    return WTAX_RATE * gross_amount


def compute_philhealth_deduction(gross_amount):
    return PHILHEALTH_RATE * gross_amount


def compute_pagibig_deduction(gross_amount):
    return PAGIBIG_RATE * gross_amount


def compute_sss_deduction(gross_amount):
    return SSS_RATE * gross_amount


def compute_total_deductions(gross_amount):
    deductions = compute_tax_deduction(gross_amount)
    deductions += compute_philhealth_deduction(gross_amount)
    deductions += compute_pagibig_deduction(gross_amount)
    deductions += compute_sss_deduction(gross_amount)
    return deductions


def compute_net_pay(gross_amount):
    net_amount = gross_amount - compute_total_deductions(gross_amount)
    return net_amount


layout = [
        [sg.Text('Company Name ABCXYZ GUI Payroll Program')],
        [sg.Text('Full Name'), sg.InputText(key='FullName')],
        [sg.Text('Hours Worked'), sg.InputText(key='HoursWorked')],
        [sg.Text('Rate'), sg.InputText(key='Rate')],
        [
            sg.Text('Pay Date', size=(15,1)),
            sg.InputText(key='PayDate'),
            sg.CalendarButton(
                "Select Date",
                close_when_date_chosen=True,
                target='PayDate',
                format='%Y-%m-%d', size=(10,1)
            )
        ],
        [sg.Button('Compute Payroll'), sg.Button('Cancel')],
        [sg.Text('Gross Pay'), sg.InputText(key='GrossPay')],
        [sg.Text('Tax'), sg.InputText(key='TaxDeduction')],
        [sg.Text('PhilHealth'), sg.InputText(key='PhilHealthDeduction')],
        [sg.Text('PAGIBIG'), sg.InputText(key='PagibigDeduction')],
        [sg.Text('SSS'), sg.InputText(key='SssDeduction')],
        [sg.Text('Net Pay'), sg.InputText(key='NetPay')]
    ]

window = sg.Window('Payroll Calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    if event == 'Compute Payroll':
        name = values['FullName']
        hours_worked = float(values['HoursWorked'])
        rate = float(values['Rate'])
        pay_date = values['PayDate']
        gross_pay = compute_gross_pay(hours_worked, rate)
        tax_deduction = compute_tax_deduction(gross_pay)
        philhealth_deduction = compute_philhealth_deduction(gross_pay)
        pagibig_deduction = compute_pagibig_deduction(gross_pay)
        sss_deduction = compute_sss_deduction(gross_pay)
        net_pay = compute_net_pay(gross_pay)
        window['GrossPay'].update(gross_pay)
        window['TaxDeduction'].update(tax_deduction)
        window['PhilHealthDeduction'].update(philhealth_deduction)
        window['PagibigDeduction'].update(pagibig_deduction)
        window['SssDeduction'].update(sss_deduction)
        window['NetPay'].update(net_pay)

window.close()
