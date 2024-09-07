import requests
ip_default="www.picolab.eu"
print("Server IP",ip_default)
r = requests.get('http://'+ip_default+'/cgi-bin/python/DHT11/DHT11_0.py')
print(r.text)


