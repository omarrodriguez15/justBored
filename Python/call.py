import requests
import urlparse

#https://api.twitter.com/1.1/friendships/outgoing.format
url = 'https://api.twitter.com/1.1/'
 
#define a variable to store results and make the request
 
#passing in the above url - simple right?
 
results = requests.get(url)
print results
#if we needed authentication to do this, we could have
 
#passed in more parameters to the requests.get() but we don't

#-----add the above code here-------
 
#results = requests.get(url)
 
#use json() to make things nicer here
 
#better_results = results.json()

#print better_results