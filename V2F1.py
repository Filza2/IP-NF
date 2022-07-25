from requests import get,post
import socket
gr="\033[1;32m";re="\033[1;31m";cy="\033[1;36m";do='\033[1;37m';so='\033[1;35m';po='\033[1;38m'
print(f"""
{gr}  ██╗░░░██╗██████╗░███████╗░░███╗░░
{po}  ██║░░░██║╚════██╗██╔════╝░████║░░
{re}  ╚██╗░██╔╝░░███╔═╝█████╗░░██╔██║░░
{cy}  ░╚████╔╝░██╔══╝░░██╔══╝░░╚═╝██║░░
{po}  ░░╚██╔╝░░███████╗██║░░░░░███████░ 

{re}      ░ By @TweakPY - @vv1ck ░

{gr}- {po}1*[Get Ip from site ]
{gr}- {po}3*[Get ip info && get your ip ]
{gr}- {po}4*[Get ip info in json with ipinfo.io ]
{gr}- {po}99*[Exit Program]
""")     
mod=int(input("[?] Enter Number : "))         
if mod==1:         
    IPS=input('[?] Enter The Site  : ') # Like Google.com
    sop=socket.gethostbyname(IPS)
    print(re+sop)
elif mod==2:
    j=int(input(po+"""
[1] Get My IP & data
[2] Get Location & data From IP Target\n:"""))        
    if j==1:
        GetLocate=get("https://get.geojs.io/v1/ip/geo/"+get("https://get.geojs.io/v1/ip.json").json()["ip"]+".json").json()
        print(re+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("My IP Address      : " + GetLocate["ip"])
        print("My Location        : " + GetLocate["country"])
        print("My Country Code    : " + GetLocate["country_code"])
        print("Service Provider   : " + GetLocate["organization_name"])
        print("Time Zone          : " + GetLocate["timezone"])
        print("Longitude On a map : " + GetLocate["longitude"])
        print("Latitude On a map  : " + GetLocate["latitude"])
    elif j==2:        
        GetLocate=get("https://get.geojs.io/v1/ip/geo/"+input("[?] Enter The ip : ")+".json").json()
        print(re+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Target IP Address         : " + GetLocate["ip"])
        print("Target Location           : " + GetLocate["country"])
        print("Target Country Code       : " + GetLocate["country_code"])
        print("Target Time Zone          : " + GetLocate["timezone"])
        print("Target Longitude On a map : " + GetLocate["longitude"])
        print("Target Latitude On a map  : " + GetLocate["latitude"])
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
elif mod==3:         
    ip=input("[?] Enter The ip : ")
    r=get(f'https://ipinfo.io/{ip}').text
    print(re+r)
    with open(f"{ip}_info.json", 'a') as x:
        x.write(f'{r}')
elif mod==99:quit(0)
else:quit(0)