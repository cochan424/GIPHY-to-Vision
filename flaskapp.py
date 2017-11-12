from flask import Flask, flash, redirect, render_template, request, session, abort
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json
import time, cv2, giphy_client, random, webbrowser
from giphy_client.rest import ApiException
from pprint import pprint

flaskapp = Flask(__name__)
 
@flaskapp.route("/")
def main():
    image = webcam()
    emot_str = emotion(image)
    print("EMOTIONAL STRING: " + emot_str)
    #giphy(emot_str)
    
    quote, bitly = giphy(emot_str)
    print("QUOTE " + quote)   
    print("BITLY " + bitly)
    return render_template(
        'hello.html',**locals())

def webcam():
    camera_port = 0

    cv2.namedWindow("preview")
    camera = cv2.VideoCapture(camera_port)

    if camera.isOpened(): # try to get the first frame
        rval, frame = camera.read()
    else:
        rval = False

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = camera.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            return_value, image = camera.read()
            cv2.imwrite("temp_img.jpg", image)
            cv2.destroyWindow("preview")
            del(camera)  # so that others can use the camera as soon as possible
            return "temp_img.jpg"

def emotion(imge):
    headers = {
        # Request headers. Replace the placeholder key below with your subscription key.
        'Content-Type': 'application/octet-stream',
        # 'Ocp-Apim-Subscription-Key': '13hc77781f7e4b19b5fcdd72a8df7156',
        'Ocp-Apim-Subscription-Key': '78171d52b4454431a8833a05f5ceb700',
    }

    params = urllib.parse.urlencode({
    })

    # Replace the example URL below with the URL of the image you want to analyze.
    with open(imge, "rb") as imageFile:
      f = imageFile.read()
    b = bytearray(f)
    body = b 
   
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read() 

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
        
    x = parsed[0]["scores"]
    print (x)
    resultkey ='eh'
    resultvalue=0
    for key in x:
        if x[key]>resultvalue:
            resultkey = key
            resultvalue = x[key]
        
    return resultkey
        
    conn.close()
    
def giphy(emotion_str):
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = 'dc6zaTOxFJmzC' # str | Giphy API Key.
    q = emotion_str # str | Search query term or prhase.
    limit = 10 # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g' # str | Filters results by specified rating. (optional)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

    try: 
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
        #pprint(api_response)

        links = []
        index = 0
        while index < len(api_response.data):
            links.append((api_response.data[index].embed_url,api_response.data[index].bitly_url))
            index += 1
        
        rand_tuple = links[random.randint(0, limit-1)]
        print() # gives a random link with the corresponding emotion query
        #webbrowser.open(rand_tuple[0])
        return(rand_tuple)

    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
 
if __name__ == "__main__":
    flaskapp.run(host='0.0.0.0', port=80)
    #