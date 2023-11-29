print("COMPANY NAME ABCXYZ PAYROLL PROGRAM")
# WTAX 14%
# PhilHealth 4% https://sprout.ph/blog/philhealth-new-contribution-rates/
# SSS 4.5% (Employee Share) https://www.sss.gov.ph/sss/DownloadContent?fileName=2023-Schedule-of-Contributions.pdf
# PAGIBIG 2% https://sprout.ph/blog/how-to-calculate-your-hdmf-contribution/

full_name = input("Enter your complete name: ")
hours_worked = float(input("Enter total hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
gross_pay = hours_worked * hourly_rate
# deductions
tax_deduction = gross_pay * 0.14
philhealth_deduction = gross_pay * 0.04
pagibig_deduction = gross_pay * 0.02
sss_deduction = gross_pay * 0.045
total_deductions = tax_deduction + philhealth_deduction + pagibig_deduction + sss_deduction
# net pay (take home pay)
net_pay = gross_pay - total_deductions

pay_date = input("Enter pay date (e.g., YYYY-MM-DD): ")
# Write data to a file
with open("payroll_data.txt", "w") as file:
    file.write(f"Pay Date: {pay_date}\n")
    file.write(f"Name: {full_name}\n")
    file.write(f"Total Hours Worked: {hours_worked} hours\n")
    file.write(f"Hourly Rate: PHP {hourly_rate:.2f}\n")
    file.write(f"Gross Pay: PHP {gross_pay:.2f}\n")
    file.write(f"Tax Deduction: PHP {tax_deduction:.2f}\n")
    file.write(f"PhilHealth Deduction: PHP {philhealth_deduction:.2f}\n")
    file.write(f"Pag-IBIG Deduction: PHP {pagibig_deduction:.2f}\n")
    file.write(f"SSS Deduction: PHP {sss_deduction:.2f}\n")
    file.write(f"Net Pay: PHP {net_pay:.2f}\n")
    file.write("=" * 30 + "\n")

print("Payroll data has been saved to payroll_data.txt.")
