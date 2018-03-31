import time
import operator
import requests
#import cv2
import operator
import numpy as np
#from __future__ import print_function
import numpy as np
import csv

# Import library to display results
import matplotlib.pyplot as plt

# Display images within Jupyter
# Variables
_region = 'westcentralus' #Here you enter the region of your subscription
_url = 'https://{}.api.cognitive.microsoft.com/face/v1.0/detect'.format(_region)
_key = 'cd3d38869499493086ad8d8f644106e8' #Here you enter your subscription key
_maxNumRetries = 10
def processRequest( json, data, headers, params ):

    """
    Parameters:
    json: Used when processing images from its URL. See API Documentation
    data: Used when processing image read from disk. See API Documentation
    headers: Used to pass the key information and the data type request
    """

    retries = 0
    result = None

    while True:

        response = requests.request( 'post', _url, json = json, data = data, headers = headers, params = params )

        if response.status_code == 429: 

            print( "Message: %s" % ( response.json() ) )

            if retries <= _maxNumRetries: 
                time.sleep(1) 
                retries += 1
                continue
            else: 
                print( 'Error: failed after retrying!' )
                break

        elif response.status_code == 200 or response.status_code == 201:

            if 'content-length' in response.headers and int(response.headers['content-length']) == 0: 
                result = None 
            elif 'content-type' in response.headers and isinstance(response.headers['content-type'], str): 
                if 'application/json' in response.headers['content-type'].lower(): 
                    result = response.json() if response.content else None 
                    #print(result)
                elif 'image' in response.headers['content-type'].lower(): 
                    result = response.content
        else:
            print( "Error code: %d" % ( response.status_code ) )
            print( "Message: %s" % ( response.json() ) )

        break
        
    return result

path = 'datasets/normal/normal_'
ans_list = []
for i in range(857):
    pathToFileInDisk = path + str(i) + '.jpg'
    print(i)
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()

    headers = dict()
    headers['Ocp-Apim-Subscription-Key'] = _key
    headers['Content-Type'] = 'application/octet-stream'

    json = None
    params = {'returnFaceAttributes':'age,gender,emotion'} 

    result = processRequest( json, data, headers, params )
    ans_list.append(result)



#np.save("normal.npy", ans_list)

f = open("normal.csv","w")
w = csv.writer(f)
w.writerows(ans_list)
f.close()