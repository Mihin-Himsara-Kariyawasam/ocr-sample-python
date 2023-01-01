import requests, os, json

model_id ='be7269f8-7687-4c6d-b008-5524b09f1696'
api_key = 'm-eSBQW6IQYI2bZ1-TqMdTrsSgHbl-N1'

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id

response = requests.request('GET', url, auth=requests.auth.HTTPBasicAuth(api_key,''))

state = json.loads(response.text)["state"]
status = json.loads(response.text)["status"]

if state != 5:
	print("The model isn't ready yet, its status is:", status)
	print("We will send you an email when the model is ready. If you are impatient, run this script again in 10 minutes to check.")
else:
	print("NEXT RUN: python ./code/prediction.py ./images/151.jpg")
