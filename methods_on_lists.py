mylist = []
#append
mylist.append(34)
mylist.append(312)
mylist.append(1)
mylist.append(13)
mylist.append(78)
print(mylist)

#insert
mylist.insert(1,11)
print(mylist)

#count
print(mylist.count(11))

#index
print(mylist.index(13))

#reverse
mylist.reverse()
print(mylist)

#sort
mylist.sort()
print(mylist)

#delete
del mylist[0]
print(mylist)

#remove
mylist.remove(78)
print(mylist)

#pop
last = mylist.pop()
print(last)
print(mylist)