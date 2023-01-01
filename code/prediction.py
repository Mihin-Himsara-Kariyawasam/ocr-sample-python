import requests, os, sys

model_id ='be7269f8-7687-4c6d-b008-5524b09f1696'
api_key = 'm-eSBQW6IQYI2bZ1-TqMdTrsSgHbl-N1'
image_path = sys.argv[1]

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/LabelFile/'

data = {'file': open(image_path, 'rb'),    'modelId': ('', model_id)}

response = requests.post(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), files=data)

print(response.text)
response_data = response.json()
for i in response_data["result"]:
    prediction = i["prediction"]
    for j in prediction:
        print (j["ocr_text"])
        ocr_text=j["ocr_text"]
        print (ocr_text)
        print (ocr_text.replace(" ",""))
