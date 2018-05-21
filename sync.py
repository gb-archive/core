import requests as r
import re
import time
import json

# configuration.py contains the authentication credentials. See configuration_example.py
import configuration as cfg

API_endpoint = 'https://api.github.com'

## SYNC forks to upstream


# GET https://api.github.com/repos/gb-archive/awesome-gbdev
# f.json()['clone_url'][:-4]
#

url = API_endpoint + '/orgs' + '/gb-archive' + '/repos'
repos = []
currentPage = 0
while True:
	params = {'page' : currentPage}
	f = r.request('GET', url=url, params=params, auth=(cfg.credentials['user'], cfg.credentials['token']))
	if (f.status_code != 200):
		print(f.json())
		break
	if (f.json() == []):
		print('Found',len(repos),'repositories')
		break
	currentPage += 1
	for repo in f.json():
		repos.append(repo["full_name"])
	print('Added',len(f.json()),'repos')

for repo in repos:
	print('\nSyncing', repo)
	# Get the upstream parent repository
	url = API_endpoint + '/repos/' + repo
	f = r.request('GET', url=url, auth=(cfg.credentials['user'], cfg.credentials['token']))
	try:
		parentRepo = f.json()['source']['full_name']
	except KeyError:
		print('Source repository not found. Trying with the parent')
		try:
			parentRepo = f.json()['parent']['full_name']
		except KeyError:
			print('No parent or source repo found, skipping.')
			continue
	print('Found parent repository', parentRepo)
	url = API_endpoint + '/repos/' + parentRepo + '/git/refs/heads/master'
	f = r.request('GET', url=url, auth=(cfg.credentials['user'], cfg.credentials['token']))
	ref = f.json()['object']['sha']
	print("Got upstream ref", ref)
	url = API_endpoint + '/repos/' + repo + '/git/refs/heads/master'
	f = r.request('PATCH', url=url, data = json.dumps({'sha':ref}), auth=(cfg.credentials['user'], cfg.credentials['token']))
	if (f.status_code == 200):
		print('Fork synced succesfully')