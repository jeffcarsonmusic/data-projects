import requests

url = "https://api.telnyx.com/v2/messaging_profile_metrics?time_frame=30d"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ###'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)