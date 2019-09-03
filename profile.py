import requests
import json
import time
import configparser

###########################################################################
## This section contains the token-related API calls
###########################################################################

URL = "https://us.api.blizzard.com"

PARSER = configparser.ConfigParser()
PARSER.read('.env')
CURR_TOKEN = PARSER.get('tokens', 'TOKEN')

def token_check():
    PARSER = configparser.ConfigParser()
    PARSER.read('.env')
    CLIENT_ID = PARSER.get('creds', 'CLIENT_ID')
    CLIENT_SECRET = PARSER.get('creds', 'CLIENT_SECRET')
    CURR_TOKEN = PARSER.get('tokens', 'TOKEN')

    if CURR_TOKEN == '':
        print("No token set. Generating new token...\n")
        time.sleep(1)
        NEW_TOKEN = token_gen(CLIENT_ID, CLIENT_SECRET)
        PARSER.set('tokens', 'TOKEN', NEW_TOKEN)
        ENVFILE = open('.env', 'w')
        PARSER.write(ENVFILE)
        ENVFILE.close()
        return True

    else:
        print("\nToken already exists. Continuing program...\n")

def token_gen(CLIENTID, CLIENTSECRET):
    TOKEN_REQ = {'grant_type':'client_credentials', 'scope':'wow.profile'}
    TOKEN_DATA = requests.post('https://us.battle.net/oauth/token',
     auth=(CLIENTID, CLIENTSECRET), data=TOKEN_REQ).json()
    print("Configuring new token...")
    time.sleep(1)
    print("Done\n")
    print(f"New session token    : {TOKEN_DATA['access_token']}")
    print(f"Token type           : {TOKEN_DATA['token_type']}")
    print(f"Token time remaining : {TOKEN_DATA['expires_in']}")
    print(f"Scope of token       : {TOKEN_DATA['scope']}")

    return TOKEN_DATA['access_token']

def token_validation():
    


    API_HTTP_PATH = "/oauth/check_token"
    REGION = "us"
    NAMESPACE = "profile-us"
    LOCALE = "en_US"    
    PARAMS = {'token':CURR_TOKEN, 'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.post(FULL_URL, params=PARAMS).json()

    print(RESULT)

###########################################################################
###########################################################################

def character_achievements(CHAR_NAME, CHAR_REALM):
    
    API_HTTP_PATH = f"/profile/wow/character/{CHAR_REALM}/{CHAR_NAME}/achievements"
    REGION = "us"
    NAMESPACE = "profile-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(RESULT)
    
    return True

###########################################################################
###########################################################################

token_validation()