#Напишите функцию, которая принимает в качестве аргумента шестизначное число и возвращает True, если оно является счастливым, и False в противном случае.
# #Счастливым называется шестизначное число, сумма первых трех цифр которого равна сумме последних трех цифр.
#
# def sum_digit(n):
#
#     if n < 6:
#         return n
#     else:
#         return n % 10 + sum_digit(n // 10)
#
#
# def detect_lucky(n):
#     if n < 100000:
#         return False
#     else:
#         return sum_digit(n % 1000) == sum_digit(n // 1000)
#
#
# print(detect_lucky(321123))
# print(detect_lucky(321453))