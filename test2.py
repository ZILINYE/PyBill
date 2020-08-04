dic1 = { 'A':30,'B':30}

dic2 = {'C':15,'D':20,'E':10,'F':15}

dic1 = {k: v for k, v in sorted(dic1.items(), key=lambda item: item[1],reverse=True)}

dic2 = {k: v for k, v in sorted(dic2.items(), key=lambda item: item[1],reverse=True)}

print(dic1)
print(dic2)

list1k = list(dic1.keys())# owe
list1v = list(dic1.values())
list2k = list(dic2.keys())#borrow
list2v = list(dic2.values())

# for i in range(len(list1)):
#     for y in range(len(list2)):
#         if(list2[y] != 0):
#             t = list1[i]  - list2[y]
#             if t > 0:
#                 list1[i] = t                               
#                 print('Owe'+str(i)+' owe  Borrow'+str(y)+' '+str(list2[y]))
#                 list2[y] = 0

#             elif t == 0:
#                 print('Owe'+str(i)+' owe  Borrow'+str(y)+' '+str(list2[y]))
#                 list2[y] = 0
#                 break

            
#             else:
#                 list2[y] = -t
#                 print('Owe'+str(i)+' owe  Borrow'+str(y)+' '+str(list1[i]))
#                 break


for i in range(len(list1v)):
    for y in range(len(list2v)):
        if(list2v[y] != 0):
            t = list1v[i]  - list2v[y]
            if t > 0:
                list1v[i] = t                               
                print('Owe'+list1k[i]+' owe  Borrow'+list2k[y]+' '+str(list2v[y]))
                list2v[y] = 0

            elif t == 0:
                print('Owe'+list1k[i]+' owe  Borrow'+list2k[y]+' '+str(list2v[y]))
                list2v[y] = 0
                break

            
            else:
                list2v[y] = -t
                print('Owe'+list1k[i]+' owe  Borrow'+list2k[y]+' '+str(list1v[i]))
                break