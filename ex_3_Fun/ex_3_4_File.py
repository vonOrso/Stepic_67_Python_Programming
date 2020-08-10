# 1
# inf = list(open('dataset_3363_2.txt','r').readline())
# st,co,b = '','',inf[0]
# for i in inf[1:]:
#     if i.isdigit():
#         co+=i
#     else:
#         st+=str(b*int(co))
#         b = i
#         co=''
# otv = open('otv_4.txt','w')
# otv.write(st)
# otv.close()

# 2
# d_kl,d_zn=[],[]
# with open('dataset_3363_3.txt','r') as inf:
#     for line in inf:
#         line = line.strip().lower().split(' ')
#         for i in line:
#             if i not in d_kl:
#                 d_kl.append(i)
#                 d_zn.append(1)
#             else:
#                 d_zn[d_kl.index(i)]+=1
# print(d_kl[d_zn.index(max(d_zn))],max(d_zn))

# 3
# mat,fiz,rus,sr = [],[],[],[]
# with open('dataset_3363_4.txt','r') as inf:
#     for line in inf:
#         line = line.strip().split(';')
#         mat.append(int(line[1]))
#         fiz.append(int(line[2]))
#         rus.append(int(line[3]))
#         sr.append((int(line[1])+(int(line[2])+int(line[3])))/3)
#
# with open('otv_4.txt','w') as f:
#     for i in sr:
#         f.write(str(i)+'\n')
#     f.write(str(sum(mat)/len(mat))+' '+str(sum(fiz)/len(fiz))+' '+str(sum(rus)/len(rus)))