import hug

def start(api):

	def aaaaa():
		return "Sim!!"

	hug.get('/funciona', api=api)(aaaaa)
