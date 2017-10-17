'''
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string 


# You are given a string. Split the string on a " " (space) delimiter and join
using a - hyphen.

Input
---
The first line contains a string consisting of space separated words.
output
---
Print the formatted string as explained above.
'''
sentence = "this is a string"

def split_and_join(line):
   words = line.split(' ')
   return '-'.join(words)

print split_and_join(sentence)