
list3 = []
list5 = []
list1 = []
for x in range(1, 1000):
    if x * 3 < 1000:
        list3.append(3*x)
    if x * 5 < 1000:
        list5.append(5*x)
#for each in list3:
#    print(each)
for each in list5:
    if each not in list3:
        list3.append(each)
list3.sort()        
for each in list3:
    print(each)
print(sum(list3))
