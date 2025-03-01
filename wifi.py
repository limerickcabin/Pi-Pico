import time, network, socket, json, ntptime, sys, requests

def getTime():
    return time.time()+6*60*60 #why does time() not return zulu?

def printTime(now):
    t=time.gmtime(now)
    h=t[3]
    m=t[4]
    s=t[5]
    hstr=""
    mstr=""
    sstr=""
    if h<10:
        hstr="0"
    if m<10:
        mstr="0"
    if s<10:
        sstr="0"
    hstr=hstr+str(h)
    mstr=mstr+str(m)
    sstr=sstr+str(s)
    print(hstr+":"+mstr+":"+sstr+"Z")

def checkBoat():
    #wifi credentials are stored in a file
    #example '{"site": "web.com", "ssid": "wifiSSID", "pwd": "wifiPWD"}'
    r=open("creds.txt","r")
    cred=json.load(r)
    site=cred["site"]
    ssid=cred["ssid"]
    pwd =cred["pwd"]
    r.close()

    #connect to wifi
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid,pwd)
    #wlan.connect("badSSID",cred["pwd"])

    #wait for connection
    t=0
    while True:
        if wlan.status()==3:
            break
        time.sleep(1)
        t=t+1
        if t>10:
            print("could not connect to wifi")
            wlan.active(False)
            return
    #print("connected")

    #the nano w comes up with its clock set to 1/1/2021
    jan_1_22=time.mktime((2022,1,1,0,0,0,5,1))
    now=getTime()
    if now<jan_1_22:
        print("getting time") #time is before 2022, set clock
        try:
            ntptime.settime()
            now=getTime()
        except:
            print("ntptime.settime failed")
            wlan.disconnect()
            wlan.active(False)
            return
    printTime(now)

    #print("requesting data")
    try:
        url=site+"/getJSON.php?file=bsec2.dat&rows=1"
        #print(url)
        response=requests.get(url).content
    except:
        print("server did not respond")
        wlan.disconnect()
        wlan.active(False)
        return
    wlan.disconnect()
    wlan.active(False)

    #print(response)
    try:
        j=json.loads(response)          #JSON object
        r=j["results"][0]               #results[0]
        then=float(r["time"])           #results[0].time
        temp=float(r["tmp" ])           #results[0].tmp
        
        temp=round(temp)
        age=round((now-then)/60)
        print(temp,"degrees",age,"minutes old")

        if temp>32:
            state="boat seems OK"
        else:
            state="temperature is low"
        if age>30:
            state="data is stale, check power"
    except:
        state="received invalid json data from server"
    print(state)
#end

def main():
    while True:
        then=getTime()
        checkBoat()
        print()
        now=getTime()
        time.sleep(5*60-(now-then))

main()