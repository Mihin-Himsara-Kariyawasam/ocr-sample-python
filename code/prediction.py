import requests, os, sys

model_id = os.environ.get('NANONETS_MODEL_ID')
api_key = os.environ.get('NANONETS_API_KEY')
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
