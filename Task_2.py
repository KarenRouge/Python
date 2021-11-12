time = int(input("Введите время в секундах: "))
minutes = int(time / 60)
secundes = int(time - minutes * 60)
hours = int(minutes / 60)
minutes2 = int(time - hours * 3600 - secundes) / 60
minutes2 == float(minutes2)
i = 10
if hours > i and minutes2 > i and secundes > i:
    print('Время в чч:мм:сc : ', f'{hours}:{int(minutes2)}:{secundes}')

elif hours > i and minutes2 <= i and secundes <= i:
    print('Время в чч:мм:сc : ', f'{hours}:0{int(minutes2)}:0{secundes}')

elif hours > i and minutes2 > i and secundes <= i:
    print('Время в чч:мм:сc : ', f'{hours}:{int(minutes2)}:0{secundes}')

elif hours <= i and minutes2 > i and secundes > i:
    print('Время в чч:мм:сc : 0' f'{hours}:{int(minutes2)}:{secundes}')

elif hours <= i and minutes2 <= i and secundes > i:
    print('Время в чч:мм:сc : 0' f'{hours}:0{int(minutes2)}:{secundes}')
elif hours > i and minutes2 <= i and secundes > i:
    print('Время в чч:мм:сc : ' f'{hours}:0{int(minutes2)}:{secundes}')
else:
    print('Время в чч:мм:сc : 0', f'{hours}:0{int(minutes2)}:0{secundes}')
