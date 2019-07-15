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
![1](https://user-images.githubusercontent.com/25087769/61192742-5fef6680-a6bf-11e9-8ee6-51ac1b48c493.PNG)

* **Paylaşım İndirme**
![Paylaşım indirme](https://user-images.githubusercontent.com/25087769/61192766-8ca37e00-a6bf-11e9-98f7-c3f63560353f.PNG)

* **Paylaşım Beğenme**
![paylasimBegenme2](https://user-images.githubusercontent.com/25087769/61192778-a6dd5c00-a6bf-11e9-8098-d55c643732f6.PNG)

* **Bir kullanıcıyı takip etme**
![Takip etme](https://user-images.githubusercontent.com/25087769/61192792-bb215900-a6bf-11e9-9652-fffd36732e74.PNG)







