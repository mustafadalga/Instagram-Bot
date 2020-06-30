```
  _____           _                                    ____        _   
 |_   _|         | |                                  |  _ \      | |  
   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ 
   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|
  _| |_| | | \__ \ || (_| | (_| | | | (_| | | | | | | | |_) | (_) | |_ 
 |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|
                            __/ |                                      
                           |___/                                       
```          

## Açıklama
**Selenium framework'ü  kullanılarak kodlanmış bir Instagram botu**  

### Ayrıntı

* İnstagram oturumunu açarak aşağıdaki özellikleri kullanabilirsiniz.
* 2 adımlı doğrulama ile güvenlik sağlanmış hesaplarda da instagram girişi yapılabilmektedir.
* Script kodlama aşamasında 2 adımlı doğrulama kodu sadece telefona gönderildiği için , doğrulama kodunun telefon numarasına gönderildiği olasılığına göre kodladım.




### Özellikler

  :heavy_check_mark: **Bir kulllanıcının tüm paylaşımlarını indirme**  
  :heavy_check_mark: **Bir kulllanıcının tüm paylaşımlarını beğenme**  
  :heavy_check_mark: **Bir kulllanıcının tüm paylaşımlarını beğenmekten vazgeçme**  
  :heavy_check_mark: **Bir fotoğrafı indirme**  
  :heavy_check_mark: **Bir videoyu indirme**  
  :heavy_check_mark: **Bir paylaşımı beğenme**  
  :heavy_check_mark: **Bir paylaşımı beğenmekten vazgeçme**  
  :heavy_check_mark: **Bir kullanıcıyı takip etme**  
  :heavy_check_mark: **Bir kullanıcıyı takip etmekten vazgeçme**  
  :heavy_check_mark: **Bir kullanıcıyı engelleme**  
  :heavy_check_mark: **Bir kullanıcının engelini kaldırma**  
  :heavy_check_mark: **İnstagram oturumunu kapatma**  
  
  
### Kurulum
 * Script web driver olarak Firefox tarayıcısını kullanmaktadır.Bu yüzden Firefox kurulu olması gerekmektedir.
 * Firefox'un kullanılabilmesi için [bu linkteki](https://github.com/mozilla/geckodriver/releases)  motoru indirip yolunu script'te belirtmeniz gerekmektedir.

* Windows için kurulum
```
python -m pip install -r .\requirements.txt
```

### Kullanım
```
python instagram.py
```
* Menü'den seçilen herhangi bir işlemden tekrar ana menüye dönmek için '**menu**' komutu kullanılmalıdır.


### Notlar
* Sadece Windows işletim sisteminde test edilmiştir.
* Python versiyonu:3.7.2
* Durum beğenme , takip etme gibi bazı işlemler sırasındaki süre aralığı instagram tarafından engellenmemek için uzun ayarlandı.
* İşlemler için belirlenen süreler kendi cihazımın ve  internetimin hızına göre ayarlanmıştır.Kendinize göre değiştirebilirsiniz.

### Uyarı
* **Beğenme , takip etme gibi işlemlerde süre aralıklarını azaltırsanız,instagram tarafından engellenebilirsiniz.**

### Ekran Görüntüleri


* **Giriş Ekranı**
![Giriş Ekranı](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/goruntuler/giris.png)

* **Paylaşım İndirme**
![Paylaşım indirme](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/goruntuler/paylasim-indirme.png)

* **Paylaşım Beğenme**
![paylasimBegenme2](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/goruntuler/paylasim-begenme-2.png)

* **Bir kullanıcıyı takip etme**
![Takip etme](https://raw.githubusercontent.com/mustafadalga/Instagram-Bot/master/goruntuler/kullanici-takip-etme.png)







