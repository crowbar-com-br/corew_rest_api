import	importlib
import	json
import	os

class Module(object):
	name		= ""
	description	= ""
	file		= ""
	version		= ""
	author		= ""

	def __init__(self, name, description, file, version, author):
		self.name			= name
		self.description	= description
		self.file			= file
		self.version		= version
		self.author			= author

		save(self.__dict__, "list.json")

def loadModules(api):
	list	= load("list.json")
	error	= []
	for module in list:
		try:
			mod	= importlib.import_module("modules." + module["file"] + "." + module["file"])
			mod.start(api)
		except:
			error.append(module)
	return	list

def save(data, fileName):
	if not os.path.exists('./cache'):
		os.makedirs('./cache')
	if not os.path.exists('./cache/' + fileName):
		open('./cache/' + fileName, mode='w').close()
	file		= open("./cache/" + fileName, "r+")
	file_open	= file.read()
	if (isJSON(file_open)):
		content	= json.loads(file_open)
	else:
		content	= []
	content.append(data)
	file.close()
	open("./cache/"  + fileName, "w").close()
	file	= open("./cache/"  + fileName, "r+")
	file.write(json.dumps(content))
	file.close()

def load(fileName):
	if not os.path.exists('./cache/' + fileName):
		return False
	with open("./cache/"  + fileName, "r") as read_file:
		data = json.load(read_file)
	return data

def isJSON(content: "A expected JSON"):
	"""Check if the param content can be a JSON"""
	try:
		object = json.loads(content)
	except:
		return False
	return True
