# 1
# a = [int(i) for i in input().split()]
# print(sum(a))

# 2
# a = [int(i) for i in input().split()]
# if len(a)==1:
#     print(a[0])
# else:
#     a.insert(0, a[-1])
#     a.append(a[1])
#     i, s = 1, []
#     while i < len(a) - 1:
#         s.append(a[i - 1] + a[i + 1])
#         i += 1
#     print(' '.join(map(str, s)))

# 3
# a = [i for i in input().split()]
# z = 0
# b = []
# while z != 1:
#     if len(a) == 0:
#         z = 1
#     else:
#         x = 0
#         ss = a[0]
#         a.remove(ss)
#         if ss in a:
#             b.append(ss)
#             while ss in a:
#                 a.remove(ss)
# print(' '.join(b))
