L = [('a',2,3), ('d', 5,1), ('e',6,2),('g',2,3), ('b', 5,1), ('z',6,2),('b', 5,1),('b', 5,2)]
for x in sorted(L):
    print(x)

name = ['ram', 'roma', 'rakesh kumar', 'balu', 'balaji', 'thiruniraiselvan', 'mahesh', 'aadhi']
ordered_name = sorted(name, key = lambda k: (len(k), k), reverse = False)
print(ordered_name)
for x in ordered_name:
    print(x)

# Breaking ties. reversing the primary sorting
ordered_name = sorted(name, key = lambda k: (-len(k), k))
print(ordered_name)
for x in ordered_name:
    print(x)