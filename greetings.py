def greetings (lang):
	if lang == 'es':
		print "Hola"
	elif lang == 'fr':
		print "Bonjour"
	elif lang == 'eng':
		print "Hello"
	else:
	  print "You're"


greetings ('fr')
greetings ('jp')

############# language and a name with it #############

def greetings (lang,name):
	if lang == 'es':
		print "Hola", name
	elif lang == 'fr':
		print "Bonjour", name
	elif lang == 'eng':
		print "Hello", name
	else:
	  print "You're"
	  name = 'no name'
	  #coder has no name


greetings ('fr', "Elise")
greetings ('es', "Juan")

############# TUPLES: changed print function to return instead for closure #############


def greetings (lang,name):
	if lang == 'es':
		return "Hola", name
	elif lang == 'fr':
		return "Bonjour", name
	elif lang == 'eng':
		return "Hello", name
	else:
	  return "You're"
	  name = 'no name'
	  #coder has no name


print greetings ('fr', "Le Chat")
print greetings ('es', "Lolinda")