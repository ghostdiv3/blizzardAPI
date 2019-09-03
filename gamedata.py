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

def achievement_categories_index():

    API_HTTP_PATH = "/data/wow/achievement-category/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(RESULT)

def achievement_categories(ACHIEVE_CATEGORY_ID):

    API_HTTP_PATH = f"/data/wow/achievement-category/{ACHIEVE_CATEGORY_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(RESULT)

def achievement_index():

    API_HTTP_PATH = f"/data/wow/achievement/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(RESULT)

def achievement_id(ACHIEVE_ID):

    API_HTTP_PATH = f"/data/wow/achievement/{ACHIEVE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(RESULT)

def achievement_media(ACHIEVE_ID):

    API_HTTP_PATH = f"/data/wow/media/achievement/{ACHIEVE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(RESULT)


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

def zone_master_list():
    
    API_HTTP_PATH = f"/wow/zone"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, indent=4, sort_keys=True))


###########################################################################
###########################################################################

achievement_index()