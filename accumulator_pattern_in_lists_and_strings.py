#In lists
num = [1,2,3,4,5]
square = []
print(num)
for i in num:
    j = i*i
    square.append(j)
print(square)

#in strings
s = input("Enter the string")
a = ''
for i in s:
    a = a + i + '*'
print(a)