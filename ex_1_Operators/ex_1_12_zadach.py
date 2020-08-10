# 1
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a+b+c)/2
# print((p*(p-a)*(p-b)*(p-c))**0.5)

# 2
# a = int(input())
# print(True) if (a>-15 and a<=12) or (a>14 and a<17) or a>=19 else print(False)

# 3
# a = float(input())
# b = float(input())
# c = input()
# if c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '/':
#     print('Деление на 0!') if b==0 else print(a/b)
# elif c == '*':
#     print(a*b)
# elif c == 'mod':
#     print('Деление на 0!') if b==0 else print(a - (a//b)*b)
# elif c == 'pow':
#     print(a**b)
# else:
#     print('Деление на 0!') if b==0 else print(a//b)

# 4
# d = input()
# pisos = 3.14
# if d == 'треугольник':
#     a,b,c = int(input()),int(input()),int(input())
#     p = (a + b + c) / 2
#     print((p*(p-a)*(p-b)*(p-c))**0.5)
# elif d == 'прямоугольник':
#     a, b = int(input()), int(input())
#     print(a*b)
# else:
#     a = int(input())
#     print(pisos*a**2)

# 5
# ss = [int(input()),int(input()),int(input())]
# print(max(ss))
# ss.remove(max(ss))
# print(min(ss))
# ss.remove(min(ss))
# print(ss[0])

# 6
# sa = input()
# sd1 = int(list(sa)[-1])
# if (sd1 >= 2 and sd1 <= 4):
#     print(sa + ' ' + 'программистов') if len(sa)>=2 and int(list(sa)[-2])==1 else print(sa + ' ' + 'программиста')
# elif sd1 == 1:
#     print(sa + ' ' + 'программистов') if len(sa)>=2 and int(list(sa)[-2])==1 else print(sa+' '+'программист')
# else:
#     print(sa + ' ' + 'программистов')

# 7
# ss = list(input())
# print('Счастливый') if int(ss[0]) + int(ss[1]) + int(ss[2]) == int(ss[3]) + int(ss[4]) + int(ss[5]) else print('Обычный')


