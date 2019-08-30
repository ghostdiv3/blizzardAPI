import requests
import json
import time
import configparser

###########################################################################
## This section sets up the token variable for use in the API calls
###########################################################################

PARSER = configparser.ConfigParser()
PARSER.read('.env')
AUTH_TOKEN = PARSER.get('tokens', 'TOKEN')

HEADER_BEARER = f"Bearer {AUTH_TOKEN}"
AUTH_HEADER = {'Authorization':HEADER_BEARER}

###########################################################################
## This section sets up the token variable for use in the API calls
###########################################################################

## specifying the global variable for the API FQDN
URL = "https://us.api.blizzard.com"

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

def creature_info(CREATURE_ID):
    API_HTTP_PATH = f"/data/wow/creature/{CREATURE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, sort_keys=True, indent=4, separators=(',', ': ')))
    
    return True

def creature_families():
    API_HTTP_PATH = f"/data/wow/creature-family/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    for i in range(len(RESULT['creature_families'])):
        print(f"""\nCreature ID: {RESULT['creature_families'][i]['id']}
                  \nCreature Name: {RESULT['creature_families'][i]['name']}""")
    
    return True

def creature_types():
    API_HTTP_PATH = "/data/wow/creature-type/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, sort_keys=True, indent=4, separators=(',', ': ')))

    return True

def item_classes_index():
    API_HTTP_PATH = "/data/wow/item-class/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, sort_keys=True, indent=4, separators=(',', ': ')))

    return True

def item_class(ITEM_CLASS_ID):
    API_HTTP_PATH = f"/data/wow/item-class/{ITEM_CLASS_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, sort_keys=True, indent=4, separators=(',', ': ')))

    return True

def item_id_check(ITEM_ID):
    API_HTTP_PATH = f"/data/wow/item/{ITEM_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS)
    
    if RESULT.status_code == 200:
        return RESULT.json()
    else:
        return f"Item ID #{ITEM_ID} does not exist."

def store_item_id(ITEM_ID):
    API_HTTP_PATH = f"/data/wow/item/{ITEM_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    return RESULT

###########################################################################
###########################################################################

ITEM_LIST = {}
ITEM_LIST['items'] = ['zero']

for i in range(0, 300):
    ITEM_LIST['items'].append(item_id_check(i))

print(ITEM_LIST['items'])