import requests
import json
#Make an API call, and store the response.
url='https://hacker-news.firebaseio.com/v0/item/19155826.json'
r=requests.get(url)
print(f"status Code {r.status_code}")
response_dict=r.json()

filename='/home/timlinux/Downloads/crash_course/chapter16/data/readable_hn_data.json'

with open(filename,'w') as f :
	json.dump(response_dict,f,indent=4)


