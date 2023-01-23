# 2
def get_name():
    temp_name = input("Enter employee name: ")
    return temp_name


# 3
def get_total_hours():
    temp_total_hours = input('Enter amount of hours worked: ')
    return temp_total_hours


# 4
def get_hourly_rate():
    temp_hourly_rate = input('Enter hourly rate: ')
    return temp_hourly_rate


# 5
def get_income_tax_rate():
    temp_income_tax_rate = input('Enter tax rate: ')
    return temp_income_tax_rate


# 6
def calculate_payroll(total_hours,hourly_rate,income_tax_rate):
    temp_gross_pay = float(total_hours) * float(hourly_rate)

    temp_tax_rate = float(income_tax_rate) * 100
    temp_tax_calc = float(income_tax_rate) * temp_gross_pay
    temp_net_pay = temp_gross_pay - temp_tax_calc
    return temp_gross_pay, temp_tax_rate, temp_tax_calc, temp_net_pay


#7
def print_info(name, total_hours, hourly_rate, gross_pay, tax_rate, tax_calc, net_pay):
    print('Name: ' + name)
    print('Hours Worked: %.2f' % float(total_hours))
    print('Hourly Rate: %.2f' % float(hourly_rate))
    print('Gross Pay: %.2f' % float(gross_pay))
    print('Tax Rate: ' + str(tax_rate) + '%')
    print('Income Tax: %.2f' % float(tax_calc))
    print('Net Pay: %.2f' % float(net_pay))


#8
def print_all_info(number_of_employees, total_hours_worked, total_gross_pay, total_income_tax_rate, total_net_pay):
    print("Total Number of Employees: " + str(number_of_employees))
    print("Total Hours Worked: " + str(total_hours_worked))
    print("Total Gross Pay: %.2f" % float(total_gross_pay))
    print("Total Income Tax: %.2f" % float(total_income_tax_rate))
    print("Total Net Pay: %.2f" % float(total_net_pay))
    print('Press any key to continue . . . ')


if __name__ == "__main__":
    total_employee_count = 0
    total_hours_worked = 0
    total_gross_pay = 0
    total_income_tax_rate = 0
    total_net_pay = 0

    condition = True
    # 1
    while condition:
        name = get_name()
        if name.lower() == 'end':
            print_all_info(total_employee_count, total_hours_worked, total_gross_pay, total_income_tax_rate, total_net_pay)
            condition = False
        else:
            total_hours = get_total_hours()
            hourly_rate = get_hourly_rate()
            income_tax_rate = get_income_tax_rate()
            gross_pay, tax_rate, tax_calc, net_pay = calculate_payroll(total_hours, hourly_rate, income_tax_rate)
            print_info(name, total_hours, hourly_rate, gross_pay, tax_rate, tax_calc, net_pay)
            total_employee_count = total_employee_count + 1
            total_hours_worked = total_hours_worked + float(total_hours)
            total_gross_pay = total_gross_pay + float(gross_pay)
            total_income_tax_rate = total_income_tax_rate + float(tax_calc)
            total_net_pay = total_net_pay + float(net_pay)

