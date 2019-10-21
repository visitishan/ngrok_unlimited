import requests, time, json, os, threading

def temp():
    os.system('cmd /k "cd C://Users//AMIT//downloads//ngrok && ngrok  http 5000"')

try:
   x = threading.Thread(target = temp)
   x.start()
except:
   print("Error: unable to start thread")

time.sleep(5)

s = requests.Session()
a = s.get("http://127.0.0.1:4040/api/tunnels").text
b = json.loads(a)
c= b['tunnels'][0]['public_url']
print(c)


link = {"link":c}
d = s.get('http://yourdomainname.com/index.php',body = link)  #Update the server for tunnel link
