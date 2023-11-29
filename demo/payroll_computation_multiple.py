print("COMPANY NAME ABCXYZ PAYROLL PROGRAM")


employees =
    {
        'name': 'John Doe',
        'rate': 300,
        'hours_worked': 0,
        'gross_pay': 0,
        'tax_deduction': 0,
        'philhealth_deduction': 0,
        'pagibig_deduction': 0,
        'sss_deduction': 0,
        'net_pay': 0
    },
    {
        'name': 'Jane Doe',
        'rate': 400,
        'hours_worked': 0,
        'gross_pay': 0,
        'tax_deduction': 0,
        'philhealth_deduction': 0,
        'pagibig_deduction': 0,
        'sss_deduction': 0,
        'net_pay': 0
    },
    {
        'name': 'Jimmy Doe',
        'rate': 500,
        'hours_worked': 0,
        'gross_pay': 0,
        'tax_deduction': 0,
        'philhealth_deduction': 0,
        'pagibig_deduction': 0,
        'sss_deduction': 0,
        'net_pay': 0
    }
]


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


pay_date = input("Enter pay date (e.g., YYYY-MM-DD): ")

with open("payroll_data_multiple.txt", "a") as file:
    for employee in employees:
        print('Employee Name: ', employee['name'])
        employee['hours_worked'] = float(input("Enter total hours worked: "))
        employee['gross_pay'] = compute_gross_pay(employee['hours_worked'], employee['rate'])
        employee['tax_deduction'] = compute_tax_deduction(employee['gross_pay'])
        employee['philhealth_deduction'] = compute_philhealth_deduction(employee['gross_pay'])
        employee['pagibig_deduction'] = compute_pagibig_deduction(employee['gross_pay'])
        employee['sss_deduction'] = compute_sss_deduction(employee['gross_pay'])
        employee['net_pay'] = compute_net_pay(employee['gross_pay'])

        file.write(f"Pay Date: {pay_date}\n")
        file.write(f"Name: {employee['name']}\n")
        file.write(f"Total Hours Worked: {employee['hours_worked']} hours\n")
        file.write(f"Hourly Rate: PHP {employee['rate']:.2f}\n")
        file.write(f"Gross Pay: PHP {employee['gross_pay']:.2f}\n")
        file.write(f"Tax Deduction: PHP {employee['tax_deduction']:.2f}\n")
        file.write(f"PhilHealth Deduction: PHP {employee['philhealth_deduction']:.2f}\n")
        file.write(f"Pag-IBIG Deduction: PHP {employee['pagibig_deduction']:.2f}\n")
        file.write(f"SSS Deduction: PHP {employee['sss_deduction']:.2f}\n")
        file.write(f"Net Pay: PHP {employee['net_pay']:.2f}\n")
        file.write("=" * 30 + "\n")

print("Payroll data has been saved to payroll_data_multiple.txt.")
