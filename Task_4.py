n = int(input('Введите целое положительное число:'))
number = n % 10
n = n//10
while n > 0:
    if n % 10 > number:
        number = n%10
    n = n // 10
print("Наибольшая цифра:", number)



