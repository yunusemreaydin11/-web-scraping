# Projenin İşleyişi

1. `import requests`: HTTP talepleri yapmak için kullanılan `requests` kütüphanesini içeri aktarır.
2. `from bs4 import BeautifulSoup`: Web sayfasından veri çıkarmak için kullanılan `BeautifulSoup` kütüphanesinden `BeautifulSoup` sınıfını içeri aktarır.
3. `url = "https://www.doviz.com/"`: Scraping yapılacak web sitesinin URL'sini tanımlar.
4. `r = requests.get(url)`: Belirtilen URL'ye bir HTTP GET isteği yapar ve yanıtı `r` değişkenine atar.
5. `soup = BeautifulSoup(r.content, "html.parser")`: HTTP yanıtının içeriğini HTML olarak ayrıştırır ve BeautifulSoup nesnesine dönüştürür.
6. `data = soup.find("span", {"data-socket-key":"gram-altin"}).text.replace(",", ".")`: Web sayfasından altın fiyatını çıkarmak için belirli bir HTML etiketini ve öznitelik değerini kullanarak altın fiyatını bulur ve virgülü noktaya dönüştürerek `data` değişkenine atar.
7. Benzer şekilde, dolar ve euro fiyatlarını `data1` ve `data2` değişkenlerine atar.
8. `entry = input ("Dönüştürmek İstediğiniz Para Birimini Giriniz: ")`: Kullanıcıdan dönüştürmek istediği para birimini girmesini ister.
9. `entry1 = float(input("Miktar Giriniz: "))`: Kullanıcıdan dönüştürmek istediği miktarı girmesini ister ve bunu ondalıklı sayıya dönüştürür.
10. `if entry.upper()=="EUR":` ve devamı: Kullanıcının girdiği para birimine göre dönüşümü hesaplar ve ekrana yazdırır.
11. Son olarak, geçerli olmayan bir para birimi girilirse, kullanıcıya hata mesajı gösterilir.

# Proje'nin Bana Kattıları
### Bu proje ile bs4 ve requests kütüphanelerini kullanarak web scraping işlemini gerçekleştirmeyi öğrendim bunun yanında siteden gelen verileri doğru bir şekilde ayıklayıp istediğim veriye ulaşmamı sağlayacak parser yöntemlerine aşina oldum.
