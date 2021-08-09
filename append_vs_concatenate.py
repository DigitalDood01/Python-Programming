mylist = [1,2,3]
print(mylist)
print("identifier is", id(mylist))
mylist.append(4)
newlist = mylist
print(mylist)
print("identifier is", id(mylist))
mylist +=   ["hello"]

print(mylist)
print(newlist)
print("identifier is", id(mylist))
print("identifier is", id(newlist))

mylist = mylist + ['dog']

print(mylist)
print(newlist)
print("identifier is", id(mylist))
print("identifier is", id(newlist))

