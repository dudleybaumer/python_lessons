def print_verse1():
   print 'here comes the sun'
   print 'little darling'

def print_chorus():
	print 'sun, sun, here it comes\n' * 5

def print_formatter(item):
   print 'here comes the %s' %(item)
   print 'little darling'


print_verse1()
print_chorus()
print_formatter ('pickles')

## pickle would be the argument. parameter would be 'item' in this case.