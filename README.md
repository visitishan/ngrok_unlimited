# ngrok_unlimited

If you want to make a personal server or self host a website, but your ISP is on a CG-NAT then the DDNS tools won't help. Since the IP assigned to the ISP is from a shared IP, there's nothing much you can do. After several hours of Googling, I found that there are some reverse tunneling tools which can help in this case. One such tool is "NGROK".


### What is NGROK? 
> Ngrok is a multiplatform tunnelling, reverse proxy software that establishes secure tunnels from a public endpoint such as internet to a locally running network service while capturing all traffic for detailed inspection and replay.
>Enter ngrok, a very cool, lightweight tool that creates a secure tunnel on your local machine along with a public URL you can use for browsing your local site. When ngrok is running, it listens on the same port that you're local web server is running on and proxies external requests to your local machine.

However, there are few limitations in NGROK as well. The biggest one is that its not completely free. And if you're using the free version of NGROK, the tunnel link expires after every 8 hours, and you'll have to restart the NGROK service again manually, and again the tunnel link will change. So to avoid this, we merged the Dynamic_DNS tool and NGROK tool. The ngrok.py file starts the NGROK service and reads the current tunnel link and sends it to the myserver.php file that is hosted on a free linux web hosting. The myserver.php file saves the current tunnel link to a text file on the server. Whenever the myserver.php file is accessed from internet, it redirects the connection to the current tunnel link. After every 8 hours, the ngrok.py script kills te running ngrok service and re-starts it. And the new tunnel link is sent to the myserver.php file which is then updated in the text file. 

If you have a better solution, your contributions are welcomed. :)
