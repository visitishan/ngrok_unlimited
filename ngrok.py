import requests, time, json, os, threading

def temp():
    os.system('cmd /k "cd C://Users//AMIT//downloads//ngrok && ngrok  http 5000"')

while True:
    try:
       x = threading.Thread(target = temp)
       x.start()
    except:
       print("Error: unable to start thread")

    time.sleep(5)

    # s = requests.Session()
    a = requests.get("http://127.0.0.1:4040/api/tunnels").text
    b = json.loads(a)
    c= b['tunnels'][0]['public_url']
    print(c)

    headers = {
    "User-Agent": "PostmanRuntime/7.19.0",
    }
    link = {"link":c}
    url = <link of your php script>
    d = requests.get(url = url, params = link, headers = headers)  #Update the server for tunnel link
    print('request data ---- ', d.text)
    full_time = 3600 * 7
    time.sleep(full_time)
    os.system("taskkill /f /im ngrok.exe")
    time.sleep(10)
    
