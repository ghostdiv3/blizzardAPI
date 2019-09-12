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

## specifying the global variable for the API FQDN

URL = "https://us.api.blizzard.com"

###########################################################################
## Achivement API
###########################################################################

def achievement_categories_index():

    API_HTTP_PATH = "/data/wow/achievement-category/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def achievement_category(ACHIEVE_CATEGORY_ID):

    API_HTTP_PATH = f"/data/wow/achievement-category/{ACHIEVE_CATEGORY_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def achievements_index():

    API_HTTP_PATH = f"/data/wow/achievement/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def achievement(ACHIEVE_ID):

    API_HTTP_PATH = f"/data/wow/achievement/{ACHIEVE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def achievement_media(ACHIEVE_ID):

    API_HTTP_PATH = f"/data/wow/media/achievement/{ACHIEVE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

###########################################################################
## Azerite Essence API
###########################################################################

def azerite_essences_index():

    API_HTTP_PATH = f"/data/wow/azerite-essence/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True 

def azerite_essence(ESSENCE_ID):

    API_HTTP_PATH = f"/data/wow/azerite-essence/{ESSENCE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def azerite_essence_media(ESSENCE_ID):

    API_HTTP_PATH = f"/data/wow/media/azerite-essence/{ESSENCE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

###########################################################################
## Connected Realm API
###########################################################################

def connected_realms_index():

    API_HTTP_PATH = f"/data/wow/connected-realm/index"
    REGION = "us"
    NAMESPACE = "dynamic-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def connected_realm(REALM_ID):

    API_HTTP_PATH = f"/data/wow/connected-realm/{REALM_ID}"
    REGION = "us"
    NAMESPACE = "dynamic-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

###########################################################################
## Creature API
###########################################################################

def creature_families_index():
    
    API_HTTP_PATH = f"/data/wow/creature-family/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

def creature_family(CREATURE_ID):

    API_HTTP_PATH = f"/data/wow/creature-family/{CREATURE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

def creature_types_index():

    API_HTTP_PATH = f"/data/wow/creature-type/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

def creature_types(TYPE_ID):

    API_HTTP_PATH = f"/data/wow/creature-type/{TYPE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()

    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

def creature(CREATURE_ID):
    
    API_HTTP_PATH = f"/data/wow/creature/{CREATURE_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

def creature_display_media(DISPLAY_ID):
    
    API_HTTP_PATH = f"/data/wow/media/creature-display/{DISPLAY_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

def creature_family_media(FAMILY_ID):
    
    API_HTTP_PATH = f"/data/wow/media/creature-family/{FAMILY_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    
    print(json.dumps(RESULT, indent=2, sort_keys=True))
    
    return True

###########################################################################
## Guild API
###########################################################################

###########################################################################
## Guild Crest API
###########################################################################

###########################################################################
## Item API
###########################################################################

def item_classes_index():
    
    API_HTTP_PATH = "/data/wow/item-class/index"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, indent=2, sort_keys=True))

    return True

def item_class(ITEM_CLASS_ID):
    
    API_HTTP_PATH = f"/data/wow/item-class/{ITEM_CLASS_ID}"
    REGION = "us"
    NAMESPACE = "static-us"
    LOCALE = "en_US"
    PARAMS = {'region':REGION, 'namespace':NAMESPACE, 'locale':LOCALE}
    FULL_URL = f"{URL}{API_HTTP_PATH}"
    RESULT = requests.get(FULL_URL, headers=AUTH_HEADER, params=PARAMS).json()
    print(json.dumps(RESULT, indent=2, sort_keys=True))

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
## Mythic Keystone Affix API
###########################################################################

###########################################################################
## Mythic Raid Leaderboard API
###########################################################################

###########################################################################
## Mount API
###########################################################################

###########################################################################
## Mythic Keystone Dungeon API
###########################################################################

###########################################################################
## Mythic Keystone Leaderboard API
###########################################################################

###########################################################################
## Pet API
###########################################################################

###########################################################################
## Playable Class API
###########################################################################

###########################################################################
## Playable Race API
###########################################################################

###########################################################################
## Playable Specialization API
###########################################################################

###########################################################################
## Power Type API
###########################################################################

###########################################################################
## PvP Season API
###########################################################################

###########################################################################
## PvP Tier API
###########################################################################

###########################################################################
## Realm API
###########################################################################

###########################################################################
## Region API
###########################################################################

###########################################################################
## Title API
###########################################################################

###########################################################################
## WoW Token API
###########################################################################

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
    print(json.dumps(RESULT, indent=2, sort_keys=True))

###########################################################################
###########################################################################
