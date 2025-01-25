print("=== Task 1 ===")
import requests
import re,csv

url1='https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1'
response = requests.get(url1)
spotlist = response.json()     
data1 = spotlist['data']      
results = data1['results']     


url2='https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'
response = requests.get(url2)
mrtlist = response.json()   
data2 = mrtlist['data']                            

distlist=['中正區','萬華區','中山區','大同區','大安區','松山區','信義區','士林區','文山區','北投區','內湖區','南港區']
spotContent = []
mrtContent = []

for i in range(0,len(results)):      
    idx = 0
    spotlist=[]
    spotlist.insert(idx,results[i]['stitle'])            
    idx=idx+1
    ser_no = results[i]['SERIAL_NO']
    for j in range(0,len(data2)):                        
       if data2[j]['SERIAL_NO']==ser_no:
           for k in range(0,len(distlist)):
               role= re.compile(distlist[k])
               if role.search(data2[j]['address']) != None:
                       spotlist.insert(idx,distlist[k])
                       idx=idx+1
                       j = j +len(data2)
                       break

    spotlist.insert(idx,results[i]["longitude"])           
    idx = idx+1
    spotlist.insert(idx,results[i]["latitude"])            

    
    imglist=results[i]["filelist"]                         
    imglist_sub =imglist[4:len(imglist)-4]
    imgurl = 'http'+ imglist_sub[0:imglist_sub.find('http')]
    idx = idx + 1
    spotlist.insert(idx,imgurl)

    spotContent.append(spotlist)                                

mrt_st =[]                                                
for h in range (0,len(data2)):  
    mrt_st.insert(h,data2[h]['MRT'])
mrt_st=list(dict.fromkeys(mrt_st))      

for m in range (0,len(mrt_st)):
    idx1 = 0
    mrtlist=[]
    mrtlist.insert(idx1,mrt_st[m])                            
    for n in range(0,len(data2)):                             
        if data2[n]['MRT']==mrt_st[m]:
            for p in range (0,len(results)):
                if results[p]['SERIAL_NO'] == data2[n]['SERIAL_NO']:   
                    idx1 = idx1+1
                    mrtlist.insert(idx1,results[p]['stitle'])
    mrtContent.append(mrtlist)                                              


with open("spot.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(spotContent)
with open("mrt.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(mrtContent)

print("=== Task 2 ===")

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req  

csvContent = []

def getData(url):
    request=req.Request(url, headers={
        "cookie":"over18=1", 
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") 

    titles=root.find_all("div",class_="title") 
    cuonts=root.find_all("div",class_="nrec") 

    
    pushcnt = []
    for cnt in cuonts:
        if not cnt.get_text():
            pushcnt.append(int(0))
        else:
            pushcnt.append(int(cnt.get_text()))
    articleIndex = 0
    for title in titles:
        if title.a != None: 
            result = []
            result.append(title.a.string)
            subhtml = requests.get("https://www.ptt.cc"+title.a['href'])    
            
            session = requests.Session()
            session.max_redirects = 100
            session.get("https://www.ptt.cc")
            subhtml.encoding = "utf-8"
            subartical=bs4.BeautifulSoup(subhtml.text,"html.parser")
            result.append(pushcnt[articleIndex])
            
            subarticals = subartical.find_all("div",class_="article-metaline")  
            if len(subarticals)!=0:
                i=0
                for itemText in subarticals:
                    if i==2 : 
                        result.append(itemText.find('span', class_='article-meta-value').string)
                    i=i+1
            else:
                result.append("")
            csvContent.append(result)    
        articleIndex = articleIndex+1

    
    nextLink=root.find("a",string="‹ 上頁") 
    return nextLink["href"]


# 主程序
pageURL="https://www.ptt.cc/bbs/Lottery/index.html"  
count=0
while count<3:
    pageURL="https://www.ptt.cc"+getData(pageURL)  
    count=count+1

with open("article.csv", mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(csvContent)