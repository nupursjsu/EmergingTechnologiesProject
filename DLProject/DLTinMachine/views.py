from django.shortcuts import render
import requests
import datetime
# from geopy.geocoders import Nominatim
# import cv2
# from fastai import *
# from fastai.tabular import *
# from torchvision.models import *
# from fastai.vision import *
from django.views.decorators.csrf import csrf_exempt
# from keras.models import load_model
import cv2
import numpy as np
# from keras.optimizers import Adam
# import shutil
# using s3 bucket
import json

def default_view(request):
    return render(request, 'base.html')


@csrf_exempt
def predict_Image(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            req = requests.get(url, stream=True)
            with open("response.jpeg", "wb") as f:
                f.write(req.content)

        except:
            req = "failed to download image"

        # model = load_model('/Users/lokesh/Downloads/DLProject/DLTinMachine/my_h5_model.h5')

        # model.compile(loss='binary_crossentropy', optimizer=Adam(lr=1e-4), metrics=['accuracy'])

        img = cv2.imread("response.jpeg")
        img = cv2.resize(img, (224, 224))
        img = np.reshape(img, [1, 224, 224, 3])
        import pickle
        data = json.dumps({"signature_name": "serving_default", "instances": img.tolist()})
        # dataText = img.tolist()

        # f = open('file.txt', 'w')
        # f.write('dict = ' + repr(data) + '\n')
        # f.close()

        headers = {"content-type": "application/json"}

        
        json_response = requests.post('http://35.223.23.11:8501/v1/models/saved_model:predict', data=data, headers=headers)
        print(json_response)
        predictions = json.loads(json_response.text)['predictions']

        classes = np.argmax(predictions)

        # classes = model.predict_classes(img)

        if classes == 0:
            result = "Malignant"
        else:
            result = "Benign"

        print(result)
        context = {
            "imageURL": url,
            "cancer": result,
        }
        return render(request, 'result.html', context)
