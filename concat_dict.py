#Write a Python script to concatenate following dictionaries to create a new one or Merging dictionary

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
final_dict = dict()
final_dict.update(dic1)
#print final_dict
final_dict.update(dic2)
#print final_dict
final_dict.update(dic3)
print 'final dictionary %s' % final_dict

# Second way

users1 = {'archana':'archana_24'}
users2 = {'suruchi':'vaidya_123'}
users_list = dict()
for i in (users1,users2):
    users_list.update(i)
print "users list %s" % users_list





###