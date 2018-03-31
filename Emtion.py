import cognitive_face as CF
import requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import json

# set up congnitive_face
KEY = '33576d5eaeeb4adcaac8a414df7cdfd1'  
CF.Key.set(KEY)

BASE_URL = 'https://southeastasia.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

# set up the url of th e group picture
img_url = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/20245535_662274280629921_284773622154778063_n.jpg?oh=d5086c717f3b9d95ec02b25b19bd43cb&oe=5B18F36E'

faces = id = (CF.face.detect(img_url,landmarks=True,attributes='age,gender,headPose,smile,facialHair,glasses,emotion,makeup,accessories,occlusion,blur,exposure,noise,hair'))

print (json.dumps(faces, sort_keys=True, indent=2))

