proceeds = float(input("Введите сумму выручки за месяц в рублях: "))
expenses = float(input("ВВедите сумму расходов за месяц в рублях: "))
if proceeds < expenses:
    dif = expenses - proceeds
    print("Расходы превышают выручкy на: ", dif, " рублей")
elif proceeds > expenses:
    costeff = proceeds / expenses
    print("Доход превышает расходы. Ренатабельность за месяц составила: " f'{costeff:.2f}')
    empnum = int(input("Введите количество сотрудников: "))
    income = proceeds - expenses
    empincome = income / empnum
    print ("Доход на одного сотрудника в месяце составил:", f'{empincome:.2f}')
elif proceeds == expenses:
    print("Доходы равны расходам")