


from bs4 import BeautifulSoup
 
url = "https://www.haberler.com/magazin/2-ay-once-kim-kardashian-la-bosanan-kanye-west-15559784-haberi/" 

tümkelimeler = []
r= request.get(url)

soup = BeautifulSoup(r.concent,"html.parser")

for kelimegrupları in soup.find_all("p"):
    içerik = kelimegrupları.text 
    kelimeler = içerik.lower().split()

    for kelime in kelimeler:
        tümkelimeler.append(kelime)
        print(kelime)