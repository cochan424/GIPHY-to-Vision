import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
import json
import random
import webbrowser
from emotion import resultkey

# create an instance of the API class
api_instance = giphy_client.DefaultApi()
api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
q = resultkey # str | Search query term or prhase.
limit = 10 # int | The maximum number of records to return. (optional) (default to 25)
offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
rating = 'g' # str | Filters results by specified rating. (optional)
lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

try: 
    # Search Endpoint
    api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
    pprint(api_response)

    links = []
    index = 0
    while index < len(api_response.data):
        links += [api_response.data[index].embed_url]
        index += 1
    # print (links)
    # print(random.randint(1, limit))
    print(links[random.randint(0, limit-1)]) # gives a random link with the corresponding emotion query
    #webbrowser.open(links[random.randint(0, limit-1)])
    #pprint(api_response.__getitem__('data'))
    #print(api_response.data[0].embed_url)

except ApiException as e:
    print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)