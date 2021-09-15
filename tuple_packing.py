tuple1 = ('i', 'am', 'studying', 'python')
print(tuple1[3], tuple1)
tuple2 = 'i', 'am', 'studying', 'python'
print(tuple2[3], tuple2)

def add(x,y):
    return x + y

z = 4,5
print(add(*z))          # Asterik is used to inform the intertpreter to unpack the tuple z

d = {'a':3, 'b':6, 'c':'hello'}
for p in d.items():
    print("key is {} and value is {}" .format(p[0], p[1]))