import requests
import json
import time
import configparser

URL = "https://us.api.blizzard.com"

PARSER = configparser.ConfigParser()
PARSER.read('.env')

def characters():
	API_HTTP_PATH = "/wow/user/characters"
	OAUTH_TOKEN = PARSER.get('codeflow', 'token')
	HEADER = f"Bearer {OAUTH_TOKEN}"
	AUTH_HEADER = {'Authorization': HEADER}

	FULL_URL = f"{URL}{API_HTTP_PATH}"
	RESULT = requests.get(FULL_URL, headers=AUTH_HEADER).json()

	print(json.dumps(RESULT, indent=2, sort_keys=True))

###########################################################################
###########################################################################

characters()
