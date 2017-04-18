from bs4 import BeautifulSoup
import requests
import re
seeds = ['http://en.wikipedia.org/wiki/Cloud_computing','http://en.wikipedia.org/wiki/Server_(computing)']
wiki= 'http://en.wikipedia.org'
keyword = ("computing", "cloud", "virtual", "network", "enterprise", "vm", "hypervisor", "storage", "datacenter", "server")
q = []
##Download all the links from the seed
def getdata(s):
    source = requests.get(s)
    print("getting url", s)
    plain_text = source.text        
    soup = BeautifulSoup(plain_text) 
    for link in soup.findAll('a'):
        links = (link.get('href'))
        links= str(links)
        if 'svg' not in links and 'Talk:' not in links and 'oldid' not in links and 'Special:' not in links and 'printable=yes' not in links and 'Wikipedia:About' not in links and 'pdf' not in links and 'jpg' not in links and '#' not in links and '%' not in links and 'UserLogin' not in links and '.org' not in links and 'signup' not in links and '@' not in links and 'BookSources' not in links and '.png' not in links and 'www' not in links and 'action=edit' not in links:
            if links.startswith('/'):
                q.append(wiki+links)
            if "http://" in links and 'wikipedia' in links:
                q.append(links)
                print("Downloading: "+links)
    return q
##Download each Url one by one from the queued list 
counter = 0
badUrl = []
valid = []
def download(url):
    global counter
    co = 0

    if getdata(url).pop(0) not in badUrl:

        for w in getdata(getdata(url).pop(0)):
        
            source = requests.get(w)
            plain_text = source.text.lower()
            soup = BeautifulSoup(plain_text)

            body = ["".join(content.findAll(text=True)) for content in soup.findAll('p')]
            content = (str(body))

                

            for key in keyword:

                if content.count(key) >= 1 and w not in valid:
                    co +=1
                    print(co, "++")
                    if co >= 2:
                        clean = re.sub("[^a-zA-z]", ' ', content)
                        valid.append(w)
                        save = w.replace("http://en.wikipedia.org/wiki/","").replace("/","")
                        file = open('./'+save+".txt","w", encoding='utf-8')
                        clean = clean.replace("[", "",).replace("]", "").replace('/', "").replace("\\", "")
                        print(clean)
                        file.write(str(clean))
                        seeds.extend([w])
                        counter += 1 
                        print("Counter: ", counter)
                        print("Url appended to the queued", w)
                        file.close()
                        co = 0
                        break                            
                    else:
                        badUrl.append(w)
                        break
    return valid

def main(url):
    while len(url) > 0 and counter < 500:
        for seed in url:
            download(seed)
main(seeds)

