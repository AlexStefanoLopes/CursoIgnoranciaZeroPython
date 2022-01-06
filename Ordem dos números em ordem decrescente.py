num = int(input('Primeiro numero:'))
num1 = int(input('Segundo numero:'))
num2 = int(input('terceiro numero:'))

if num > num1 > num2:
    print(num, num1, num2)
elif num1 > num > num2:
    print(num1, num, num2)
elif num2 > num > num1:
    print(num2, num, num1)