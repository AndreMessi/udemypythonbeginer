#tipe data list
mylist = ["ayam goreng","nasi bungkus","nasi balap puyung"]
print (mylist)
print (mylist[0])
print (mylist[0:4])
print (mylist[5:11])

list_two = ["bakso malang","gado gado"]
list_new = mylist+list_two
print (list_new)

#delete list
del mylist[2]
print (mylist)

print (len(mylist))
mylist.append("python")
print (mylist)
mylist.index("python")