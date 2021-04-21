#. 5. Вычислить сумму четных чисел и произведение нечетных в заданном диапазоне.

# start = int(input())
# end = int(input())
# sum = 0
# proizv = 1
#
#
# for i in range(start, end):
#     if i % 2 == 0:
#         sum += i
#     else:
#         proizv *= i
# print('Summa', sum)
# print('Proizvedenie', proizv)

#6. Вывести на экран все числа, кратные 3, в диапазоне от 0 до 100
#
# for i in range(1,100):
#     if i % 3 == 0:
#         print(i, end=' ')

#7. Написать программу, вычисляющую факториал введѐнного числа

# a = int(input())
# x = 1
#
# for i in range(1, a +1):
#     x *= i
# print(x)

#8. Написать программу, вычисляющую степень числа.

# a = int(input())
# b = int(input())
# x = 1
#
# for i in range(10):
#     x = a * x
# print(x)

#11. С клавиатуры вводится целое число. Вывести на экран все числа, на которые введѐнное число делится без остатка.

# a = int(input())
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i)
