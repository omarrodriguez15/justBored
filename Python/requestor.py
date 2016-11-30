import requests
def call(url):
   
   results = requests.get(url)
   print results