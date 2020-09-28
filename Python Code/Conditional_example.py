# Salary tax calculator

# Variables

salary = int(input('Salary: '))
tax = input('Tax value: ')

# Salary calculator with tax

if not tax:
    tax = 27.5
else:
    tax = float(tax)

# Net Salary

netSalary = salary - (salary * (tax * 0.01))
print(netSalary)