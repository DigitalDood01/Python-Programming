#Optional parameters

def fun(a, L = []):
    L.append(a)
    return L

print(fun(1))
print(fun(2))
print(fun(3))
print(fun(4))
print(fun(5, ['hii']))
print(fun(6, ['hello']))

#keyword parameters

i = 5
def f(x, y=3, z = i):
    print("value of x,y,z are " +str(x), str(y), str(z))

f(1)
f(1,2,3)
f(1,z=10)
