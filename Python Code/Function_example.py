def SalaryCalculator():
     tax = 27.
     while tax > 0.:
         tax = input('Imposto ou (s) sair: ')
         if not tax:
             tax = 27.
         elif tax == "s":
             break
         else:
             tax = float(tax)
         print('Valor final: {0}'.format(salary - (salary * tax*0.01)))


salary = int(input('Salary: '))

SalaryCalculator()