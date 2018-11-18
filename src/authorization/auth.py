def getToken(username, password, keys): # Still in test
	import	json
	import	requests
	from	cryption	import cryptKey

	url = "http://localhost:8080/getToken"

	headers = {
		'cache-control'	: "no-cache"
	}

	payload = {
		'username'	: username,
		'password'	: password
	}

	auth_pubKey = json.loads(
		requests.request("GET", "http://localhost:8080/publicKey").text
	)['publicKey']

	payload	= {
		'payload'	: cryptKey.encryptData(payload, cryptKey.loadPublic(auth_pubKey)),
		'publicKey'	: cryptKey.savePublic(keys.public)
	}

	response = requests.request("POST", url, headers=headers, data=payload)
	data = json.loads(response.text)
	return cryptKey.decryptData(data['payload'], keys.private)

def checkToken(request):
	import	requests

	authorization = request.get_header("Authorization")

	if 'Bearer' in authorization:
		url = "http://localhost:8080/token_authenticated"

		headers = {
			'cache-control': "no-cache",
			'Authorization': authorization.replace('Bearer ', '')
		}

		response = requests.request("GET", url, headers=headers)
		return response.status_code
	else:
		return 403

def hug_checkToken(token):
	import	requests

	if 'Bearer' in token:
		url = "http://localhost:8080/token_authenticated"

		headers = {
			'cache-control': "no-cache",
			'Authorization': token.replace('Bearer ', '')
		}

		response = requests.request("GET", url, headers=headers)
		if response.status_code == 200:
			return True
		else:
			return False
	else:
		return False
