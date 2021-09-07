str = "This the string to check the occurence of alphabets using dictionaries"
X = {}

for c in str:
    if c not in X:
        X[c] = 0;
    X[c] = X[c] +1

print('a in the string is',X['a'])
print('i in the string is',X['i'])
print('c in the string is',X['c'])
print('r in the string is',X['r'])
print('e in the string is',X['e'])

print(X)

for i in X:
    print(" Number of ",i,"in  Dictonary is", X[i])

# Finding out the character with maximum and minimum occurrence  occurence in the string
d = list(X.keys())
print(d)
maxvalue = d[0]
minvalue = d[0]

for i in d:
    if X[i] > X[maxvalue]:
        maxvalue = i
    elif X[i] < X[minvalue]:
        minvalue = i

print(" max value is", maxvalue, "min value is", minvalue)
