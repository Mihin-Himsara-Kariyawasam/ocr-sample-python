import requests, os

model_id ='be7269f8-7687-4c6d-b008-5524b09f1696'
api_key = 'm-eSBQW6IQYI2bZ1-TqMdTrsSgHbl-N1'

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/' + model_id + '/Train/'

querystring = {'modelId': model_id}

response = requests.request('POST', url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=querystring)

print(response.text)

print("\n\nNEXT RUN: python ./code/model-state.py")