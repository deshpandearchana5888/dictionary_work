dic1={1:10, 2:20, 3:40,4:50,5:80}
dic2={3:30, 4:40}
dict3 = {}

for i in dic1.iterkeys():
    for j in dic2.iterkeys():
        if i == j:
            dict3[i]= 100
            print dict3.items()
        if i != j:
            print i

