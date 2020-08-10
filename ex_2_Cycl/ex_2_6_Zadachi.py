# 1
# i,ss,sa = 1,0,0
# while i != 0:
#     a = int(input())
#     ss+=a
#     sa += a**2
#     if ss == 0:
#         i = 0
# print(sa)

# 2
# a = int(input())
# i,z,x = 1,[],0
# while x!=1:
#     if len(z)+i>a:
#         z+=[str(i)]*(a-len(z))
#         x =1
#     else:
#         z += [str(i)] * i
#     i += 1
# print(' '.join(z))

# 3
# a = [int(i) for i in input().split()]
# x = int(input())
# s, d = 0,0
# while d<len(a):
#     if a[d] == x:
#         print(str(d), end=' ')
#         s+=1
#     d+=1
# if s==0:
#     print('Отсутствует')

# 4
# ss,spl = [],[]
# while 'end' not in spl:
#     spl = input().split()
#     if 'end' not in spl: ss.append([int(i) for i in spl])
#
# l_str = len(ss)
# l_stlb = len(ss[0])
# ss.insert(0,ss[-1])
# ss.append(ss[1])
# z = 1
# while z < l_str+1:
#     ss[z].insert(0, ss[z][-1])
#     ss[z].append(ss[z][1])
#     z+=1
# sa = [['']*l_stlb for i in range(l_str)]
# z = 1
# while z < l_str+1:
#     x = 1
#     while x < l_stlb+1:
#         sa[z-1][x-1] = str(ss[z-1][x]+ss[z+1][x]+ss[z][x-1]+ss[z][x+1])
#         x+=1
#     z+=1
# z = 0
# while z < l_str:
#     print(' '.join(sa[z]))
#     z+=1

# 5
# n = int(input())
# ss = [['']*n for i in range(n)]
# st, m = 1, 0
# ss[n//2][n//2]=str(n*n)
# for v in range(n//2):
#     for i in range(n-m):
#         ss[v][i+v] = str(st)
#         st+=1
#     for i in range(v+1, n-v):
#         ss[i][-v-1] = str(st)
#         st+=1
#     for i in range(v+1, n-v):
#         ss[-v-1][-i-1] = str(st)
#         st+=1
#     for i in range(v+1, n-(v+1)):
#         ss[-i-1][v]= str(st)
#         st+=1
#     m+=2
# for i in ss:
#     print(' '.join(i))