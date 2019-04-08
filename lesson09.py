#tipe data dictionery
dict = {'name':'andre', 'age':25}
print (dict['name'])
print (dict['age'])
print (dict.values())

#adding dictionery
dict['name']='nurmayana'
print (dict['name'])
dict['address']='lombok'
print (dict['address'])
print (type(dict))
print (len(dict))
print (max(dict))
dict1 = dict.copy()
dict1['name']='naya'
print (dict1)
print (dict.items())
dict.update(dict1)
print (dict)