# print("Hello world!")

# print("Salam", end=' ')
# print("Khoobi?")

# s = input('Enter --> ')
# print(type(s))
# print('s : ',s)

# # data type and data structure
# i = 10  # int
# print(f'content:{i}\ntype:{type(i)}')
# print('-------------------------')
# f = 10.0  # float
# print(f'content:{f}\ntype:{type(f)}')
# print('-------------------------')
# l = [1, 2, 4, "two"]  # list
# print(f'content:{l}\ntype:{type(l)}')
# l[2]=67
# print(f'content:{l}\ntype:{type(l)}')
# print('-------------------------')
# s = "network"  # string
# print(f'content:{s}\ntype:{type(s)}')
# print('-------------------------')
# t = (6, 5, 8)  # tuple
# print(f'content:{t}\ntype:{type(t)}')
# t[1] = 34
# print(f'content:{t}\ntype:{type(t)}')
# print('-------------------------')
# d = {"course": "Network", "id": 1234}  # dictionary
# print(f'content:{d}\ntype:{type(d)}')
# print(d)
# print(d.values())
# print(d.keys())
# d = list(d.values())
# print(d)
# print('-------------------------')

# # Casting
# print(str(23))
# print(type(str(23)))
# print(int(1.6))
# print(float('8765'))


# # condition_loop
# # if_else
# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(b)

# # while
# a = 0
# b = 1
# while a < 10:
#     print(a)
#     c = b
#     b = a + b
#     a = c
#
# # continue
# x = 0
# while x < 10:
#     x += 1
#     if x % 2 == 0:
#         continue
#     print(x)
#
# # break
# result = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#     result = result + n
# print(result)

# # for
# numbers = [4, 7, 8]
# for num in numbers:
#     print(num)
#
# for i in range(len(numbers)):
#     print(i, numbers[i])
#
# # # enumerate
# for index, value in enumerate(numbers):
#     print(index, value)

# # range()
# for i in range(5):
#     print(i, end=' ')
#
# for i in range(5, 10):
#     print(i, end=' ')

# for i in range(0, 10, 2):
#     print(i, end=' ')

# # len()
# words = ['salam', 'khoobi?', ':)))']
#
# for i in range(len(words)):
#     print(words[i])
# print(len(words))


# # function
# def f(n):
#     return n + n
#
#
# print('f :', f(55))

# # write Fibonacci series up to n
# def fib(n):
#     """Print a Fibonacci series up to n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#
#
# print(fib(2000))

# # Handling Exceptions
# try:
#     x = int(input('Enter : '))
#     print("It's a number!")
# except ValueError as e:
#     print("It's just a string!", e)

## datetime
# from datetime import time
# #
# t = time(17, 21, 20, 2021)
# print(t)
# # error not writable
# t.hour = 10
# print(t)

# from datetime import date
# d = date(2019, 5, 23)
# print(d.year, d.month, d.day)

# from datetime import datetime
# dt = datetime(1, 2, 3, 4, 5, 6, 7)
# print(dt.hour, dt.minute, dt.second, dt.microsecond)
# print(dt.year, dt.month, dt.day)
# print(datetime.now())

# str1 = "ali".encode()  # convert string to byte
# print(str1)
# str2 = str1.decode()  # convert byte to string
# print(str2)


## file
# f = open('a.txt')
# print(f.read(6))
# print(f.read(6))

# f = open("Info.txt", "r")
# lines = []
# while True:
#     line = f.readline()
#     if line == '':
#         break  # end of file
#     lines.append(line)
# for line in lines:
#     print(line)

# n = int(input('line:'))
# f = open("Info.txt", "a")
# for i in range(n):
#     line = input('content:')
#     f.write(line + '\n')
