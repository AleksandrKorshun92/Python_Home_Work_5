#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#Первый вариант - через цикл
'''def stepen_number(a,b):
    c = 1
    stepen = a
    while b>c:
        stepen = stepen * a
        c+=1
    print(stepen)

a = int(input("first number "))
b = int(input("second number "))
stepen_number(a,b)
'''
#Второй вариант - рекурсию
'''def stepen_number(a,b):
    if b == 1:
        return a
    if b != 1:
        return (a*stepen_number(a, b - 1))
   
a = int(input("first number "))
b = int(input("second number "))
stepen_number(a,b)
print(stepen_number(a,b))
'''
#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a,b):
    if a <=0:
        return b
    else:
        return sum(a - 1, b + 1)
a = int(input("first number "))
b = int(input("second number "))
print(sum(a,b))