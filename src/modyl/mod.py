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
	if not os.path.exists('./.cache/modulesList.json'):
		open('./.cache/modulesList.json', mode='w').write('[]')
	list	= loadJSON("modulesList.json") # Let's load our list of modules
	errors	= [] # Well, nothing is perfect, we never know
	for module in list:
		try:
			mod	= importlib.import_module("modules." + module["file"] + "." + module["file"]) # So, we find the module on our module package, there we estore it
			mod.start(api) # Let's start it! I hope...
		except Exception as e: # TODO: Report broken modules
			errors.append({
				"module": module,
				"error": str(e.__class__) + " " + str(e)
			}) # Aaaannnddd we got a rotten apple
			list.remove(module)
	if errors:
		print("Modules errors:")
		for error in errors:
			print("\tModule " + error['module']['name'] + "\n\tError: " + error['error'])
	return	list, errors

def uploadModule(
		fileName		: "The name of the zip file, wich contains the package of the module",
		stream			: "A zip file, in package format",
		content_length	: "The lenght of the file"
	): # Method used to upload modules into the REST API, wich will create a package 'modules' for these modules, upload them into the same and list them into the 'modulesList'

	if not os.path.exists('./modules'): # We need the modules package
		os.makedirs('./modules') # Well, let's create it!
		open('./modules/__init__.py', mode='w').close()

	if not os.path.exists('./.cache/tmp/module'):
		os.makedirs('./.cache/tmp/module') # Let's create a temp folder for our module
	with open('./.cache/tmp/module/' + fileName, 'wb') as file: # Let's create it!
		file.write(stream.read(content_length or 0)) # Write it's content
		file.close() # Close it

	folderName	= os.path.splitext('./.cache/tmp/module/' + fileName)[0]

	with ZipFile('./.cache/tmp/module/' + fileName,"r") as zip_ref:
		zip_ref.extractall(folderName)

	modulesList	= loadJSON("modulesList.json")
	info		= loadJSON("info.json", folderName) # Let's load the info about this module
	module		= Module(info['name'], info['description'], info['file'], info['version'], info['author']) # Let's get a module object from it!

	if not module.__dict__ in modulesList: # We already have it?
		shutil.move(folderName, './modules/') # No! Let's move it to our modules package
		save(module.__dict__, "modulesList.json") # And save it in our modulesList
		shutil.rmtree('./.cache/tmp/module') # Time to clean the temp
		return module # Nice!
	else:
		shutil.rmtree('./.cache/tmp/module')
		return False # Yes.. :c
	shutil.rmtree('./.cache/tmp/module')

	return False # Something went wrong...

def removeModule(name):

	if not os.path.exists('./modules'): # We need the modules package
		os.makedirs('./modules') # Well, let's create it!
		open('./modules/__init__.py', mode='w').close()

	modulesList	= loadJSON('modulesList.json')

	module		= next((item for item in modulesList if item['name'] == name), None)

	try:
		shutil.rmtree('./modules/' + module['name'])
	except Exception as e:
		e = e
	try:
		delete(module, "modulesList.json")
	except ValueError as e:
		return False
	return True

def save(data, fileName):
	""" """
	if not os.path.exists('./.cache'):
		os.makedirs('./.cache')
	if not os.path.exists('./.cache/' + fileName):
		open('./.cache/' + fileName, mode='w').close()
	file		= open("./.cache/" + fileName, "r+")
	file_open	= file.read()
	if (isJSON(file_open)):
		content	= json.loads(file_open)
	else:
		content	= []
	content.append(data)
	file.close()
	open("./.cache/"  + fileName, "w").close()
	file	= open("./.cache/"  + fileName, "r+")
	file.write(json.dumps(content))
	file.close()

def delete(data, filename):
	if not os.path.exists('./.cache'):
		os.makedirs('./.cache')
	if not os.path.exists('./.cache/' + filename):
		open('./.cache/' + filename, mode='w').close()
	file		= open("./.cache/" + filename, "r+")
	file_open	= file.read()
	if (isJSON(file_open)):
		content	= json.loads(file_open)
	else:
		content	= []
	content.remove(data)
	file.close()
	open("./.cache/"  + filename, "w").close()
	file	= open("./.cache/"  + filename, "r+")
	file.write(json.dumps(content))
	file.close()

def loadJSON(fileName, folderName = ""):
	if folderName != "":
		with open(folderName + "/" + fileName, "r") as read_file:
			data = json.load(read_file)
			return data
	if not os.path.exists('./.cache/' + fileName):
		return False
	with open("./.cache/"  + fileName, "r") as read_file:
		data = json.load(read_file)
		return data

def isJSON(content: "A expected JSON"):
	"""Check if the param content can be a JSON"""
	try:
		object = json.loads(content)
	except:
		return False
	return True
