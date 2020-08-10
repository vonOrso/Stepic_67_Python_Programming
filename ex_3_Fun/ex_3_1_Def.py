# 1
# def f(x):
#     return 1-(x+2)**2 if x <= -2 else -(x/2) if x > -2 and x<=2 else (x-2)**2+1

# 2
# def modify_list(l):
#     z = 0
#     x = len(l)
#     while z<x:
#         if l[z] % 2 != 0:
#             l.remove(l[z])
#             x-=1
#         else:
#             l[z] = int(l[z]/2)
#             z+=1
#
# lst = [1, 2, 3, 4, 5, 6]
# modify_list(lst)
# print(lst)