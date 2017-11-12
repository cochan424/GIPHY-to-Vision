# ########### Python 2.7 #############
# import http.client, urllib, base64

# headers = {
#     # Request headers. Replace the placeholder key below with your subscription key.
#     'Content-Type': 'application/json',
#     'Ocp-Apim-Subscription-Key': '13hc77781f7e4b19b5fcdd72a8df7156',
# }

# params = urllib.parse.urlencode({
# })

# # Replace the example URL below with the URL of the image you want to analyze.
# body = "{ 'url': 'http://example.com/picture.jpg' }"

# try:
#     # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
#     #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
#     #   URL below with "westcentralus".
#     conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
#     conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
#     response = conn.getresponse()
#     data = response.read()
#     print(data)
#     conn.close()
# except Exception as e:
#     print("[Errno {0}] {1}".format(e.errno, e.strerror))

# ####################################

########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, sys, json

headers = {
    # Request headers. Replace the placeholder key below with your subscription key.
    'Content-Type': 'application/octet-stream',
    # 'Ocp-Apim-Subscription-Key': '13hc77781f7e4b19b5fcdd72a8df7156',
    'Ocp-Apim-Subscription-Key': '78171d52b4454431a8833a05f5ceb700',
}

params = urllib.parse.urlencode({
})

# Replace the example URL below with the URL of the image you want to analyze.
with open("opencv.jpg", "rb") as imageFile:
  f = imageFile.read()
  #print(bytearray(f))
  b = bytearray(f)
body = b #{'url': 'C:\Users\cchan\Documents\Code\GIPHY to Vision\opencv.png'} #"{ 'url': 'https://www.askideas.com/media/41/Sweet-Baby-Very-Funny-Sad-Face-Picture-For-Whatsapp.jpg' }"

try:
    # NOTE: You must use the same region in your REST call as you used to obtain your subscription keys.
    #   For example, if you obtained your subscription keys from westcentralus, replace "westus" in the 
    #   URL below with "westcentralus".
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/emotion/v1.0/recognize?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read() 

    # 'data' contains the JSON data. The following formats the JSON data for display.
    parsed = json.loads(data)
    # print ("Response:")
    # print (json.dumps(parsed, sort_keys=True, indent=2))
    
    x = parsed[0]["scores"]
    print (x)
    resultkey ='eh'
    resultvalue=0
    for key in x:
        if x[key]>resultvalue:
            resultkey = key
            resultvalue = x[key]
    
    print(resultkey)
    
    conn.close()
except Exception as e:
    print(e.args)
####################################