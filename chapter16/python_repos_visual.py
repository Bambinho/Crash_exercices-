import requests

from plotly.graph_objs import  Bar
from plotly import offline

url='https://api.github.com/search/repositories?q=language:python&sort=stars'
headers={'Accepte':'application/vnd.github.v3+json'}
r=requests.get(url,headers=headers)
request_dict=r.json()
print(request_dict.keys())
repo_dicts= request_dict['items']
#repo_names,stars,labels=[],[],[]
repo_links,stars,labels=[],[],[]

for repo_dict in repo_dicts:
	repo_name=repo_dict['name']
	repo_url=repo_dict['html_url']
	repo_link=f"<a href='{repo_url}'> {repo_name}</a>"
	repo_links.append(repo_link)
	owner=repo_dict['owner']['login']
	description=repo_dict['description']
	label=f"{owner}<br /> {description}"

	labels.append(label)
	stars.append(repo_dict['stargazers_count'])
#Making visualization 
data=[{
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
	      'color':'rgb(60,100,150)',
	      'line':{'width':1.5,'color':'rgb(25,25,25)'}
	  },
	  'opacity':0.6,
}

]

my_layout={
	  'title':"Most-starred Python Projects on GitHub",
	  'titlefont':{'size':25},
	  'xaxis':{
	        'title': 'Repositories',
	        'titlefont':{'size':12},
	        'tickfont':{'size':14}
	           },
	  'yaxis':{
	      'title':'Stars',
	      'titlefont':{'size':12},
	       'tickfont':{'size':14}
	       },
}

fig={'data':data,'layout':my_layout}

offline.plot(fig,filename='python_repos.html')

