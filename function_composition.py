def most_common_character(s):
    dict = count_freq(s)
    return repeat_character(dict)

# Function to count the frequency of each character in the given string
def count_freq(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 0
        d[c] = d[c] + 1
    print(d)
    return(d)

# Function to find which character in the string occurs more 
def repeat_character(dict):
    d = dict.keys()
    d = list(d)
    best_key_so_far = d[0]
    for k in d:
        if dict[k] > dict[best_key_so_far]:
            best_key_so_far = k
    return(best_key_so_far)
print(most_common_character("aaaaaaaaaaaaaaabbcccddddfffff"))
