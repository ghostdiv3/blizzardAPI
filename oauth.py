import requests
import json
import time
import configparser

PARSER = configparser.ConfigParser()
PARSER.read('.env')

URL = "https://us.battle.net"
CHAR_URL = "https://us.api.blizzard.com"

###########################################################################
## This section contains the User Authentication calls
###########################################################################

def authorization_request():

	CLIENT_ID = PARSER.get('creds', 'CLIENT_ID')
	API_HTTP_PATH = "/oauth/authorize"
	RESPONSE_TYPE = "code"
	REDIRECT_URI = "https://localhost"
	SCOPE = "wow.profile"
	FULL_URL = f"{URL}{API_HTTP_PATH}"
	PARAMS = {'response_type':RESPONSE_TYPE,
	'client_id':CLIENT_ID,
	'redirect_uri':REDIRECT_URI,
	'scope':SCOPE}
	RESULT = requests.get(FULL_URL, params=PARAMS).url
	
	print(f"""Paste the following URL into a web browser and enter the new code
	 (you may have to log into Battle.net):\n\n{RESULT}\n\n""")

	GET_CODE = input("New OAuth Token: ")
	PARSER.set('codeflow', 'authorization', GET_CODE)
	ENVFILE = open('.env', 'w')
	PARSER.write(ENVFILE)
	ENVFILE.close()

def access_token_request():
	AUTH_CODE = PARSER.get('codeflow', 'authorization')
	CLIENT_ID = PARSER.get('creds', 'client_id')
	CLIENT_SECRET = PARSER.get('creds', 'client_secret')
	API_HTTP_PATH = "/oauth/token"
	GRANT_TYPE = "authorization_code"
	REDIRECT_URI = "https://localhost"
	SCOPE = "wow.profile"
	PARAMS = {'grant_type':GRANT_TYPE,
	'code':AUTH_CODE,
	'redirect_uri':REDIRECT_URI,
	'scope':SCOPE}
	FULL_URL = f"{URL}{API_HTTP_PATH}"

	RESULT = requests.post(FULL_URL, auth=(CLIENT_ID, CLIENT_SECRET), params=PARAMS).json()

	OAUTH_TOKEN = RESULT['access_token']
	OAUTH_EXPIRATION = str(RESULT['expires_in'])
	OAUTH_SCOPE = RESULT['scope']
	OAUTH_TYPE = RESULT['token_type']
	
	# injects the new token data into the .env file for future use
	PARSER.set('codeflow', 'token', OAUTH_TOKEN)
	PARSER.set('codeflow', 'expiration', OAUTH_EXPIRATION)
	PARSER.set('codeflow', 'scope', OAUTH_SCOPE)
	PARSER.set('codeflow', 'type', OAUTH_TYPE)
	
	# open and save the .env file with new configparser changes
	ENVFILE = open('.env', 'w')
	PARSER.write(ENVFILE)
	ENVFILE.close()

	print("Token Request: Success\n\n")
	print(f"New OAuth Token: {OAUTH_TOKEN}\n")
	print(f"OAuth Token Expiration: {OAUTH_EXPIRATION}\n")
	print(f"OAuth Scope: {OAUTH_SCOPE}\n")
	print(f"OAuth Type: {OAUTH_TYPE}\n")

	return True

def user_info(): # uses the POST method, recommended by Blizzard over GET

	API_HTTP_PATH = "/oauth/userinfo"
	OAUTH_TOKEN = PARSER.get('codeflow', 'token')
	HEADER = f"Bearer {OAUTH_TOKEN}"
	AUTH_HEADER = {'Authorization': HEADER}
	FULL_URL = f"{URL}{API_HTTP_PATH}"
	
	RESULT = requests.get(FULL_URL, headers=AUTH_HEADER).json()

	print(RESULT)

###########################################################################
## This section contains the Application Authentication calls
###########################################################################

def access_apptoken_request():
	CLIENT_ID = PARSER.get('creds', 'client_id')
	CLIENT_SECRET = PARSER.get('creds', 'client_secret')
	API_HTTP_PATH = "/oauth/token"
	GRANT_TYPE = "client_credentials"
	SCOPE = "wow.profile"
	PARAMS = {'grant_type':GRANT_TYPE,
	'scope':SCOPE}
	FULL_URL = f"{URL}{API_HTTP_PATH}"

	RESULT = requests.post(FULL_URL, auth=(CLIENT_ID, CLIENT_SECRET), params=PARAMS).json()

	AUTH_TOKEN = RESULT['access_token']
	AUTH_EXPIRATION = str(RESULT['expires_in'])
	AUTH_SCOPE = RESULT['scope']
	AUTH_TYPE = RESULT['token_type']

	# injects the new token data into the .env file for future use
	PARSER.set('tokens', 'token', AUTH_TOKEN)
	PARSER.set('tokens', 'expiration', AUTH_EXPIRATION)
	PARSER.set('tokens', 'scope', AUTH_SCOPE)
	PARSER.set('tokens', 'type', AUTH_TYPE)
	
	# open and save the .env file with new configparser changes
	ENVFILE = open('.env', 'w')
	PARSER.write(ENVFILE)
	ENVFILE.close()


###########################################################################
## This section contains the Token Validation calls
###########################################################################

def token_validation():

	API_HTTP_PATH = "/oauth/check_token"
	OAUTH_TOKEN = PARSER.get('codeflow', 'token')
	HEADER = f"Bearer {OAUTH_TOKEN}"
	AUTH_HEADER = {'Authorization': HEADER}
	PARAMS = {'token':OAUTH_TOKEN}
	FULL_URL = f"{URL}{API_HTTP_PATH}"

	RESULT = requests.get(FULL_URL, params=PARAMS).json()

	if RESULT['exp'] - int(time.time()) <= 600:
		print("API token expires in less than 10 minutes. Regenerating...\n")
		# insert future 1-shot regen function
	else:
		print("API token is still valid. Continuing...\n")


###########################################################################
###########################################################################

#authorization_request()
#access_token_request()
access_apptoken_request()
#user_info()
#token_validation()