#Write a Python script to sort (ascending and descending) a dictionary by value.

dict1 = {0:10,1:30,2:20,3:40}
for i in sorted(dict1.items()):
    print i

#Write a Python script to add a key to a dictionary
table = {'name':'archana','age':28,'gender':'female'}
print 'before entering new item', sorted(table.items())
table['email']= 'abc@gmail.com'
print 'after entering new item',sorted(table.items())

#Second way:
table.update({2:30})
print table




