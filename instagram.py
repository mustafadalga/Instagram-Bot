from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime
import os
import urllib.request
import requests
import getpass
from termcolor import colored
from colorama import init
import threading

class Instagram():
    def __init__(self):
        init(convert=True)
        self.script()
        self.threadOlustur()
        self.girisYapildimi = False
        self.tarayiciAcildimi = False
        self.aktifKullanici = ""
        self.BASE_URL = "https://www.instagram.com/"
        self.girisYap()

    def script(self):
        print("")
        print(self.uyariOlustur("  _____           _                                    ____        _   ", 1))
        print(self.uyariOlustur(" |_   _|         | |                                  |  _ \      | |  ", 1))
        print(self.uyariOlustur("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ", 1))
        print(self.uyariOlustur("   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|", 1))
        print(self.uyariOlustur("  _| |_| | | \__ \ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ ", 1))
        print(self.uyariOlustur(" |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|", 1))
        print(self.uyariOlustur("                            __/ |                                      ", 1))
        print(self.uyariOlustur("                           |___/                                       ", 1))
        print(self.uyariOlustur("# ==============================================================================", 1))
        print(self.uyariOlustur("# author      	:", 1) + "Mustafa Dalga")
        print(self.uyariOlustur("# linkedin    	:", 1) + "https://www.linkedin.com/in/mustafadalga")
        print(self.uyariOlustur("# github      	:", 1) + "https://github.com/mustafadalga")
        print(self.uyariOlustur("# email      	:", 1) + "mustafadalgaa < at > gmail[.]com")
        print(self.uyariOlustur("# date        	:", 1) + "15.07.2019")
        print(self.uyariOlustur("# version     	:", 1) + "2.0")
        print(self.uyariOlustur("# python_version:", 1) + "3.8.1")
        print(self.uyariOlustur("# ==============================================================================", 1))
        print("")

    def menu(self):
        print("")
        print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
        print("")
        print(self.uyariOlustur(" 1 -) Tüm paylaşımları indir", 3))
        print(self.uyariOlustur(" 2 -) Tüm paylaşımları beğen", 3))
        print(self.uyariOlustur(" 3 -) Tüm paylaşımları beğenmekten vazgeç", 3))
        print(self.uyariOlustur(" 4 -) Fotoğraf indir(tek fotoğraf)", 3))
        print(self.uyariOlustur(" 5 -) Video indir(tek video)", 3))
        print(self.uyariOlustur(" 6 -) Paylaşım beğen (tek paylaşım)", 3))
        print(self.uyariOlustur(" 7 -) Paylaşım beğenmekten vazgeç(tek paylaşım)", 3))
        print(self.uyariOlustur(" 8 -) Kullanıcı takip et", 3))
        print(self.uyariOlustur(" 9 -) Kullanıcı takip etmekten vazgeç", 3))
        print(self.uyariOlustur(" 10-) Kullanıcı engelle", 3))
        print(self.uyariOlustur(" 11-) Kullanıcı engel kaldır", 3))
        print(self.uyariOlustur(" 12-) İnstagram çıkış yap", 3))
        print(self.uyariOlustur(" 13-) Uygulama'dan çıkış yap", 3))
        print("")
        self.islemSec()

    def islemSec(self):
        secim = input(" İşlem yapmak için bir seçim yapınız >> ").strip()
        if secim:
            try:
                secim = int(secim)
                if 0 < secim < 24:
                    self.secilenIslem(secim)
                    if secim == 1 or secim == 2 or secim == 3 or secim == 8 or secim == 9 or secim == 10 or secim == 11 or secim == 15:
                        self.profilSec(secim)
                    elif secim == 4:
                        self.fotografIndir()
                    elif secim == 5:
                        self.videoIndir()
                    elif secim == 6:
                        self.paylasimBegen()
                    elif secim == 7:
                        self.paylasimBegen(False)
                    elif secim == 12:
                        self.cikisYap()
                    elif secim == 13:
                        self.quit()
                    elif secim == 14:
                        self.kullaniciListesiSec(secim)
                    elif secim == 16:
                        self.paylasimBegenenleriTakipEt()
                    elif secim == 17:
                        self.takipEtmeyenleriTakiptenCik()
                    elif secim == 18:
                        self.topluTakiptenCik()
                    elif secim==19:
                        self.topluMesajSilme()
                    elif secim==20:
                        self.hikayeIndirme()
                    elif secim==21:
                        self.oneCikanHikayeIndir()
                    elif secim==22:
                        self.gonderiYorumYapma()
                    elif secim==23:
                        self.gonderiTopluYorumYapma()
                else:
                    print(self.uyariOlustur("[-] Lütfen geçerli bir seçim yapınız!", 2))
                    self.islemSec()
            except Exception as e:
                print(e)
                print(self.uyariOlustur("[-] Yapılacak işlem,  başındaki sayıya göre seçilmeli.", 2))
                self.islemSec()
        else:
            self.islemSec()

    def topluMesajSilme(self):
        print("[*] Toplu mesaj silme işlemi başladı.")
        try:
            self.driver.get(self.BASE_URL+'direct/inbox/')
            time.sleep(5)
            devamEtsinMi=True
            silinenMesajlar = set()
            islemIndex=0
            while devamEtsinMi:
                mesajListesi = self.driver.find_elements_by_css_selector("div.N9abW  a.rOtsg")
                if len(mesajListesi) == 0:
                    print("[*] Mesaj kutusunda mesaj bulunmamaktadır.")
                    break
                for mesaj in mesajListesi:
                    if mesaj not in silinenMesajlar:
                        silinenMesajlar.add(mesaj)
                        kullaniciAdi=mesaj.find_element_by_css_selector("._7UhW9.xLCgt.MMzan.KV-D4.fDxYl").text
                        islemIndex=islemIndex+1
                        print(self.uyariOlustur("[*] {index} -) {kullaniciAdi} ile yapılan mesajlaşma silinecek.".format(index=islemIndex,kullaniciAdi=kullaniciAdi), 1))
                        mesaj.click()
                        time.sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button").click()
                        time.sleep(1)
                        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button").click()
                        time.sleep(2)
                        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button[1]").click()
                        print(self.uyariOlustur("[*] {index} -) {kullaniciAdi} ile yapılan mesajlaşma başarıyla silindi.".format(index=islemIndex,kullaniciAdi=kullaniciAdi), 1))
                        time.sleep(10)
                    break
        except Exception as error:
            print(self.uyariOlustur('[-] Toplu mesaj  aşağıda kaydırma işlemi sırasında bir hata oluştu: {hata}'.format(hata=str(error)),2))

        print("[*] Toplu mesaj silme işlemi tamamlandı.")


    def yorumVarMi(self,yorum):
        if len(yorum)>0:
            return True
        else:
            return False

    def yorumUzunlukBelirle(self,yorum):
        return yorum[0:250]

    def yorumYap(self,yorum):
        try:

            textarea = self.driver.find_element_by_class_name('Ypffh')
            self.inputTemizle(textarea)
            textarea.click()
            textarea = self.driver.find_element_by_class_name('Ypffh')

            textarea.send_keys(yorum)
            textarea.send_keys(Keys.ENTER)
        except Exception as error:
            print(self.uyariOlustur( "[-] {url} gönderisine yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

    def rastgeleYorumGetir(self):
        try:
            return requests.get("http://metaphorpsum.com/paragraphs/1/1").text
        except Exception as error:
            print(self.uyariOlustur("[-] Rastgele yorum getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)),2))

    def yorumLimitiAsildiMi(self,yorumSayisi):
        if yorumSayisi>50:
            return True
        else:
            return False

    def dosyaİceriginiAl(self,dosya):
        try:
            icerik=set()
            with open(dosya, "r", encoding="utf-8") as satirlar:
                for satir in satirlar:
                    if len(satir.strip())>0:
                        icerik.add(satir)
            return icerik
        except Exception as error:
            print(self.uyariOlustur("[-] Seçilen dosyanın yüklenme işlemi sırasında bir hata oluştu:" + str(error), 2))
            return False

    def dosyaİcerigiAlindiMi(self,icerik):
        if icerik:
            return True
        else:
            return False


    def gonderiTopluYorumYapma(self,url=None,yorumSayisi=None,secilenIslem=None):
        try:
            if url is None and yorumSayisi is None and secilenIslem is None:
                print(self.uyariOlustur("Seçilen İşlem >>> Bir gönderiye toplu yorum yapma", 1))

            if not url:
                url = input("Yorum yapmak istediğiniz gönderi url'isini giriniz >> ").strip()

                if self.urlKontrol(url):
                    print("[*] {url}  gönderisine yönlendiriliyor...".format(url=url))
                    self.driver.get(url)
                    time.sleep(3)

                    if not self.sayfaMevcutMu():
                        print(self.uyariOlustur("[-] {url} url'sine ulaşılamadı!".format(url=url), 2))
                        self.gonderiTopluYorumYapma()

                    if self.hesapGizliMi():
                        print(self.uyariOlustur(
                           "[-] {url} gönderisinin sahibinin hesabı gizli hesap olduğundan dolayı toplu yorum yapma işlemi gerçekleştirilemiyor".format(
                               url=url), 2))
                        self.gonderiTopluYorumYapma()
                else:
                    print(self.uyariOlustur("[-] Gönderi url'si girmediniz!!", 2))
                    self.gonderiTopluYorumYapma()

            if not yorumSayisi:
                yorumSayisi = input("Yapmak istediğiniz yorum sayısını giriniz >> ").strip()
                if yorumSayisi.isnumeric() and int(yorumSayisi)>0:
                    yorumSayisi=int(yorumSayisi)
                    if self.yorumLimitiAsildiMi(yorumSayisi):
                        yorumSayisi=50
                        print(self.uyariOlustur("[*] En fazla 50 yorum yapabilirsiniz.Yorum sayısı 50 olarak belirlenmiştir!", 2))
                else:
                    print(self.uyariOlustur("[-] Yapmak istediğiniz yorum sayısını girmediniz!", 2))
                    self.gonderiTopluYorumYapma(url=url, yorumSayisi=None, secilenIslem=None)

            if not secilenIslem:
                print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                print(self.uyariOlustur("Uygulama ile oluşturan rastgele yorumlar ile işlem yapmak için 1,", 3))
                print(self.uyariOlustur("Txt dosyasından olarak oluşturduğunuz yorumlar ile işlem yapmak için 2 giriniz.", 3))
                print("")
                secilenIslem = str(input("Uygulama ile oluşturan rastgele yorumlar seçilsin mi? >> ").strip())

            if secilenIslem == "1":
                print(self.uyariOlustur("Seçilen İşlem >>> Uygulama ile oluşturan rastgele yorumlar ile işlem yapma",1))
                print("[*] {url}  gönderisine toplu yorum yapma işlemi başladı.".format(url=url))
                try:
                    for i in range(yorumSayisi):
                        yorum=self.rastgeleYorumGetir()
                        yorum=self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        print("[*] {index}.yorum yapıldı.".format(index=i+1))
                        time.sleep(15)
                except Exception as error:
                    print(error)
            elif secilenIslem == "2":
                print(self.uyariOlustur("Seçilen İşlem >>> Txt dosyasından olarak oluşturduğunuz yorumlar ile işlem yapma",1))
                dosya = self.dosyaSec(1)
                yorumlar = self.dosyaİceriginiAl(dosya)
                if self.dosyaİcerigiAlindiMi(yorumlar):
                    print("[*] {url}  gönderisine toplu yorum yapma işlemi başladı.".format(url=url))
                    for index,yorum in enumerate(yorumlar):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        print("[*] {index}.yorum yapıldı.".format(index=index + 1))
                        if (index+1)==yorumSayisi:
                            break
                        time.sleep(15)
                else:
                    self.gonderiTopluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=secilenIslem)
            else:
                print(self.uyariOlustur("[-] Bir seçim yapmadınız!.Lütfen yapmak istediğiniz işlemin numarasını giriniz!", 2))
                print("")
                self.gonderiTopluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=None)

        except Exception as error:
            print(self.uyariOlustur("[-] {url} gönderisine toplu yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(url=url,hata=str(error)), 2))
            self.gonderiTopluYorumYapma()

        print("[*] {url}  gönderisine toplu yorum yapma işlemi tamamlandı.".format(url=url))


    def gonderiYorumYapma(self,url=None,yorum=None):
        try:
            if not (url and yorum):
                print(self.uyariOlustur("Seçilen İşlem >>> Bir gönderiye yorum yapma", 1))

            if not url:
                url = input("Yorum yapmak istediğiniz gönderi url'isini giriniz >> ").strip()
            if not yorum:
                yorum = input("Yorumunuzu giriniz >> ").strip()

            if self.urlKontrol(url):
                self.driver.get(url)
                time.sleep(5)

                if not self.sayfaMevcutMu():
                    print(self.uyariOlustur("[-] İndirmek istediğiniz öne çıkan hikayenin url'sine ulaşılamadı!", 2))
                    self.gonderiYorumYapma()

                if not self.hesapGizliMi():
                    if self.yorumVarMi(yorum):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        print("[*] {url}  gönderisine yorum yapma işlemi başladı.".format(url=url))
                        self.yorumYap(yorum)
                        print("[*] {url}  gönderisine yorum yapma işlemi tamamlandı.".format(url=url))
                        self.gonderiYorumYapma()
                    else:
                        print(
                            self.uyariOlustur("[-] Yorum girişi yapmadınız!", 2))
                        self.gonderiYorumYapma(url=url,yorum=None)
                else:
                    print(self.uyariOlustur(
                        "[-] {url} gönderisinin sahibinin hesabı gizli hesap olduğundan dolayı yorum yapma işlemi gerçekleştirilemiyor".format(url=url), 2))
                    self.gonderiYorumYapma()
            else:
                print(self.uyariOlustur("[-] {url} url'sine ulaşılamadı!".format(url=url), 2))
                self.gonderiYorumYapma(url=None,yorum=yorum)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] {url} gönderisine yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(url=url,hata=str(error)), 2))
            self.gonderiYorumYapma()

    def hikayeVarMi(self):
        try:
            durum=self.driver.find_element_by_css_selector("div.RR-M-").get_attribute("aria-disabled")
            if durum=="false":
                return True
            else:
                return False
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Hikaye olup olmadığı işleminin kontrolü sırasına bir hata oluştu: {hata}".format(hata=str(error)), 2))


    def hikayeVideoMu(self):
        try:
            self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5")
            return True
        except:
            return False

    def hikayeSayisiGetir(self):
        try:
            hikayeSayisi=self.driver.find_elements_by_css_selector("div.w9Vr-  > div._7zQEa")
            return len(hikayeSayisi)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Hikaye sayısı getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

    def hikayeleriGetir(self):
        try:
            hikayeler={
                "video":[],
                "fotograf":[]
            }
            for i in range(self.hikayeSayisiGetir()):
                if self.hikayeVideoMu():
                    video_url=self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5 > source").get_attribute("src")
                    print(self.uyariOlustur("[*] Video hikaye url:" + str(video_url), 1))
                    hikayeler["video"].append(video_url)
                else:
                    foto_srcset = str(self.driver.find_element_by_css_selector("div.qbCDp >  img.y-yJ5").get_attribute("srcset"))
                    foto_url=(foto_srcset.split(",")[-1]).split(" ")[0]
                    print(self.uyariOlustur("[*] Fotoğraf hikaye url:" + str(foto_url), 1))
                    hikayeler["fotograf"].append(foto_url)
                btn_ileri=self.driver.find_element_by_css_selector("button.ow3u_")
                btn_ileri.click()
                time.sleep(1)
            return hikayeler
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Hikayeleri getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))


    def sayfaMevcutMu(self):
        if "Sorry, this page isn't available." not in self.driver.page_source:
            return True
        else:
            return False

    def hesapGizliMi(self):
        if "This Account is Private" in self.driver.page_source:
            return True
        else:
            return False

    def hikayeIndirme(self):
        try:
            print(self.uyariOlustur("Seçilen İşlem >>> Bir kullanıcının hikayelerini indirme", 1))

            kullanici = input("Hikayelerini indirmek istediğiniz profilin kullanıcı adınız giriniz >> ").strip()
            self.driver.get(self.BASE_URL + kullanici)
            time.sleep(5)

            if not self.sayfaMevcutMu():
                print(self.uyariOlustur("[-] " + kullanici + " kullanıcısına ulaşılamadı", 2))
                self.hikayeIndirme()

            if not self.hesapGizliMi():
                if self.hikayeVarMi():
                    self.driver.find_element_by_css_selector("div.RR-M-").click()
                    time.sleep(3)
                    hikayeler = self.hikayeleriGetir()
                    self.dosyaIndir(hikayeler)
                    print("[*] {kullanici} kullanıcısının hikayelerini indirme işlemi tamamlandı.".format(
                        kullanici=kullanici))
                else:
                    print(self.uyariOlustur("[-] Hikaye bulunamadı!",2))
            else:
                print(self.uyariOlustur("[-] {kullanici} adlı kişinin hesabı gizli hesap olduğundan takipçileri takip edilemiyor!".format(kullanici=kullanici),2))

        except Exception as error:
            print(self.uyariOlustur("[-] Hikayeleri indirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.hikayeIndirme()

    def elemanMevcutMu(self,secici,seciciTuru):
        try:
            self.driver.find_element_by_xpath(secici)
            return True
        except:
            return False


    def oneCikanHikayeIndir(self):
        try:
            print(self.uyariOlustur("Seçilen İşlem >>> Bir kullanıcının öne çıkan hikayelerini indirme", 1))
            url = input("Öne çıkan hikaye url giriniz >> ").strip()
            if self.urlKontrol(url):
                self.driver.get(url)
                time.sleep(5)

                if not self.sayfaMevcutMu():
                    print(self.uyariOlustur("[-] İndirmek istediğiniz öne çıkan hikayenin url'sine ulaşılamadı!", 2))
                    self.oneCikanHikayeIndir()

                print("[*] {url}  öne çıkan hikayesini indirme işlemi başladı".format(url=url))
                btn_oynat=self.driver.find_element_by_css_selector("button._42FBe")
                btn_oynat.click()
                time.sleep(1)
                hikayeler = self.hikayeleriGetir()
                self.dosyaIndir(hikayeler)
                print("[*] {url}  öne çıkan hikayesini indirme işlemi tamamlandı.".format(url=url))
            else:
                print(self.uyariOlustur("[-] İndirmek istediğiniz öne çıkan hikayenin url'sine ulaşılamadı!", 2))
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Öne çıkan hikayeyi indirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.oneCikanHikayeIndir()

    def dosyaIndir(self,veri):
        try:
            count=1
            for tur in veri:
                for dosya in veri["{tur}".format(tur=tur)]:
                    if tur=="fotograf":
                        isim = str(count) + "_" + str(datetime.datetime.now()).replace(":", "_").replace(" ","") + ".jpg"
                    elif tur=="video":
                        isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".mp4"
                    count += 1
                    urllib.request.urlretrieve(dosya, isim)
                    print(self.uyariOlustur("[+] " + dosya + " indirildi", 1))
        except Exception as error:
            print(self.uyariOlustur(
                '[-] dosya indirme işlemi sırasında bir hata oluştu: {hata}'.format(hata=str(error)), 2))

    def topluTakiptenCik(self):
        try:
            print("[*] Toplu takipten çıkma işlemi başladı.")
            self.driver.get(self.BASE_URL + self.aktifKullanici)
            time.sleep(5)
            takipEdilenSayisi = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
            takipEdilenSayisi = int(self.metindenKarakterSil(takipEdilenSayisi, ','))

            btn_takipEdilenler = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            btn_takipEdilenler.click()
            time.sleep(5)
            takipEdilenIndexNumarasi = 0
            devamEtsinMi = True
            takiptenVazgecilenler = set()
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = takip.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                    takipEdilenKullanıcıAdi = self.metindenKarakterSil(
                        self.metindenKarakterSil(takipEdilenKullanıcıAdi, self.BASE_URL), '/')
                    btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                    if btn_takip.text == "Following":
                        btn_takip.click()
                        time.sleep(2)
                        try:
                            btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                            btn_onay.click()
                            takiptenVazgecilenler.add(takipEdilenKullanıcıAdi)
                        except Exception as error:
                            print(self.uyariOlustur(
                                '[-] {kullaniciAdi} kullanıcısını takipten çıkma işlemi sırasında bir hata oluştu: {hata}'.format(
                                    kullaniciAdi=takipEdilenKullanıcıAdi, hata=str(error)), 2))
                            pass
                        print(self.uyariOlustur(
                            "[*] {index} -) {kullaniciAdi} adlı kullanıcı takip edilmekten vazgeçildi.".format(
                                index=takipEdilenIndexNumarasi + 1, kullaniciAdi=takipEdilenKullanıcıAdi), 1))
                        takipEdilenIndexNumarasi = takipEdilenIndexNumarasi + 1
                        if takipEdilenIndexNumarasi == takipEdilenSayisi:
                            devamEtsinMi = False
                            break
                        time.sleep(10)
                    elif btn_takip.text == "Follow":
                        ## Test amaclı kontrol
                        print("{kullanici} zaten takip ediliyor!".format(kullanici=takipEdilenKullanıcıAdi))
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        print(self.uyariOlustur(
                            '[-] Popup aşağıda kaydırma işlemi sırasında bir hata oluştu: {hata}'.format(
                                hata=str(error)), 2))
                        pass
                    time.sleep(3)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Toplu takipten çıkma işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))


    def takipEdilenleriGetir(self, takipciler, hedefTakipEdilenSayisi=None):
        try:
            print("[*] Takip edilen kullanıcıları seçme işlemi başladı.")
            if hedefTakipEdilenSayisi is None:
                takipEdilenSayisi = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
                takipEdilenSayisi = int(self.metindenKarakterSil(takipEdilenSayisi, ','))
            else:
                kaynakTakipEdilenSayisi = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
                kaynakTakipEdilenSayisi = self.metindenKarakterSil(kaynakTakipEdilenSayisi, ',')
                takipEdilenSayisi = int(self.hedefKaynaktanBuyukMu(hedefTakipEdilenSayisi, kaynakTakipEdilenSayisi))

            btn_takipEdilenler = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            btn_takipEdilenler.click()
            time.sleep(5)

            takipEdilenIndexNumarasi = 0
            islemIndex = 0
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = takip.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                    takipEdilenKullanıcıAdi = self.metindenKarakterSil(
                        self.metindenKarakterSil(takipEdilenKullanıcıAdi, self.BASE_URL), '/')

                    if takipEdilenKullanıcıAdi not in takipciler:
                        btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                        if btn_takip.text == "Following":
                            btn_takip.click()
                            time.sleep(2)
                            try:
                                btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                                btn_onay.click()
                            except Exception as error:
                                print(self.uyariOlustur('[-] {kullaniciAdi} kullanıcısını takipten çıkma işlemi sırasında bir hata oluştu: {hata}'.format(kullaniciAdi=takipEdilenKullanıcıAdi, hata=str(error)), 2))
                                pass
                            print(self.uyariOlustur(
                                "[*] {index} -) {kullaniciAdi} adlı kullanıcı takip edilmekten vazgeçildi.".format(
                                    index=takipEdilenIndexNumarasi + 1, kullaniciAdi=takipEdilenKullanıcıAdi), 1))
                            takipEdilenIndexNumarasi = takipEdilenIndexNumarasi + 1
                            if takipEdilenIndexNumarasi == takipEdilenSayisi:
                                devamEtsinMi = False
                                break
                            time.sleep(5)
                    islemIndex = islemIndex + 1
                    if hedefTakipEdilenSayisi:
                        if islemIndex >= kaynakTakipEdilenSayisi:
                            devamEtsinMi = False
                            break
                    else:
                        if islemIndex >= takipEdilenSayisi:
                            devamEtsinMi = False
                            break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        print(self.uyariOlustur(
                            '[-] Popup aşağıda kaydırma işlemi sırasında bir hata oluştu: {hata}'.format(
                                hata=str(error)), 2))
                        pass
                    time.sleep(3)

        except Exception as error:
            print(self.uyariOlustur(
                '[-] Takip etmeyen kullanıcıları takipten çıkma işlemi sırasında bir hata oluştu: {hata}'.format(
                    hata=str(error)), 2))

    def popupAsagiKaydir(self, secici):
        self.driver.execute_script('''
                                                    var fDialog = document.querySelector('{secici}');
                                                    fDialog.scrollTop = fDialog.scrollHeight
                                                '''.format(secici=secici))

    def takipcileriGetir(self, hedefTakipciSayisi=None):
        try:
            print("[*] Takipçileri listeye ekleme işlemi başladı.")
            self.driver.get(self.BASE_URL + self.aktifKullanici)
            time.sleep(5)

            if hedefTakipciSayisi is None:
                takipciSayisi = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text
                takipciSayisi =int(self.metindenKarakterSil(takipciSayisi, ','))
            else:
                kaynakTakipciSayisi = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text
                kaynakTakipciSayisi = self.metindenKarakterSil(kaynakTakipciSayisi, ',')
                takipciSayisi = int(self.hedefKaynaktanBuyukMu(hedefTakipciSayisi, kaynakTakipciSayisi))

            btn_takipciler = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            btn_takipciler.click()
            time.sleep(5)

            takipciler = set()
            takipciIndexNumarasi = 0
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipcilerPopup = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takipci in takipcilerPopup:
                    takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                    takipciKullaniciAdi=self.metindenKarakterSil(self.metindenKarakterSil(takipciKullaniciAdi,self.BASE_URL),'/')
                    print(self.uyariOlustur("[*] {index} -) {takipci} takipcisi listeye eklendi.".format(index=takipciIndexNumarasi + 1,takipci=takipciKullaniciAdi), 1))
                    takipciler.add(takipciKullaniciAdi)
                    takipciIndexNumarasi = takipciIndexNumarasi + 1
                    if takipciIndexNumarasi == takipciSayisi:
                        devamEtsinMi = False
                        break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        print(self.uyariOlustur(
                            '[-] Popup aşağıda kaydırma işlemi sırasında bir hata oluştu: {hata}'.format(
                                hata=str(error)), 2))
                        pass
                    time.sleep(3)

            btn_close_dialog = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
            btn_close_dialog.click()
            return takipciler
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Takipçileri seçme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

    def takipEtmeyenleriTakiptenCik(self, islemSecildiMi=None, secilenIslem=None):
        try:
            if islemSecildiMi is None:
                print(
                    self.uyariOlustur("Seçilen İşlem >>> Takip edilip, takip etmeyen kullanıcıları takipten çıkma", 1))
                print("")

            if secilenIslem is None:
                print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                print(self.uyariOlustur("Tüm takip edilenler listesi içerisinden işlem yapmak için 1,", 3))
                print(
                    self.uyariOlustur("Belirtilen sayı kadar takip edilenler içerisinden işlem yapmak için 2 giriniz.",
                                      3))
                print("")
                secilenIslem = str(input("Tüm takip edilenler listesi içerisinde mi işlem yapılsın ? >> ").strip())

            if secilenIslem == "1":
                print(self.uyariOlustur(
                    "Seçilen İşlem >>> Tüm takip edilenler listesi içerisinden takip etmeyen kullanıcıları takipten çıkma",
                    1))
                takipciler = self.takipcileriGetir()
                print("[*] Takipçileri listeye ekleme işlemi başladı.")
                self.takipEdilenleriGetir(takipciler=takipciler, hedefTakipEdilenSayisi=None)
                print("[*] Takip etmeyen kullanıcıları takipten çıkma işlemi tamamlandı.")
            elif secilenIslem == "2":
                print(self.uyariOlustur(
                    "Seçilen İşlem >>> Belirtilen sayı kadar takip edilenler listesi içerisinden takip etmeyen kullanıcıları takipten çıkma",
                    1))
                sayi = input("İşlem yapmak için bir sayı giriniz >>> ").strip()
                if sayi.isnumeric():
                    limit = int(sayi)
                    takipciler = self.takipcileriGetir(limit)
                    print("[*] Takipçileri listeye ekleme işlemi başladı.")
                    self.takipEdilenleriGetir(takipciler=takipciler, hedefTakipEdilenSayisi=limit)
                    print("[*] Takip etmeyen kullanıcıları takipten çıkma işlemi tamamlandı.")
                else:
                    print(self.uyariOlustur("[-] Bir sayı girişi yapmadınız.Lütfen bir sayı giriniz!", 2))
                    print("")
                    self.takipEtmeyenleriTakiptenCik(islemSecildiMi=True, secilenIslem=secilenIslem)
            else:
                print(self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!", 2))
                print("")
                self.takipEtmeyenleriTakiptenCik(islemSecildiMi=islemSecildiMi, secilenIslem=None)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Takip etmeyen kullanıcıları takipten çıkma işlemi sırasında bir hata oluştu: {hata}".format(
                    hata=str(error)), 2))

    def paylasimTipiKontrol(self):
        try:
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img")
            return True
        except:
            return False

    def metindenKarakterSil(self, metin, silinecekKarakterler):
        return metin.replace(silinecekKarakterler, '')
        # return ''.join(karakter for karakter in metin if karakter not in silinecekKarakterler)

    def paylasimBegenenleriTakipEt(self, islemSecildiMi=None, secilenIslem=None):
        url = input("İşlem yapmak istediğiniz gönderi url >> ").strip()

        if not url:
            self.paylasimBegenenleriTakipEt()
        elif url == "menu":
            self.menu()

        if self.urlKontrol(url):
            self.driver.get(url)
            time.sleep(5)

            hedefBegenenSayisi = None
            if islemSecildiMi is None:
                print(self.uyariOlustur("Seçilen İşlem >>> Bir paylaşımı beğenen kullanıcıları takip etme", 1))
                print("")

            if secilenIslem is None:
                print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                print(self.uyariOlustur("Tüm takipçiler listesi içerisinden işlem yapmak için 1,", 3))
                print(self.uyariOlustur(
                    "Belirtilen sayı kadar takipçiler listesi içerisinden işlem yapmak için 2 giriniz,", 3))
                print("")
                secilenIslem = str(input("Tüm takipçiler listesi içerisinde mi işlem yapılsın ? >> ").strip())

            if secilenIslem == "1":
                print(
                    self.uyariOlustur("Seçilen İşlem >>> Paylaşımı beğenen tüm kullanıcıları takip etme", 1))
            elif secilenIslem == "2":
                print(self.uyariOlustur(
                    "Seçilen İşlem >>> Belirtilen sayı kadar paylaşımı beğenen tüm kullanıcıları takip etme", 1))
                hedefBegenenSayisi = input("İşlem yapmak için bir sayı giriniz >>> ").strip()
                if hedefBegenenSayisi.isnumeric():
                    hedefBegenenSayisi = int(hedefBegenenSayisi)
                else:
                    print(self.uyariOlustur("[-] Bir sayı girişi yapmadınız.Lütfen bir sayı giriniz!", 2))
                    print("")
                    self.paylasimBegenenleriTakipEt(islemSecildiMi=True, secilenIslem=secilenIslem)
            else:
                print(self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!", 2))
                print("")
                self.paylasimBegenenleriTakipEt(islemSecildiMi=None, secilenIslem=None)

            if not self.hesapGizliMi():
                try:
                    print("[*] '" + url + "'  paylaşımını beğenen kullanıcıları takip etme işlemi başladı...")
                    if self.paylasimTipiKontrol():
                        takipIstekSayisi = 0
                        islemIndex = 0
                        devamEtsinMi = True
                        if hedefBegenenSayisi is None:
                            begenenSayisi = self.driver.find_element_by_css_selector(
                                "div.Nm9Fw > button.sqdOP > span").text
                            begenenSayisi = int(self.metindenKarakterSil(begenenSayisi, ','))
                        else:
                            kaynakBegenenSayisi = self.driver.find_element_by_css_selector(
                                "div.Nm9Fw > button.sqdOP > span").text
                            kaynakBegenenSayisi = int(self.metindenKarakterSil(kaynakBegenenSayisi, ','))
                            begenenSayisi = int(self.hedefKaynaktanBuyukMu(hedefBegenenSayisi, kaynakBegenenSayisi))

                        btn_begenenler = self.driver.find_element_by_css_selector("div.Nm9Fw > button.sqdOP")
                        btn_begenenler.click()
                        time.sleep(5)

                        while devamEtsinMi:
                            dialog_popup = self.driver.find_element_by_css_selector("div.pbNvD")
                            begenenlerKullanicilar = dialog_popup.find_elements_by_css_selector('div.HVWg4')
                            for begenenKullanici in begenenlerKullanicilar:
                                begenenKullaniciAdi = begenenKullanici.find_element_by_css_selector(
                                    "div.Igw0E > div.Igw0E > div._7UhW9  a").get_attribute('href')
                                begenenKullaniciAdi = begenenKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                                btn_takip = begenenKullanici.find_element_by_css_selector("div.Igw0E > button.sqdOP")
                                if btn_takip.text == "Follow":
                                    print(self.uyariOlustur(
                                        "[*] {index} -) {kullaniciAdi} kullanıcısı takip edilme işlemi başladı.".format(
                                            index=takipIstekSayisi + 1, kullaniciAdi=begenenKullaniciAdi), 1))
                                    btn_takip.click()
                                    takipIstekSayisi = takipIstekSayisi + 1
                                    if takipIstekSayisi == begenenSayisi:
                                        devamEtsinMi = False
                                        break
                                    time.sleep(5)

                                islemIndex = islemIndex + 1
                                if hedefBegenenSayisi:
                                    if islemIndex >= kaynakBegenenSayisi:
                                        devamEtsinMi = False
                                        break
                                else:
                                    if islemIndex >= begenenSayisi:
                                        devamEtsinMi = False
                                        break
                            if devamEtsinMi:
                                self.popupAsagiKaydir(secici='div[role="dialog"]  .i0EQd > div:nth-child(1)')

                                time.sleep(3)
                            else:
                                print("[*] Takipçi seçme işlemi tamamlandı.")
                                self.paylasimBegenenleriTakipEt()
                    else:
                        print(
                            '[*] {url} paylaşımını  beğenen kullanıcıların listesi görüntülenemediğinden dolayı takip etme işlemi yapılamıyor'.format(
                                url=url))
                except Exception as error:
                    print(self.uyariOlustur(
                        '[-] {url} paylaşımını beğenen kullanıcıların listesini getirme işlemi sırasında hata oluştu: {hata}'.format(
                            url=url, hata=str(error)), 2))
                    self.paylasimBegenenleriTakipEt()
            else:
                print(self.uyariOlustur(
                    "[-] " + url + " paylaşımının sahibinin profili gizli hesap olduğundan dolayı, bu paylaşımı beğenen kullanıcıların listesi alınamıyor!",
                    2))
                self.paylasimBegenenleriTakipEt()
        else:
            self.paylasimBegenenleriTakipEt()

    def kullaniciListesiSec(self, secim):
        print(self.uyariOlustur("Seçilen İşlem >>> Txt dosyasından olarak oluşturduğunuz kullanicilar listesi ile işlem yapma", 1))
        dosya = self.dosyaSec(secim)
        kullanicilar=self.dosyaİceriginiAl(dosya)
        if self.dosyaİcerigiAlindiMi(kullanicilar):
            self.kullanicilariTakipEt(kullanicilar, 14)
        else:
            self.kullaniciListesiSec(secim)

    def kullanicilariTakipEt(self, kullaniciListesi, secim):
        for kullanici in kullaniciListesi:
            self.kullaniciTakipEt(kullanici.strip(), secim)
            time.sleep(30)
            print(kullanici)

    def dosyaSec(self, secim):
        try:
            dosyaAdi = input("Dosya yolunu giriniz >> ").strip()
            if self.dosyaMi(dosyaAdi) and self.txtDosyasiMi(dosyaAdi):
                return str(dosyaAdi)
            else:
                print(self.uyariOlustur("[-] Lütfen geçerli  bir dosya yolu belirtin!", 2))
                self.dosyaSec(secim)
        except Exception as error:
            print(self.uyariOlustur("[-] Dosya seçme işlemi sırasında bir hata oluştu:" + str(error), 2))
            self.dosyaSec(secim)

    def dosyaMi(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False

    def txtDosyasiMi(self,dosya):
        if os.path.splitext(dosya)[-1].lower()==".txt":
            return True
        else:
            return False


    def secilenIslem(self, secim):
        print("")
        if secim == 1:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kulllanıcının tüm paylaşımlarını indirme", 1))
        elif secim == 2:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kulllanıcının tüm paylaşımlarını beğenme", 1))
        elif secim == 3:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kulllanıcının tüm paylaşımlarını beğenmekten vazgeçme", 1))
        elif secim == 4:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir fotoğrafı indirme", 1))
        elif secim == 5:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir videoyu indirme", 1))
        elif secim == 6:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir paylaşımı beğenme", 1))
        elif secim == 7:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir paylaşımı beğenmekten vazgeçme", 1))
        elif secim == 8:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kullanıcıyı takip etme", 1))
        elif secim == 9:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kullanıcıyı takip etmekten vazgeçme", 1))
        elif secim == 10:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kullanıcıyı engelleme", 1))
        elif secim == 11:
            print(self.uyariOlustur(" Seçilen İşlem >>> Bir kullanıcının engelini kaldırma", 1))
        elif secim == 12:
            print(self.uyariOlustur(" Seçilen İşlem >>> İnstagram oturumunu kapatma", 1))
        elif secim == 13:
            print(self.uyariOlustur(" Seçilen İşlem >>> Python uygulamasından çıkış yapma", 1))
        if secim < 12:
            print(self.uyariOlustur(" [*] Ana menüye dönmek için  'menu' komutunu giriniz", 3))
        print("")

    def threadOlustur(self):
        t1 = threading.Thread(target=self.tarayiciBaslat)
        t1.daemon = True
        t1.start()

    def tarayiciBaslat(self):
        print(self.uyariOlustur("[*] Tarayıcı Başlatılıyor...", 1))
        self.driver = webdriver.Firefox(firefox_profile=self.dilDegistir(),
                                        executable_path="E:\\Python\\Uygulamalar\\Intagram-Bot\\Instagram-Bot\\geckodriver.exe")
        self.driver.get(self.BASE_URL + 'accounts/login/')

    def dilDegistir(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        return profile

    def girisYap(self, username=False, password=False):
        try:
            if not username and not password:
                print(" ")
                print(" ")
                print(self.uyariOlustur("<<< Instagram Giriş Yap >>>>", 1))
                username = input('Kullanıcı adınız >> ')
                password = getpass.getpass(prompt='Parolanız >> ')
            elif not username:
                username = input('Kullanıcı adınız >> ')
            elif not password:
                password = getpass.getpass(prompt='Parolanız >> ')

            if not username and not password:
                print(self.uyariOlustur("[-] Lütfen kullanıcı adınızı ve parolanızı giriniz!", 2))
                self.girisYap()
            elif not username:
                print(self.uyariOlustur("[-] Lütfen kullanıcı adınızı giriniz!", 2))
                self.girisYap(False, password)
            elif not password:
                print(self.uyariOlustur("[-] Lütfen parolanızı giriniz!", 2))
                self.girisYap(username, False)

            print(self.uyariOlustur("[*] Kullanıcı girişi yapılıyor...", 1))
            time.sleep(15)
            usernameInput = self.driver.find_elements_by_css_selector('form input')[0]
            passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
            usernameInput.send_keys(username.strip())
            passwordInput.send_keys(password.strip())
            passwordInput.send_keys(Keys.ENTER)
            time.sleep(5)
            print(self.girisKontrol())
            if self.girisYapildimi:
                self.aktifKullanici = username
                self.menu()
            else:
                self.inputTemizle(usernameInput)
                self.inputTemizle(passwordInput)
                self.girisYap()
        except Exception as e:
            print(self.uyariOlustur("[-] Kullanıcı girişi sırasında hata:" + str(e), 2))

    def girisKontrol(self):
        if "The username you entered doesn't belong to an account. Please check your username and try again." in self.driver.page_source:
            uyari = self.uyariOlustur(
                "[-] Girdiğiniz kullanıcı adı bir hesaba ait değil. Lütfen kullanıcı adınızı kontrol edin ve tekrar deneyin.",
                2)
        elif "Sorry, your password was incorrect. Please double-check your password." in self.driver.page_source:
            uyari = self.uyariOlustur("[-] Üzgünüz, parolanız hatalıydı. Lütfen parolanızı tekrar kontrol edin.", 2)
        elif self.BASE_URL + "accounts/login/two_factor" in self.driver.current_url:
            uyari = self.girisDogrulama()
        elif self.driver.current_url != self.BASE_URL + "accounts/login/":
            uyari = self.uyariOlustur("[+] Giriş işlemi başarılı", 1)
            self.girisYapildimi = True
        else:
            uyari = self.uyariOlustur("[-] Giriş işlemi başarısız", 2)
        return uyari

    def girisDogrulama(self, durum=True):
        kod = input("Telefonunuza gönderilen kodu giriniz >> ").strip()
        if not kod:
            self.girisYap(durum)

        if durum:
            time.sleep(5)
        kodInput = self.driver.find_elements_by_css_selector('form input')[0]
        kodInput.send_keys(kod)
        kodInput.send_keys(Keys.ENTER)
        time.sleep(5)
        if "A security code is required." in self.driver.page_source:
            print(self.uyariOlustur("[-] Lütfen güvenlik kodunu giriniz!", 2))
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif "Please check the security code and try again." in self.driver.page_source:
            print(self.uyariOlustur("[-] Lütfen güvenlik kodunu kontrol edin ve tekrar deneyin.", 2))
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif self.BASE_URL + "accounts/login/two_factor" not in self.driver.current_url:
            self.girisYapildimi = True
            return self.uyariOlustur("[+] Giriş işlemi başarılı", 1)
        else:
            return self.uyariOlustur("[-] Giriş Yapılamıyor...", 2)

    def inputTemizle(self, inpt):
        inpt.clear()

    def profilSec(self, secim):
        kullanici = input(" İşlem yapmak istediğiniz profilin kullanıcı adı >> ")

        if kullanici == "menu":
            self.menu()

        if not kullanici:
            self.profilSec(secim)

        if self.kullaniciKontrol(kullanici):
            print("[*] Tarayıcı '" + kullanici + "' profiline yönlendiriliyor...")
            if secim == 1:
                self.paylasimlariIndir(kullanici, secim)
            elif secim == 2:
                self.paylasimlariBegen(kullanici, secim)
            elif secim == 3:
                self.paylasimlariBegen(kullanici, secim, False)
            elif secim == 8:
                self.kullaniciTakipEt(kullanici, secim)
            elif secim == 9:
                self.kullaniciTakipVazgec(kullanici, secim)
            elif secim == 10:
                self.kullaniciEngelle(kullanici, secim)
            elif secim == 11:
                self.kullaniciEngelKaldir(kullanici, secim)
            elif secim == 15:
                self.kullaniciTakipcileriniTakipEt(kullanici, secim)
        else:
            print(self.uyariOlustur("[-] '" + kullanici + "' adında bir kullanıcı bulunamadı ", 2))
            self.profilSec(secim)

    def hedefKaynaktanBuyukMu(self, hedef, kaynak):
        if hedef > kaynak:
            hedef = kaynak
        return hedef

    def kullaniciTakipcileriniTakipEt(self, kullaniciAdi, secim, islemSecildiMi=None, secilenIslem=None):
        try:
            self.driver.get(self.BASE_URL + kullaniciAdi)
            time.sleep(4)
            hedefTakipciSayisi = None
            if islemSecildiMi is None:
                print(
                    self.uyariOlustur("Seçilen İşlem >>> Bir kullanıcının takipçilerini takip etme", 1))
                print("")

            if secilenIslem is None:
                print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                print(self.uyariOlustur("Tüm takipçiler listesi içerisinden işlem yapmak için 1,", 3))
                print(self.uyariOlustur(
                    "Belirtilen sayı kadar takipçiler listesi içerisinden işlem yapmak için 2 giriniz,", 3))
                print("")
                secilenIslem = str(input("Tüm takipçiler listesi içerisinde mi işlem yapılsın ? >> ").strip())

            if secilenIslem == "1":
                print(
                    self.uyariOlustur("Seçilen İşlem >>> Tüm takipçiler listesi içerisindeki kullanıcıları takip etme",
                                      1))
            elif secilenIslem == "2":
                print(self.uyariOlustur(
                    "Seçilen İşlem >>> Belirtilen sayı kadar takipçiler listesi içerisindeki kullanıcıları takip etme",
                    1))
                hedefTakipciSayisi = input("İşlem yapmak için bir sayı giriniz >>> ").strip()
                if hedefTakipciSayisi.isnumeric():
                    hedefTakipciSayisi = int(hedefTakipciSayisi)
                else:
                    print(self.uyariOlustur("[-] Bir sayı girişi yapmadınız.Lütfen bir sayı giriniz!", 2))
                    print("")
                    self.kullaniciTakipcileriniTakipEt(kullaniciAdi, secim, islemSecildiMi=True,
                                                       secilenIslem=secilenIslem)
            else:
                print(self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!", 2))
                print("")
                self.kullaniciTakipcileriniTakipEt(kullaniciAdi, secim, islemSecildiMi=None, secilenIslem=None)

            print("[*] '" + kullaniciAdi + "' kullanıcısının takipçilerini takip etme işlemi başladı...")

            if not self.sayfaMevcutMu():
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if not self.hesapGizliMi():
                takipIstekSayisi = 0;
                devamEtsinMi = True
                islemIndex = 0

                if hedefTakipciSayisi is None:
                    takipciSayisi = self.driver.find_element_by_css_selector("a.-nal3 > span.g47SY").get_attribute(
                        'title')
                    takipciSayisi = int(self.metindenKarakterSil(takipciSayisi, ','))
                else:
                    kaynakTakipciSayisi = self.driver.find_element_by_css_selector(
                        "a.-nal3 > span.g47SY").get_attribute('title')
                    kaynakTakipciSayisi = int(self.metindenKarakterSil(kaynakTakipciSayisi, ','))
                    takipciSayisi = self.hedefKaynaktanBuyukMu(hedefTakipciSayisi, kaynakTakipciSayisi)

                btn_takipciler = self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
                btn_takipciler.click()
                time.sleep(5)

                while devamEtsinMi:
                    dialog_popup = self.driver.find_element_by_css_selector('div._1XyCr')
                    takipciListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                    for takipci in takipciListe:
                        takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                        takipciKullaniciAdi = takipciKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                        try:
                            btn_takip = takipci.find_element_by_css_selector('button.sqdOP')
                            if btn_takip.text == "Follow":
                                print(self.uyariOlustur("[*] {index} -) {takipci} takip edilme işlemi başladı.".format(
                                    index=takipIstekSayisi + 1, takipci=takipciKullaniciAdi), 1))
                                btn_takip.click()
                                takipIstekSayisi = takipIstekSayisi + 1
                                if takipIstekSayisi == takipciSayisi:
                                    devamEtsinMi = False
                                    break
                                time.sleep(5)
                        except Exception:
                            pass

                        islemIndex = islemIndex + 1
                        if hedefTakipciSayisi:
                            if islemIndex >= kaynakTakipciSayisi:
                                devamEtsinMi = False
                        else:
                            if islemIndex >= takipciSayisi:
                                devamEtsinMi = False

                    if devamEtsinMi:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                        time.sleep(3)
                print("[*] '" + kullaniciAdi + "' kullanıcısının takipçilerini takip etme işlemi tamamlandı.")
            else:
                print(self.uyariOlustur(
                    "[-] " + kullaniciAdi + " adlı kişinin hesabı gizli hesap olduğundan takipçileri takip edilemiyor!",
                    2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariOlustur(
                "[-] " + kullaniciAdi + " kullanıcısının takipçilerini takip etme işlemi sırasında hata:" + str(e), 2))
            self.profilSec(secim)

    def kullaniciKontrol(self, kullaniciadi):
        response = requests.get(self.BASE_URL + kullaniciadi)
        if response.status_code == 404:
            return False
        else:
            return True

    def kullaniciTakipEt(self, kullaniciAdi, secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısını takip etme işlemine başladı...")
        try:
            self.driver.get(self.BASE_URL + kullaniciAdi)
            time.sleep(5)

            if not self.sayfaMevcutMu():
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                if secim != 14:
                    self.profilSec(secim)

            if self.hesapGizliMi():
                btn_takip = self.driver.find_element_by_css_selector("button.BY3EC")
            else:
                btn_takip = self.driver.find_element_by_css_selector('button._5f5mN')
            if (btn_takip.text == 'Follow'):
                btn_takip.click()
                if self.hesapGizliMi():
                    print(self.uyariOlustur("[+] " + kullaniciAdi + " kullanıcısına takip isteği gönderildi", 1))
                else:
                    print(self.uyariOlustur("[+] " + kullaniciAdi + " kullanıcısı takip edilmeye başlandı", 1))

                if secim != 14:
                    self.profilSec(secim)
            elif btn_takip.text == "Requested":
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısına takip isteği zaten gönderildi", 2))
                if secim != 14:
                    self.profilSec(secim)
            else:
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısını zaten takip ediyorsun", 2))
                if secim != 14:
                    self.profilSec(secim)
        except Exception as e:
            print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısını takip etme işlemi sırasında hata:" + str(e),
                                    2))
            if secim != 14:
                self.profilSec(secim)

    def kullaniciTakipVazgec(self, kullaniciAdi, secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısı takip etmekten vazgeçiliyor...")
        try:
            self.driver.get(self.BASE_URL + kullaniciAdi)
            time.sleep(5)

            if not self.sayfaMevcutMu():
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if self.hesapGizliMi():
                btn_takip = self.driver.find_element_by_css_selector("button.BY3EC")
            else:
                btn_takip = self.driver.find_element_by_css_selector('button._5f5mN')

            if btn_takip.text == "Following":
                btn_takip.click()
                time.sleep(5)
                btn_popup = self.driver.find_element_by_css_selector('button.aOOlW')
                btn_popup.click()
                print(self.uyariOlustur("[+] " + kullaniciAdi + " kullanıcısı takip edilmekten vazgeçildi", 1))
                self.profilSec(secim)
            else:
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısını zaten takip etmiyorsun", 2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariOlustur(
                "[-] " + kullaniciAdi + " kullanıcısını takip etmekten vazgeçme işlemi sırasında hata:" + str(e), 2))
            self.profilSec(secim)

    def kullaniciEngelle(self, kullaniciAdi, secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısı engelleniyor...")
        try:
            self.driver.get(self.BASE_URL + kullaniciAdi)
            time.sleep(3)

            if not self.sayfaMevcutMu():
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if self.hesapGizliMi():
                btn = self.driver.find_element_by_css_selector('button.BY3EC')
            else:
                btn = self.driver.find_element_by_css_selector('button._5f5mN')

            if btn.text != "Unblock":
                self.driver.find_element_by_css_selector(
                    "span.glyphsSpriteMore_horizontal__outline__24__grey_9").click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[1].click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[0].click()
                print(self.uyariOlustur("[+] '" + kullaniciAdi + "' kullanıcısı engellendi", 1))
                self.profilSec(secim)
            else:
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısı zaten engellenmiş durumda", 2))
                self.profilSec(secim)

        except Exception as e:
            print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısını engelleme işlemi sırasında hata:" + str(e),
                                    2))
            self.profilSec(secim)

    def kullaniciEngelKaldir(self, kullaniciAdi, secim):
        print("[*] '" + kullaniciAdi + "' kullanıcısının engeli kaldırılıyor...")
        try:
            self.driver.get(self.BASE_URL + kullaniciAdi)
            time.sleep(3)

            if not self.sayfaMevcutMu():
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısına ulaşılamadı", 2))
                self.profilSec(secim)

            if self.hesapGizliMi():
                btn = self.driver.find_element_by_css_selector('button.BY3EC')
            else:
                btn = self.driver.find_element_by_css_selector('button._5f5mN')

            if btn.text == "Unblock":
                self.driver.find_element_by_css_selector(
                    "span.glyphsSpriteMore_horizontal__outline__24__grey_9").click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[1].click()
                time.sleep(2)
                self.driver.find_elements_by_css_selector("div.mt3GC > button")[0].click()
                print(self.uyariOlustur("[+] '" + kullaniciAdi + "' kullanıcısının engeli kaldırıldı.", 1))
                self.profilSec(secim)
            else:
                print(self.uyariOlustur("[-] " + kullaniciAdi + " kullanıcısı zaten engellenmemiş durumda", 2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariOlustur(
                "[-] " + kullaniciAdi + " kullanıcısının engelini kaldırma işlemi sırasında hata:" + str(e), 2))
            self.profilSec(secim)

    def paylasimlariIndir(self, kullaniciadi, secim):
        self.driver.get(self.BASE_URL + kullaniciadi)
        time.sleep(10)
        try:
            if not self.hesapGizliMi():
                print("[*] Paylaşım tarama işlemi başladı....")
                video_urls, carousel_url = self.paylasimTara(kullaniciadi)
                print("[*] Video indirme işlemine geçiliyor...")
                print("[*] İndirilecek Tekli Video Sayısı:" + str(len(video_urls)))
                self.veriIndir(video_urls, "video")
                if len(video_urls) > 0:
                    print(self.uyariOlustur("[+] Video indirme işlemi tamamlandı", 1))

                print("[*] Carousel Video ve Resim paylaşımlarının tarama işlemi geçiliyor...")
                print("[*] Carouse Paylaşımlarının tarama işlemi başladı...")
                print("[*] İndirilecek Toplam Carousel Paylaşım Sayısı:" + str(len(carousel_url)))
                self.veriIndir(carousel_url, "carousel")
                if len(carousel_url) > 0:
                    print(self.uyariOlustur("[+] Carousel Video ve Resim paylaşımlarının indirme işlemi tamamlandı...",
                                            1))

                print(self.uyariOlustur("[+] " + kullaniciadi + " adlı kullanıcının tüm paylaşımları indirildi", 1))
                self.klasorDegistir("../")
                self.profilSec(secim)
            else:
                print(self.uyariOlustur(
                    "[-] " + kullaniciadi + " adlı kişinin hesabı gizli hesap olduğundan Paylaşımları indirme işlemi yapılamıyor!",
                    2))
                self.profilSec(secim)
        except Exception as e:
            print(self.uyariOlustur(
                "[-] '" + kullaniciadi + "' kullanısının paylaşımlarını indirme işlemi sırasında bir hata oluştu:" + str(
                    e), 2))
            self.profilSec(secim)

    def paylasimTara(self, kullaniciadi):
        img_src = set()
        carousel_url = set()
        video_urls = set()
        try:
            gonderiSayisi = self.driver.find_element_by_css_selector("span.g47SY").text
            if int(gonderiSayisi) < 10:
                gonderiSayisi = 10
            for i in range(round(int(gonderiSayisi) / 10)):
                try:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    article = self.driver.find_element_by_css_selector('article.FyNDV')
                    hrefs = article.find_elements_by_tag_name("a")
                    for href in hrefs:
                        durum = True
                        divs = href.find_elements_by_tag_name("div")
                        for div in divs:
                            if "u7YqG" in div.get_attribute("class"):
                                span = div.find_element_by_tag_name("span")
                                href = href.get_attribute("href")
                                if "mediatypesSpriteVideo__filled__32" in span.get_attribute("class"):
                                    if href not in video_urls:
                                        print(self.uyariOlustur("[*] Video url:" + href, 1))
                                    video_urls.add(href)

                                    durum = False
                                elif "mediatypesSpriteCarousel__filled__32" in span.get_attribute("class"):
                                    if href not in carousel_url:
                                        print(self.uyariOlustur("[*] Carousel paylaşim url:" + href, 1))
                                    carousel_url.add(href)

                                    durum = False
                        if durum:
                            src = href.find_element_by_tag_name("img").get_attribute("src")
                            if src not in img_src:
                                print(self.uyariOlustur("[*] Resim url:" + src, 1))
                            img_src.add(src)
                    time.sleep(10)
                except Exception as e:
                    print(self.uyariOlustur(
                        "[-] '" + kullaniciadi + "' kullanıcısının paylaşımlarını tarama işlemi sırasında hata oluştu:" + str(
                            e), 2))
                    continue
        except Exception as e:
            print(self.uyariOlustur(
                "[-] '" + kullaniciadi + "' kullanıcısının paylaşımlarını tarama işlemi sırasında hata oluştu:" + str(
                    e), 2))
            pass

        print("[*] İndirilecek Tekli Fotoğraf Sayısı:" + str(len(img_src)))
        self.klasorOlustur(kullaniciadi)
        print("[*] Fotoğraf indirme işlemi başladı")
        self.veriIndir(img_src, "resim")
        print("[*] Fotoğraf indirme işlemi tamamlandı")
        return video_urls, carousel_url

    def carouselTara(self, url):
        self.driver.get(url)
        time.sleep(10)
        try:
            ul = self.driver.find_element_by_css_selector("ul.YlNGR")
            li = ul.find_elements_by_css_selector("li._-1_m6")
            carousel_len = len(ul.find_elements_by_css_selector("li._-1_m6"))
            carousel = []
            print("[*] " + url + " Adresi url'leri taranıyor.")
            for i in range(carousel_len):
                satir = {}
                if self.resimMi(li[i]):
                    src = li[i].find_element_by_css_selector("img.FFVAD").get_attribute("src")
                    satir['src'] = src
                    satir['tip'] = 'fotograf'
                    print(self.uyariOlustur("[*] Img src:" + src, 1))
                    time.sleep(3)
                    if i < carousel_len - 1:
                        self.driver.find_element_by_css_selector("button._6CZji").click()
                else:
                    src = li[i].find_element_by_css_selector("video.tWeCl").get_attribute("src")
                    satir['src'] = src
                    satir['tip'] = 'video'
                    print(self.uyariOlustur("[*] Video url:" + src, 1))
                    print("Tip:" + satir['tip'])
                    time.sleep(3)
                    if i < carousel_len - 1:
                        self.driver.find_element_by_css_selector("button._6CZji").click()
                carousel.append(satir)
            print("[*] Carousel tarama işlemi tamamlandı")
            return carousel
        except Exception as e:
            print(self.uyariOlustur("[-] Carousel tarama işlemi sırasında hata oluştu:" + str(e), 2))
            pass

    def resimMi(self, li):
        try:
            li.find_element_by_css_selector("img.FFVAD")
            return True
        except:
            return False

    def veriIndir(self, veri, durum):
        try:
            count = 1
            if durum == "resim":
                for img in veri:
                    try:
                        isim = str(count) + "_" + str(datetime.datetime.now()).replace(":", "_").replace(" ",
                                                                                                         "") + ".jpg"
                        count += 1
                        urllib.request.urlretrieve(img, isim)
                        print(self.uyariOlustur("[+] " + img + " indirildi", 1))
                    except Exception as e:
                        print(str(e))
                        continue
            elif durum == "video":
                for url in veri:
                    self.driver.get(url)
                    print("[*] Indirilecek video url:" + url)
                    time.sleep(5)
                    video = self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                    isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".mp4"
                    count += 1
                    urllib.request.urlretrieve(video, isim)
                    print(self.uyariOlustur("[+] " + video + " indirildi", 1))
            elif durum == "carousel":
                klasor_count = 1
                for url in veri:
                    urls = self.carouselTara(url)
                    klasor_adi = str(klasor_count) + "_carousel"
                    self.klasorOlustur(klasor_adi)
                    for link in urls:
                        if link['tip'] == "fotograf":
                            isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".jpg"
                        elif link['tip'] == "video":
                            isim = str(count) + str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".mp4"
                        count += 1
                        urllib.request.urlretrieve(link['src'], isim)
                        print(self.uyariOlustur("[+] " + link['src'] + " indirildi", 1))
                    self.klasorDegistir("../")
                    klasor_count += 1
        except Exception as e:
            print(self.uyariOlustur("[-] Veri indirme işlemi sırasında hata oluştu:" + str(e), 2))

    def paylasimlariBegen(self, kullaniciadi, secim, durum=True):
        self.driver.get(self.BASE_URL + kullaniciadi)
        time.sleep(10)
        if not self.hesapGizliMi():
            print("[*] '" + kullaniciadi + "' kullanıcısının paylaşımlarının tarama işlemi başladı...")
            gonderiSayisi = self.driver.find_element_by_css_selector(
                "ul.k9GMp > li.Y8-fY > span.-nal3 > span.g47SY").text
            if int(gonderiSayisi) < 10:
                gonderiSayisi = 10
            pics_href = set()
            for i in range(round(int(gonderiSayisi) / 10)):
                try:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    hrefs = self.driver.find_element_by_css_selector('article.FyNDV').find_elements_by_tag_name("a")
                    for href in hrefs:
                        href = href.get_attribute("href")
                        if href not in pics_href:
                            print(self.uyariOlustur("[+] Url:" + href, 1))
                        pics_href.add(href)

                    time.sleep(5)
                except Exception as e:
                    print(self.uyariOlustur(
                        "[-] '" + kullaniciadi + "' kullanıcısının paylaşımlarını tarama işlemi sırasında bir hata oluştu:" + str(
                            e), 2))
                    continue

            print(self.uyariOlustur("[+] '" + kullaniciadi + "' kullanıcısının paylaşımlarının tarama işlemi bitti...",
                                    1))
            print("[*] Toplam paylaşım sayısı:" + str(len(pics_href)))
            if durum:
                print("[*] Paylaşım beğenme işlemi başladı...")
            else:
                print("[*] Paylaşım beğenmekten vazgeçme işlemi başladı...")
            for pic in pics_href:
                if durum:
                    print("[*] " + pic + " paylaşımı beğeniliyor...")
                else:
                    print("[*] " + pic + " paylaşımı beğenmekten vazgeçiliyor...")
                try:
                    self.driver.get(pic)
                    time.sleep(5)
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    btn_begen_class = self.driver.find_element_by_css_selector(
                        "span.fr66n > button > span").get_attribute("class")
                    if durum:
                        if "glyphsSpriteHeart__outline__24__grey_9" in btn_begen_class:
                            begen = self.driver.find_element_by_css_selector(
                                "span.glyphsSpriteHeart__outline__24__grey_9")
                            begen.click()
                            print(self.uyariOlustur("[+] " + pic + " paylaşımı beğenildi", 1))
                            time.sleep(10)
                        else:
                            print(self.uyariOlustur("[-] Bu gönderi daha önce beğenildi.", 1))
                    else:
                        if "glyphsSpriteHeart__filled__24__red_5" in btn_begen_class:
                            btn_begen = self.driver.find_element_by_css_selector(
                                "span.glyphsSpriteHeart__filled__24__red_5")
                            btn_begen.click()
                            print(self.uyariOlustur("[+] " + pic + " paylaşımı beğenilmekten vazgeçildi.", 1))
                            time.sleep(10)
                        else:
                            print(self.uyariOlustur("[-] Bu gönderi zaten beğenilmedi.", 1))
                except Exception as e:
                    print(self.uyariOlustur(
                        "[-] '" + kullaniciadi + "' kullanıcısının paylaşımlarını beğenme işlemi sırasında bir hata oluştu:" + str(
                            e), 2))
                    continue

            print(
                self.uyariOlustur("[+] '" + kullaniciadi + "' kullanıcısının paylaşımlarını beğenme işlemi tamamlandı",
                                  1))
            self.profilSec(secim)
        else:
            print(self.uyariOlustur(
                "[-] " + kullaniciadi + " adlı kişinin hesabı gizli hesap olduğundan beğeni işlemi yapılamıyor!", 2))
            self.profilSec(secim)

    def paylasimBegen(self, durum=True):
        if durum:
            url = input("Beğenmek istediğiniz paylaşım url >> ").strip()
        else:
            url = input("Beğenmekten vazgeçmek istediğiniz paylaşım url >> ").strip()

        if not url:
            self.paylasimBegen(durum)
        elif url == "menu":
            self.menu()

        if self.urlKontrol(url):
            self.driver.get(url)
            if durum:
                print("[*] '" + url + "' adresindeki paylaşımın beğenme işlemi başladı...")
            else:
                print("[*] '" + url + "' adresindeki paylaşımın beğenmekten vazgeçme işlemi başladı...")
            time.sleep(10)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            if not self.hesapGizliMi():
                try:
                    btn_begen_class = self.driver.find_element_by_css_selector(
                        "span.fr66n > button > span").get_attribute("class")
                    if durum:
                        if "glyphsSpriteHeart__outline__24__grey_9" in btn_begen_class:
                            begen = self.driver.find_element_by_css_selector(
                                "span.glyphsSpriteHeart__outline__24__grey_9")
                            begen.click()
                            print(self.uyariOlustur("[+] " + url + " paylaşımı beğenildi", 1))
                            self.paylasimBegen(durum)
                        else:
                            print(self.uyariOlustur("[-] Bu gönderi daha önce beğenildi.", 2))
                            self.paylasimBegen(durum)
                    else:
                        if "glyphsSpriteHeart__filled__24__red_5" in btn_begen_class:
                            btn_begen = self.driver.find_element_by_css_selector(
                                "span.glyphsSpriteHeart__filled__24__red_5")
                            btn_begen.click()
                            print(self.uyariOlustur("[+] " + url + " paylaşımı beğenilmekten vazgeçildi.", 1))
                            self.paylasimBegen(durum)
                        else:
                            print(self.uyariOlustur("[-] Bu gönderi zaten beğenilmedi.", 2))
                            self.paylasimBegen(durum)
                except Exception as e:
                    if durum:
                        print(self.uyariOlustur("[-] Paylaşım beğenme işlemi sırasında hata:" + str(e), 2))
                        self.paylasimBegen(durum)
                    else:
                        print(self.uyariOlustur("[-] Paylaşım beğenmekten vazgeçme işlemi sırasında hata:" + str(e), 2))
                        self.paylasimBegen(durum)
            else:
                print(self.uyariOlustur(
                    "[-] " + url + " paylaşımının sahibinin profili gizli hesap olduğundan beğeni işlemi yapılamıyor!",
                    2))
                self.paylasimBegen(durum)
        else:
            self.paylasimBegen(durum)

    def fotografIndir(self):
        url = input("İndirmek istediğiniz fotoğraf url >> ").strip()

        if not url:
            self.fotografIndir()
        elif url == "menu":
            self.menu()

        if self.urlKontrol(url):
            try:
                self.driver.get(url)
                print("[*] '" + url + "' adresindeki fotoğrafın indirme işlemi başladı...")
                time.sleep(10)
                if not self.hesapGizliMi():
                    klasoradi = self.driver.find_element_by_css_selector("h2.BrX75").find_element_by_css_selector(
                        "a.FPmhX").text
                    self.klasorOlustur(klasoradi)
                    img = self.driver.find_element_by_css_selector("div.KL4Bh").find_element_by_tag_name(
                        "img").get_attribute("src")
                    isim = str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".jpg"
                    urllib.request.urlretrieve(img, isim)
                    print(self.uyariOlustur("[+] " + img + " indirildi", 1))
                    self.klasorDegistir("../")
                    self.fotografIndir()
                else:
                    print(self.uyariOlustur(
                        "[-] " + url + " paylaşımının sahibinin profili gizli hesap olduğundan fotoğraf indirme işlemi yapılamıyor!",
                        2))
                    self.fotografIndir()
            except Exception as e:
                print(self.uyariOlustur("[-] " + url + " paylaşımını indirme işlemi sırasında hata:" + str(e), 2))
                self.fotografIndir()
        else:
            print(self.uyariOlustur("[-] indirmek istediğiniz fotoğrafın url'sine ulaşılamadı!", 2))
            self.fotografIndir()

    def videoIndir(self):
        url = input("İndirmek istediğiniz video url >> ").strip()

        if not url:
            self.videoIndir()
        elif url == "menu":
            self.menu()

        if self.urlKontrol(url):
            try:
                self.driver.get(url)
                print("[*] '" + url + "' adresindeki video'nun indirme işlemi başladı...")
                time.sleep(10)
                if not self.hesapGizliMi():
                    klasoradi = self.driver.find_element_by_css_selector("h2.BrX75").find_element_by_css_selector(
                        "a.FPmhX").text
                    self.klasorOlustur(klasoradi)
                    video = self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                    isim = str(datetime.datetime.now()).replace(":", "_").replace(" ", "") + ".mp4"
                    urllib.request.urlretrieve(video, isim)
                    print(self.uyariOlustur("[+] " + video + " indirildi", 1))
                    self.klasorDegistir("../")
                    self.videoIndir()
                else:
                    print(self.uyariOlustur(
                        "[-] " + url + " paylaşımının sahibinin profili gizli hesap olduğundan video indirme işlemi yapılamıyor!",
                        2))
                    self.videoIndir()
            except Exception as e:
                print(self.uyariOlustur("[-] " + url + " paylaşımını indirme işlemi sırasında hata:" + str(e), 2))
                self.videoIndir()
        else:
            print(self.uyariOlustur("[-] indirmek istediğiniz video'nun url'sine ulaşılamadı!", 2))
            self.videoIndir()

    def urlKontrol(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 404:
                return False
            else:
                return True
        except:
            return False



    def uyariOlustur(self, mesaj, durum):
        if durum == 1:
            return colored(mesaj, "green")
        elif durum == 2:
            return colored(mesaj, "red")
        elif durum == 3:
            return colored(mesaj, "blue")

    def klasorOlustur(self, klasor):
        if not os.path.exists(klasor):
            os.mkdir(klasor)
            print(self.uyariOlustur("[+] '" + klasor + "' adında klasör oluşturuldu", 1))
            self.klasorDegistir(klasor)
            print("[*] '" + klasor + "' klasörüne geçiş yapıldı")
        else:
            print("[*] " + klasor + " adında klasör zaten mevcut")
            self.klasorDegistir(klasor)
            print("[*] '" + klasor + "' klasörüne geçiş yapıldı")

    def klasorDegistir(self, klasor):
        os.chdir(klasor)

    def cikisYap(self):
        print("[*] İnstagramdan çıkış yapılıyor...")
        try:
            self.driver.get(self.BASE_URL + self.aktifKullanici)
            time.sleep(3)
            self.driver.find_element_by_css_selector("span.glyphsSpriteUser__outline__24__grey_9").click()
            time.sleep(5)
            ayarlar = self.driver.find_element_by_css_selector("span.glyphsSpriteSettings__outline__24__grey_9")
            ayarlar.click()
            time.sleep(3)
            cikis = self.driver.find_element_by_xpath("/html/body/div[3]/div/div/div/button[6]")
            cikis.click()
            print(self.uyariOlustur("[*] İnstagramdan çıkış yapıldı...", 1))
            self.driver.get(self.BASE_URL + 'accounts/login/')
            self.girisYapildimi = False
            self.girisYap()
        except Exception as e:
            print(self.uyariOlustur("[-] İnstagramdan çıkış işlemi sırasında hata:" + str(e), 2))
            self.menu()

    def quit(self):
        try:
            print("[*] Uygulamadan çıkış yapılıyor...")
            self.driver.quit()
            print(self.uyariOlustur("[*] Uygulamadan çıkış yapıldı...", 1))
            exit()
        except Exception as e:
            print(self.uyariOlustur("[-] Uygulamadan çıkış sırasında hata oluştu:" + str(e), 2))
            self.menu()


try:
    instagram = Instagram()
except KeyboardInterrupt:
    print("\n [*] Python uygulamasından çıkış yapılıyor...")
    exit()


