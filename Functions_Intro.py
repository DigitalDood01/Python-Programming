def Hello(i,j):
    output = "Good morning " + i + "   "
    print(output * 3 )

Hello("Roma", 4)

def square(y):
    y = y*y
    return(y)
x = 10;
result = square(x)
print(" The square of ", x, "is", result)

def total(lst):
    total = 0
    for item in lst:
        total = item + total
    print(total)

lst = [1,2,3,4,5]
total(lst)