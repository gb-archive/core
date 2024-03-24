import requests as r
import re
import time
import itertools

# configuration.py contains the authentication credentials. See configuration_example.py
import configuration as cfg

API_endpoint = 'https://api.github.com'

## FORK

# Authenticate as an user with enough rights in the organization and fork as the organization using this parameter
params = {'organization':'gb-archive'}

# List of repository sources
sources = ['https://raw.githubusercontent.com/gbdev/awesome-gbdev/master/README.md',
	   'https://raw.githubusercontent.com/gbdev/awesome-gbdev/master/EMULATORS.md',
	   'https://gbdev.io/pandocs/single.html']
m = []
reg = re.compile('github.com\/([a-zA-Z0-9-]*)\/([a-zA-Z0-9-]*)')

for source in sources:
	# Compile a list of repositories links to fork
	reslist = r.request('get', source)
	m.append(re.findall(reg, reslist.text))


# Flatten
chain = itertools.chain.from_iterable(m)
repoList = list(chain)
print('Found',len(repoList),'repositories')


# Fork each matched repo
for i in range (0, len(m[0])):
	# POST /repos/:owner/:repo/forks
	url = API_endpoint + '/repos/' + m[0][i][0] + '/' + m[0][i][1] + '/forks'
	print('Forking '+ m[0][i][0] + '/' + m[0][i][1])
	print(url)
	f = r.request('post', url=url, params=params, auth=(cfg.credentials['user'], cfg.credentials['token']))
	print(f.status_code)
