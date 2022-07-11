import requests 
from plotly.graph_objs import Bar
from plotly import offline 

url='https://api.github.com/search/repositories?q=language:Java&sort=stars'
headers={'Accepte':'application/vnd.github.v3+json'}

r=requests.get(url,headers=headers)
print(f"Status: {r.status_code}")
response_dict=r.json()
print(response_dict.keys())
repo_dicts=response_dict['items']
#print(sorted(repo_dicts[0].keys()))
repo_links,stars,labels=[],[],[]

for repo_dict in repo_dicts:
	repo_name=repo_dict['name']
	repo_url=repo_dict['html_url']
	repo_link=f"<a href='{repo_url}'> {repo_name}</a>"
	owner=repo_dict['owner']['login']
	description=repo_dict['description']
	label=f"{owner} </br> {description}"
	labels.append(label)
	repo_links.append(repo_link)
	stars.append(repo_dict['stargazers_count'])

data=[{
    'type':'bar',
    'x':repo_links,
    'y':stars,
    'hovertext':labels,
    'marker':{
        'color':'rgb(67,80,87)',
        'line': {'width':1.5,'color':'rgb(25,25,25)'}
    },
    'opacity':0.6,
}]


layout={
    'title':' Bar char for popularity of Java',
    'titlefont':{'size': 12},

    'xaxis':{ 
        'title':'Repositories',
        'titlefont':{'size':12},
        'tickfont':{'size':14},
       },
    'yaxis':{
        'title':'Number of Visit',
        'titlefont':{'size':12},
        'tickfont':{'size':14},
    }

}

fig={'data':data,'layout':layout}

offline.plot(fig)


