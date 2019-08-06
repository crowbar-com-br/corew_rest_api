import	hug
from	conx		import connex
from	cryption	import cryptKey
from	modyl		import mod

api		= hug.get(on_invalid=hug.redirect.not_found)
keys	= cryptKey.Key()

def getAPI():
	return hug.API(__name__)

def updateAPI():
	readFile = open("./app.py")
	lines = readFile.readlines()
	readFile.close()

	a = open("./app.py",'a')
	a.write(' ')
	a.close()

	w = open("./app.py",'w')
	w.writelines([item for item in lines[:-1]])
	w.close()

modules	= mod.loadModules(getAPI())

@api.get(
	'/publicKey',
	version=1
)
def getPublicKey():
	"""Returns the public key of this Micro-Service"""
	return {
		'publicKey'	: cryptKey.savePublic(keys.public)
	}

@api.get(
	'/status',
	version=1
)
def getStatus():
	"""Returns the actual status of this MS server"""
	import psutil
	return {
		'CPU'	: psutil.cpu_percent(),
		'Memory': psutil.virtual_memory()[2]
	}

@api.get('/')
def list():
	return modules

@api.post()
def uploadModule(request):
	mod.uploadModule(request.headers['FILENAME'], request.stream)
	mod.loadModules(getAPI())
	updateAPI() # TODO: FIND A BETTER WAY
	return "Success!"

@api.get(
	'/{slug_one}/'
) # THIS IS RIDICULOUS
def get_one():
	return True

@api.get(
	'/{slug_one}/{slug_two}/'
) # REALLY???
def get_two():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/'
) # OH DUDE, KILL ME
def get_three():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/'
) # NOOOOOOOOOOOO
def get_four():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/'
) # DAMMIT
def get_five():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/'
) # OKAY, OKAY, YOU WON
def get_six():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/'
) # sorry
def get_seven():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/'
) # Please, give me a better solution
def get_eight():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/{slug_nine}/'
) # ...
def get_nine():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/{slug_nine}/{slug_ten}/'
)
def get_ten():
	return True

@api.get(
	'/{slug_one}/'
)
def post_one():
	return True

@api.post(
	'/{slug_one}/{slug_two}/'
)
def post_two():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/'
)
def post_three():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/'
)
def post_four():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/'
)
def post_five():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/'
)
def post_six():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/'
)
def post_seven():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/'
)
def post_eight():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/{slug_nine}/'
)
def post_nine():
	return True

@api.post(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/{slug_nine}/{slug_ten}/'
)
def post_ten():
	return True

def isJSON(content: "A expected JSON"):
	"""Check if the param content can be a JSON"""
	try:
		object = json.loads(content)
	except:
		return False
