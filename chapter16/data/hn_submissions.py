from operator import itemgetter
import requests
from plotly.graph_objs import Bar
from plotly import offline 

###Make an API call and store the reponse 

url='https://hacker-news.firebaseio.com/v0/topstories.json'
r=requests.get(url)
print(f"Status: {r.status_code}")
##proccess information about each submission
submission_ids=r.json()
submission_dicts=[]

for submission_id in submission_ids:
	###Make a separate API call for each submission
	url=f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r=requests.get(url)
	#print(f"{submission_id}\tstatus: {r.status_code}")
	response_dict=r.json()
	##Make a dictionary for each submission
	try:
		submission_dict={
	    'title':response_dict['title'],
	    'hn_link':f"https://news.ycombinator.com/item?id={submission_id}",
	    'comments': response_dict['descendants']
	    }
	except KeyError:
	 	pass 

	submission_dicts.append(submission_dict)

submission_dicts=sorted(submission_dicts,key=itemgetter('comments'),reverse=True)

labels,heights=[],[]
for submission_dict in submission_dicts:
	if submission_dict['comments']==0:
		pass
	else:
		label=f"<a href='{submission_dict['hn_link']}'> {submission_dict['title']} </a>"
		labels.append(label)
		heights.append(submission_dict['comments'])
	# print(f"\nTitle:{submission_dict['title']}")
	# print(f"Discussion link: {submission_dict['hn_link']}")
	# print(f"Comments: {submission_dict['comments']}")

data=[{
	'type':'bar',
	'x':labels,
	'y':heights,
}]

layout={
   'title':" hacker comment to article",
   'titlefont':{'size':25},
   'xaxis':{
       'title':"Comments to Post",
       'titlefont':{'size':12},
   },
   'yaxis':{
       'title':'Number of Coments',
       'titlefont':{'size':12}
   }

}

fig={'data':data,'layout':layout}
offline.plot(fig)

