import	hug
from	conx		import connex
from	cryption	import cryptKey
from	modyl		import mod

api		= hug.get(on_invalid=hug.redirect.not_found)
API		= hug.API(__name__)
keys	= cryptKey.Key()
modules	= mod.loadModules(API)

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

@api.get()
def list():
	return modules

@api.get()
def newModule(name, description, file, version, author):
	mod.Module(name, description, file, version, author)

@api.get(
	'/{slug_one}/'
) # THIS IS RIDICULOUS
def get_one():
	return True

@api.get(
	'/{slug_one}/{slug_two}/'
)
def get_two():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/'
)
def get_three():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/'
)
def get_four():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/'
)
def get_five():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/'
)
def get_six():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/'
)
def get_seven():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/'
)
def get_eight():
	return True

@api.get(
	'/{slug_one}/{slug_two}/{slug_three}/{slug_four}/{slug_five}/{slug_six}/{slug_seven}/{slug_eight}/{slug_nine}/'
)
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
	return True
