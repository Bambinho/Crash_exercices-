import requests 


def open_api(url,head):
	r=requests.get(url,headers=head)
	return r
def main():
	#Make an API call and store the response 
	url='https://api.github.com/search/repositories?q=language:python&sort=stars'
	headers={'Accept':'application/vnd.github.v3+json'}
	r=open_api(url,headers)
	# r=requests.get(url,headers=headers)
	request_dict=r.json()
	print(f"keys {request_dict.keys()}")
	print(f"The number of response: {request_dict['total_count']}")
	repo_dicts=request_dict['items']
	print(f"Repository returned: {len(repo_dicts)}")
	#repo_dict=repo_dicts[0]

	print(f"\nSelected information about first repository:")
	for repo_dict in repo_dicts:
		print(f"\nName:{repo_dict['name']}")
		print(f"Owner:{repo_dict['owner']['login']}")
		print(f"Repository: {repo_dict['html_url']}")
		print(f"Stars: {repo_dict['stargazers_count']}")
		print(f"Created: {repo_dict['created_at']}")
		print(f"Updated: {repo_dict['updated_at']}")
		print(f"Description: {repo_dict['description']}")


if __name__=='__main__':
	main()




