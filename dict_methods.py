#WAP to check if keys are similar in two dictionary if it is same then add value to that key
# if it is not then add those keys and corresponding value

dic1={1:10,2:20,3:40,4:50,5:80}
dic2={3:30,4:40}
dic3 = dict()
#print dic3
for i in  sorted(dic1.keys()):
    #print i
    for j in sorted(dic2.keys()):
        #print j
        if i == j:
            dic3[j]= 100
            #print dic3
        if i not in sorted(dic3.keys()):
            #print i
            dic3.update({i:10})
            #print dic3

print 'dictionary after modification %s' % dic3


