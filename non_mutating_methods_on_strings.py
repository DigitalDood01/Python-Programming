s = "Hello Dood"
t = s.lower()
print(s.upper())
print(t)

#counting elements in the string
c = print(s.count('o'))

#strip- removes the whitespace in the beginning and end of string
ss = "          good     morning                "
print(ss)
print(ss.strip())

#replace - strings are non-mutable so it creates a new string.
print(id(s))
print(s.replace('o', '$'))
print(id(s))

#format - Makes the code more readable.
print("{}. checking out the format method in string {}. ".format(s,ss))