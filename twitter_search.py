import oauth2
import time
import urllib2
import json

url1 = "https://api.twitter.com/1.1/search/tweets.json"
params = {
"oauth_version": "1.0",
"oauth_nonce": oauth2.generate_nonce(),
"oauth_timestamp": int(time.time())
}

consumer = oauth2.Consumer(key="wexyVEpfmqjGxOL8KReDoyR3L", secret="uiSFgPuPqaFZAat0TquLI4gPL7QWllv6omvHuozyccsLRu5kyh")
token = oauth2.Token(key="39716397-mVN30oaYbMK92eCGqIEPUzydalzQA2n3zokwWeQyh", secret="tUB10EV7dUYpHsHjpK9dStGMxRw7qFHdMUWTTfVbNgJrz")
params["oauth_consumer_key"] = consumer.key
params["oauth_token"] = token.key

# for i in range(1):
# 	url = url1
# 	req = oauth2.Request(method="GET", url=url, parameters=params)
# 	signature_method = oauth2.SignatureMethod_HMAC_SHA1()
# 	req.sign_request(signature_method, consumer, token)
# 	headers = req.to_header()
# 	url = req.to_url()
# 	print headers
# 	print url

for i in range(1):
	url = url1
	params["q"] = "microsoft"
	params["count"] = 100
	req = oauth2.Request(method="GET", url=url, parameters=params)
	signature_method = oauth2.SignatureMethod_HMAC_SHA1()
	req.sign_request(signature_method, consumer, token)
	headers = req.to_header()
	url = req.to_url()
	response = urllib2.Request(url)
	data = json.load(urllib2.urlopen(response))
	# print type(data)
	print data[u'search_metadata']
	# print data[u'statuses']
	# print data.keys()
