l1 = [6,-2,3,10,8,0]
l2 = ['hii', 'good morning', 'hello']
l1.sort()
print(l1)
l2.sort()
print(l2)

# see the difference between .sort() and sorted()
l3 = [4,-5,2,0,12,8]
print(l3)
l4 = sorted(l3)
print(l4)
print(sorted(l3))
print('--------')
print(l3)
l3.sort()
print(l3)
print(l3.sort())
print(sorted("Roma"))

# Optional reverse parameter
print(sorted(l3, reverse = True))
print(sorted(l3, reverse = False))

#Optional Key parameter

def absolute(x):
    if x< 0:
        return -x
    else:
        return x

print(sorted(l3, key = absolute))
print(sorted(l3, key = absolute, reverse = True))




