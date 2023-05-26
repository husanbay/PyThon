# print("Hello World")

    # 25.05.2023
# a=[True, True, True, True]
# print (any(a))
# print (all(a))


# a= -5
# print (abs(a))


# a= -5
# b= abs (a) *2
# print (b)


# num = 3.43457997543
# print(round(num, 3 ))


# loan = float (input("ведите сумму займа"))
# protcent = 3.47
# total =loan * protcent / 100
# if loan >=50000:
#     print(round(total, 2))
# else:
#     print("ведите сумму больше 50000")


# setm =set()
# for i in range (5):
#     i = int(input("введите число: "))
#     setm. add(i)
# print(min(setm))


# try: 
#     a = int (input())
#     b = int (input())
#     print (a / b)
# except ZeroDivisionError:
#     print ("нельзя делить на ноль")


# try: 
#     print(10 + "10")
# except TypeError:
#     print ("нельзя сложить число на строку")


# values = ['a', 'b', (4, 5), 'c']
# convertibility = []
# for item in values:
    # try:
        # set(item)
        # convertibility.append(True)
    # except TypeError:

        # convertibility.append(False)
   
# can_convert = all(convertibility)
# print("Можно ли конвертировать values в SET?", can_convert)


# user_input = input("Введите Python функцию: ")

# try:
#     result = eval(user_input)
#     print("Результат выполнения функции", result)
# except NameError:
#     print("В Python такой фунции нет!")


# try:
#     my_list = [1, 2, 3]
#     print(my_list[9])
# except IndexError:          
#     print("такого индекса нету")

# while True:
#     try:
#         num1 = int(input())
#         a = input()
#         num2 = int(input())
#         if a == '+':
#             print(num1 + num2)
#         elif a == "-":
#             print(num1 - num2)
#         elif a == '/':
#             try: 
#                 print(num1 / num2)
#             except ZeroDivisionError:
#                 print("Нельзя делить на ноль!")
#             finally:
#                 print('YES')
#         elif a == '*':
#             print(num1 * num2)
#         elif a == '**':
#             print(num1 ** num2)
#         else:
#             print("Error")
#     except ValueError :
#         print("Введите число!")






    # 26.05.2023

# file = open ("new.txt","w")
# file.write("Hello, World\n")
# file.write("Hi")
# file.close()

file = open ("new.txt","r", encoding="utf-8")
# file.write("Hello, World\n")
# file.write("Hi")
s =file.read()
print (s)
file.close()





