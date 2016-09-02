import requests
from PIL import Image
from io import BytesIO
import json

#r = requests.get("https://api.github.com/events")
r = requests.get("http://www.omdbapi.com/?t=midnight+in+paris&y=&plot=short&r=json")

# what will 'print r' do? print status code of request OR r.status_code

#print 'data is\n' + r.text
#print 'url is ' + r.url
#print 'encoding is ' + r.encoding
#print 'binary content\n' + r.content

img_data = requests.get('https://assets-cdn.github.com/images/modules/open_graph/github-mark.png')
i = Image.open(BytesIO(img_data.content))
#i.show()

js = r.json()
#print js.keys()
#print js['Title']

#print r.json()
#print r.raw

#print r.headers

post_header = {'name' : 'kds', 'product' : 'kdsdk'}
post_req = requests.post('http://httpbin.org/post',json.dumps(post_header))
#print post_req

teapot = requests.get('http://httpbin.org/status/418')
#print teapot.text

head_req = requests.head('http://httpbin.org/get')
#print head_req.text

options_req = requests.options('http://httpbin.org/get')
#print options_req.text

pass_params = {'name' : 'kds', 'product' : 'kdsdk'}
pass_params_req = requests.get('http://httpbin.org/get', params = pass_params)
#print pass_params_req.url

#print r.history       contains all status codes for redirection made to complete request
#gh_url = requests.head('http://github.com', allow_redirects=True)
#print gh_url.history

# no packet received in 0.001s
#gh_url = requests.get('http://github.com', allow_redirects=True, timeout = 0.001)
#print gh_url.history