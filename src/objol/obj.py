import	json
import	os
import	shutil

class Objol(object):
	name		= ""
	slug		= ""
	schema		= "{}"
	subObjols	= "[]"
	active		= False

	def __init__(self, name, slug, schema, subObjols, active):
		self.name		= name
		self.slug		= slug
		self.schema		= schema
		self.subObjols	= subObjols
		self.active		= active

def addObjol(objol):

	objolsList	= loadJSON("objolsList.json")
	if not objolsList:
		objolsList	= []
	objol		= Objol(
		name=objol["name"],
		slug=objol["slug"],
		schema=objol["schema"],
		subObjols=objol["subObjols"],
		active=objol["active"]
	)
	if not objol.__dict__ in objolsList:
		save(objol.__dict__, "objolsList.json")
		return objol
	return False

def removeObjol(name):

	objolsList	= loadJSON('objolsList.json')
	objol		= next((item for item in objolsList if item['name'] == name), None)

	try:
		delete(objol, "objolsList.json")
	except ValueError as e:
		return False
	return True

def updateObjol(new_objol):

	objolsList	= loadJSON('objolsList.json')
	old_objol		= next((item for item in objolsList if item['name'] == name), None)

	try:
		delete(old_objol, "objolsList.json")
		save(objol.__dict__, "objolsList.json")
	except ValueError as e:
		return False

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
