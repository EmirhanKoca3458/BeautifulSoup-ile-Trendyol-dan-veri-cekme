import requests
from bs4 import BeautifulSoup 


url = "https://www.trendyol.com/cep-telefonu-x-c103498"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

sıra = 1
liste = soup.find_all("div",attrs={"class":"p-card-wrppr with-campaign-view"}) 



for telefon in liste:
    name = telefon.find("div",{"class":"product-down"}).h3.text
    price = telefon.find("div",{"class":"prc-box-dscntd"}).text.strip("TL")
    evaluation = telefon.find("div",{"class":"ratings-container"}).text.strip("()") 
    
   
    
    print("Telefon\n",sıra,"İsmi:",name,"Fiyatı:",price,"TL","Değerlendirme Sayısı:","Kişi değerlendirmiş")
    sıra += 1
    



