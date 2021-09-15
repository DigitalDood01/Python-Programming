S = ("PythonProgramming")
L = []
for x in S:
    L.append(x)
print(L)

d = {}
for x in L:
    if x not in d:
        d[x] = 1
    else:
        d[x] = d[x] + 1
print(d)

for x in sorted(d.keys()):
    print( "{} appears {} times" .format(x, d[x]))

print("-----------------------------------------------")
#To sort based on the count values of keys in dictionary
for x in sorted(d.keys(), key = lambda k: d[k], reverse = True ):
    print( "{} appears {} times" .format(x, d[x]))

print("-----------------------------------------------")
for x in sorted(d.keys, key = lambda k: d[k], reverse = False ):
    print( "{} appears {} times" .format(x, d[x]))