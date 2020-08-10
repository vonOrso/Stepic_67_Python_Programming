# 1
# n = int(input())
# com,plays,win,non,lose,allpoints = [],[],[],[],[],[]
# for i in range(n):
#     st = input().split(';')
#     for z in [0,2]:
#         if st[z] not in com:
#             com.append(st[z])
#             plays.append(0)
#             win.append(0)
#             non.append(0)
#             lose.append(0)
#             allpoints.append(0)
#
#     cm1,cm2 = com.index(st[0]),com.index(st[2])
#     plays[cm1] += 1
#     plays[cm2] += 1
#     p1,p2 = int(st[1]),int(st[3])
#     if p1>p2:
#         win[cm1]+=1
#         allpoints[cm1]+=3
#         lose[cm2]+=1
#     elif p2>p1:
#         win[cm2]+=1
#         allpoints[cm2]+=3
#         lose[cm1]+=1
#     else:
#         non[cm1]+=1
#         allpoints[cm1]+=1
#         non[cm2]+=1
#         allpoints[cm2]+=1
#
# for i in range(len(com)):
#     print(com[i]+': '+str(plays[i])+' '+str(win[i])+' '+str(non[i])+' '+str(lose[i])+' '+str(allpoints[i]))

# 2
# def code_decode(chto,chem,na_chto):
#     for i in range(len(chto)):
#         chto[i] = na_chto[chem.index(chto[i])]
#     return ''.join(chto)
#
# alp = list(input())
# cod = list(input())
# coded = list(input())
# de_coded = list(input())
# print(code_decode(coded,alp,cod))
# print(code_decode(de_coded,cod,alp))

# 3
# dic = [input().lower() for i in range(int(input()))]
# l = int(input())
# nep = []
# for i in range(l):
#     st = input().lower().split(' ')
#     for z in st:
#         if z not in dic and z not in nep: nep.append(z)
# for i in nep:
#     print(i)

# 4
# coord = [0,0]
# for i in range(int(input())):
#     st = input().split(' ')
#     if st[0] == 'север': coord[1]+=int(st[1])
#     elif st[0] == 'юг': coord[1]-=int(st[1])
#     elif st[0] == 'восток': coord[0]+=int(st[1])
#     else: coord[0]-=int(st[1])
# print(str(coord[0])+' '+str(coord[1]))

# 5
# ss = [[] for i in range(11)]
# with open('dataset_3380_5.txt','r') as inf:
#     for line in inf:
#         st = line.replace('\n','').split('\t')
#         ss[int(st[0])-1].append(int(st[2]))
# for i in range(11):
#     print(str(i+1)+' -') if ss[i] == [] else print(str(i+1)+' '+str(sum(ss[i])/len(ss[i])))