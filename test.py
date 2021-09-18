import re
w = 'My name IS Dip Bron in 22 March 1996 #hane #lol #come #how'
c = re.findall('([A-Z])', w)
s = re.findall('([a-z])', w)
n = re.findall('([0-9])', w)
hash_ = re.findall('([#])', w)
print('capitel letter' , c)
print('small letter' , s)
print('numbers' , n)
print('hash tag' , hash_)