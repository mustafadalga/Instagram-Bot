<h1 align="center">Instagram Bot</h1>

<p align="center">
  <a href="https://github.com/mustafadalga/Instagram-Bot">
    <img src="https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/logo.png" alt="Instagram Bot" width="300">
  </a>
</p>

## :books: Dokümantasyon 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :small_blue_diamond: [İngilizce](https://github.com/mustafadalga/Instagram-Bot) dokümantasyon için  


## Açıklama 
**Selenium framework'ü  kullanılarak geliştirilmiş bir Instagram botu**

## Özellikler
  :large_blue_circle: **Bir kullanıcının tüm gönderilerini indirme**  
  :large_blue_circle: **Bir kullanıcının tüm gönderilerini beğenme veya beğenmekten vazgeçme**  
  :large_blue_circle: **Toplu takipten çıkma**  
  :large_blue_circle: **Bir gönderiye toplu yorum yapma**  
  :large_blue_circle: **Takip etmeyen kullanıcıları takipten çıkma**  
  :large_blue_circle: **Toplu mesaj silme**  
  :large_blue_circle: **Öne çıkan hikaye indirme**  
  :large_blue_circle: **Hikaye indirme**  
  :large_blue_circle: **Tek gönderi indirme**  
  :large_blue_circle: **IG TV video indirme**  
  :large_blue_circle: **Bir Kullanıcının takipçilerini takip etme**   
  :large_blue_circle: **Bir dosyadaki tüm kullanıcıları takip etme**  
  :large_blue_circle: **Bir gönderiyi beğenen kullanıcıları takip etme**  
  :large_blue_circle: **Etikete Göre kullanıcıları takip etme**  
  :large_blue_circle: **Etikete göre gönderileri beğenme**   
  :large_blue_circle: **Tek gönderi beğenme veya beğenmekten vazgeçme**   
  :large_blue_circle: **Bir gönderiye yorum yapma**  
  :large_blue_circle: **Kullanıcı takip etme veya takip etmekten vazgeçme**  
  :large_blue_circle: **Kullanıcı engelleme veya engel kaldırma**   
  

## Diğer Özellikler
  :large_blue_circle: İngilizce ve Türkçe olarak 2 dil desteği eklenmiştir.  
  :large_blue_circle: Tarayıcı penceresi gizli veya açık bir şekilde çalıştırabilmek için 2 seçenek eklenmiştir.  
  :large_blue_circle: Ayarlar menüsü eklenmiştir.Ayarlar menüsü ile dil ve tarayıcı ayarları görüntülenebilir ve değişiklikler yapılabilir.        
    

## Ayrıntılar

:large_blue_diamond:	 İnstagram oturumunuzu açarak yukarıdaki özellikleri kullanabilirsiniz.  
:large_blue_diamond:	 2 adımlı doğrulama ile güvenlik sağlanmış hesaplarda da instagram girişi yapılabilmektedir.  
:large_blue_diamond:	 Proje geliştirme aşamasında 2 adımlı doğrulama kodu sadece telefona gönderildiği için ,2 adımlı doğrulama özelliği , doğrulama kodunun telefon numarasına gönderilme durumuna göre geliştirilmiştir.  
:large_blue_diamond:	 Varsayılan uygulama dili İngilizce'dir. 

## Yapılandırma Ayarları
 :gear:	 Proje webdriver olarak Firefox tarayıcısını kullanmaktadır.Bu yüzden Firefox'un kurulu olması gerekmektedir.  
 :gear:	 Firefox'un kullanılabilmesi için [webdriver](https://github.com/mozilla/geckodriver/releases) indirilmeli ve indirilen webdriver'in dizin yolu [config.json](https://github.com/mustafadalga/Instagram-Bot/blob/master/config.json) içerisinde tanımlanmalıdır.


* ### Config Ayarları

:gear: **driver_path:** Webdriver dizin yolunu belirtir.  
:gear: **headless:** Tarayıcının görünüp görünmemesini belirtir.Varsayılan değeri:**true**   
:gear: **language:** Uygulamanın varsayılan dilini belirtir.    
:gear: **languages:** Her bir uygulama dili için ayarlar , menü ve uyarı mesajlarını barındırır.  
:gear: **time:** **time.sleep()** kullanılan yerler için işlem bekleme sürelerini belirtir.  



* ### Windows için paketlerin kurulumu
```
python -m pip install -r .\requirements.txt
```

## Kullanım
:small_blue_diamond: Kullanıcıdan bilgi girişi yapması istenilen herhangi bir işlem/konumdan ana menüye dönmek için '**menu**' komutu kullanılmalıdır.

```
python instagram.py
```



### Notlar
:small_blue_diamond: Gönderi beğenme , kullanıcı takip etme , toplu yorum yapma gibi işlemlerde hesabınızın engellenmemesi için işlem süre aralıkları uzun süreler olarak ayarlandı.   
:small_blue_diamond: Yapılan işlemler için belirlenen işlem süreleri [config.json](https://github.com/mustafadalga/Instagram-Bot/blob/master/config.json) dosyası içerisinden değiştirilebilir.  
:small_blue_diamond: Sadece Windows işletim sisteminde test edilmiştir.  
:small_blue_diamond: Python versiyonu:3.8.1  


### Kullanılan Teknolojiler
 * Python
 * Selenium
 * Javascript

## Ekran Görüntüleri

:small_blue_diamond: Ana menü

![Ana menü](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/mainMenu.PNG)


:small_blue_diamond: Gönderileri indirme

![Gönderileri indirme](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/postsDownload.PNG)

:small_blue_diamond: Gönderileri beğenme

![Gönderileri beğenme](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/postsLike.PNG)

:small_blue_diamond: Toplu takipten çıkma

![Toplu takipten çıkma](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/allUnfollow.PNG)


:small_blue_diamond: Toplu yorum yapma

![Toplu yorum yapma](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/bulkComment.PNG)

:small_blue_diamond: Toplu mesaj silme

![Toplu mesaj silme](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/assets/img/messagesDeleted.PNG)


## License
 [![License](https://img.shields.io/github/license/mustafadalga/Instagram-Bot)](https://github.com/mustafadalga/Instagram-Bot/blob/master/LICENSE)