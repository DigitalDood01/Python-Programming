# This Program is about exploring the options in Dictionary
medals = {'gold':1, 'silver':2, 'bronze':3}
print(medals)

medals['gold'] = 23;
print(medals)

del medals['bronze']
print(medals)

data = len(medals)
print(data)

#Accessing the keys in a dictionary
for key in medals.keys():
    print(key)

#Accessing both the keys and its values in a dictionary
for key in medals.keys():
    print(key, "and its value is", medals[key])

#Accessing the the keys in dictionary as a list
keys =list(medals.keys())
print(keys)

#Accessing the values in a dictionary
for value in medals.values():
    print(value)

#Accessing the the keys and values on the whole in dictionary as a list
keys =list(medals.items())
print(keys)

for key in medals:
    print("got the key-", key)

# Checking whether the key is present or not in a dictionary
print('gold' in medals)
print('bronze' in medals)

print(medals.get('gold'))
print(medals.get('diamond',0))