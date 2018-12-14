import	importlib
import	json
import	os
import	shutil
from	zipfile	import ZipFile

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

def loadModules(api	: "Hug API object, used to register our modules on the REST API"):
	if not os.path.exists('./cache/modulesList.json'):
		open('./cache/modulesList.json', mode='w').write('[]')
	list	= loadJSON("modulesList.json") # Let's load our list of modules
	error	= [] # Well, nothing is perfect, we never know
	for module in list:
		try:
			mod	= importlib.import_module("modules." + module["file"] + "." + module["file"]) # So, we find the module on our module package, there we estore it
			mod.start(api) # Let's start it! I hope...
		except: # TODO: Report broken modules
			error.append(module) # Aaaannnddd we got a rotten apple
	return	list

def uploadModule(fileName, stream): # TODO: Implement uploadModule, wich, will receive a zip file with the package of the module; extract it in cache; check if it's a module; extract it in modules package; list it in modulesList;

	if not os.path.exists('./modules'): # We need the modules package
		os.makedirs('./modules') # Well, let's create it!
		open('./modules/__init__.py', mode='w').close()

	if not os.path.exists('./temp/module'):
		os.makedirs('./temp/module') # Let's create a temp folder for our module
	with open('./temp/module/' + fileName, 'wb') as file: # Let's create it!
		file.write(stream.read()) # Write it's content
		file.close() # Close it

	folderName	= os.path.splitext('./temp/module/' + fileName)[0]

	with ZipFile('./temp/module/' + fileName,"r") as zip_ref:
		zip_ref.extractall(folderName)

	modulesList	= loadJSON("modulesList.json")
	info		= loadJSON("info.json", folderName) # Let's load the info about this module
	module		= Module(info['name'], info['description'], info['file'], info['version'], info['author']) # Let's get a module object from it!

	if not module.__dict__ in modulesList: # We already have it?
		shutil.move(folderName, "./modules/") # No! Let's move it to our modules package
		save(module.__dict__, "modulesList.json") # And save it in our modulesList
		#return "Salvo!"
	else:
		print("oi")
		#return "Já existente" # Yes.. :c

	shutil.rmtree('./temp/module') # Time to clean the temp

	return "False"

def save(data, fileName):
	""" """
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

def loadJSON(fileName, folderName = ""):
	if folderName != "":
		with open(folderName + "/" + fileName, "r") as read_file:
			data = json.load(read_file)
			return data
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
