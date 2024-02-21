import requests
from bs4 import BeautifulSoup

url = "https://www.doviz.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


data = soup.find("span", {"data-socket-key":"gram-altin"}).text.replace(",", ".")
data1 = soup.find("span", {"data-socket-key":"USD"}).text.replace(",", ".")
data2 = soup.find("span", {"data-socket-key":"EUR"}).text.replace(",", ".")

data_top = [data1, data2, data]



entry = input ("Dönüştürmek İstediğiniz Para Birimini Giriniz: ")
entry1 = float(input("Miktar Giriniz: "))




if entry.upper()=="EUR":
    ans = float(data2) * entry1
    print(f"{entry1} EURO =  {ans} TL Yapıyor")
elif entry.upper()=="USD":
    ans = float(data1) * entry1
    print(f"{entry1} USD =  {ans} TL Yapıyor")
elif entry.upper()=="ALTIN":
    ans = float(data) * entry1
    print(f"{entry1} GR ALTIN =  {ans} TL Yapıyor")
else : 
    print("Geçersiz Para Birimi Girdiniz Lütfen USD-EUR-ALTIN Anahtar Kelimelerini Kullanınız!")



  

