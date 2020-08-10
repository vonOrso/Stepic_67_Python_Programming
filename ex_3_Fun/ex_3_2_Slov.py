# 1
# def update_dictionary(d, key, value):
#     if key not in d and key*2 in d:
#         d[key*2].append(value)
#     elif key not in d and key*2 not in d:
#         d[key*2]=[value]
#     else:
#         d[key].append(value)
#
# d = {}
# update_dictionary(d, 1, -1)  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}

# 2
# a = [i.lower() for i in input().split()]
# d = {}
# for i in a:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for i in d:
#     print(i+' '+str(d[i]))

# 3
# def f(a):
#     return
#
# n=int(input())
# d={}
# s = []
# for i in range(n):
#     a = int(input())
#     s.append(a)
#     if a not in d:
#         d[a]=f(a)
# for i in s:
#     print(str(d[i]))