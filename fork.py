import requests as r
import re
import time

# configuration.py contains the authentication credentials. See configuration_example.py
import configuration as cfg

API_endpoint = 'https://api.github.com'

# There's no (current) way to API authenticate as an organization. Authenticate as an user with enough rights in the organization and fork as the organization using this parameter
params = {'organization':'gb-archive'}

# Remote list of repositories links to fork
reslist = r.request('get', 'https://raw.githubusercontent.com/avivace/awesome-gbdev/master/README.md')

reg = re.compile('github.com\/([a-zA-Z0-9-]*)\/([a-zA-Z0-9-]*)')
m = re.findall(reg, reslist.text)
print('Found',len(m),'repositories')

# Skip the first match, the original awesome repo.
for i in range (1, len(m)):
	url = API_endpoint + '/repos/' + m[i][0] + '/' + m[i][1] + '/forks'
	print('Forking '+ m[i][0] + '/' + m[i][1])
	print(url)
	f = r.request('post', url=url, params=params, auth=(cfg.credentials['user'], cfg.credentials['token']))
	print(f.status_code)
	# Forks happen asynchronously. Avoid instantly requesting hundreds of them.
	time.sleep(0.5)