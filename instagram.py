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
from random import randint


class Instagram():
    def __init__(self):
        init(convert=True)
        self.script()
        self.tarayiciThreadOlustur()
        self.girisYapildimi = False
        self.tarayiciAcildimi = False
        self.aktifKullanici = ""
        self.index = 1
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
        print(self.uyariOlustur(" 1 -)  Tüm Gönderileri İndir", 3))
        print(self.uyariOlustur(" 2 -)  Tüm Gönderileri Beğen", 3))
        print(self.uyariOlustur(" 3 -)  Tüm Gönderileri Beğenmekten Vazgeç", 3))
        print(self.uyariOlustur(" 4 -)  Toplu Takipten Çıkma", 3))
        print(self.uyariOlustur(" 5 -)  Bir Gönderiye Toplu Yorum Yapma", 3))
        print(self.uyariOlustur(" 6 -)  Takip Etmeyenleri Takipten Çıkma", 3))
        print(self.uyariOlustur(" 7 -)  Toplu Mesaj Silme", 3))
        print(self.uyariOlustur(" 8 -)  Öne Çıkan Hikaye İndirme", 3))
        print(self.uyariOlustur(" 9 -)  Hikaye İndirme", 3))
        print(self.uyariOlustur(" 10 -) Tek Gönderi İndirme", 3))
        print(self.uyariOlustur(" 11 -) IG TV Video İndirme", 3))
        print(self.uyariOlustur(" 12 -) Bir Kullanıcının Takipçilerini Takip Etme", 3))
        print(self.uyariOlustur(" 13 -) Bir Dosyadaki Tüm Kullanıcıları Takip Etme", 3))
        print(self.uyariOlustur(" 14 -) Bir Gönderiyi Beğenleri Takip Etme", 3))
        print(self.uyariOlustur(" 15 -) Etikete Göre Gönderileri Beğenme", 3))
        print(self.uyariOlustur(" 16 -) Etikete Göre Kullanıcıları Takip Etme", 3))
        print(self.uyariOlustur(" 17 -) Tek Gönderi Beğenme", 3))
        print(self.uyariOlustur(" 18 -) Tek Gönderi Beğenmekten Vazgeçme", 3))
        print(self.uyariOlustur(" 19 -) Bir Gönderiye Yorum Yapma", 3))
        print(self.uyariOlustur(" 20 -) Kullanıcı Takip Etme", 3))
        print(self.uyariOlustur(" 21 -) Kullanıcı Takip Etmekten Vazgeçme", 3))
        print(self.uyariOlustur(" 22 -) Kullanıcı Engelleme", 3))
        print(self.uyariOlustur(" 23 -) Kullanıcı Engeli Kaldırma", 3))
        print(self.uyariOlustur(" 24 -) İnstagram Çıkış Yapma", 3))
        print(self.uyariOlustur(" 25 -) Uygulama'dan Çıkış Yapma", 3))
        print("")
        self.islemSec()

    def islemSec(self):
        secim = input(" İşlem yapmak için bir seçim yapınız >> ").strip()
        if secim:
            try:
                secim = int(secim)
                if 0 < secim < 26:
                    self.secilenIslemiGoster(secim)
                    if secim in [1,2,3,9,12,20,21,22,23]:
                        self.profilSec(secim)
                    elif secim==4:
                        self.topluTakiptenCik()
                    elif secim==5:
                        self.topluYorumYapma()
                    elif secim==6:
                        self.takipEtmeyenleriTakiptenCik()
                    elif secim==7:
                        self.topluMesajSilme()
                    elif secim==8:
                        self.oneCikanHikayeIndir()
                    elif secim in [10,11]:
                        self.gonderiIndir()
                    elif secim==13:
                        self.kullaniciListesiTakipEt()
                    elif secim==14:
                        self.gonderiBegenenleriTakipEt()
                    elif secim==15:
                        self.etiketeGoreBegenme()
                    elif secim==16:
                        self.etiketeGoreTakipEtme()
                    elif secim==17:
                        self.gonderiBegen()
                    elif secim==18:
                        self.gonderiBegen(False)
                    elif secim==19:
                        self.gonderiYorumYapma()
                    elif secim==24:
                        self.cikisYap()
                    elif secim==25:
                        self.quit()
                else:
                    print(self.uyariOlustur("[-] Lütfen geçerli bir seçim yapınız!", 2))
                    self.islemSec()
            except Exception:
                print(self.uyariOlustur("[-] Yapılacak işlem , başındaki sayıya göre seçilmeli.", 2))
                self.islemSec()
        else:
            self.islemSec()

    def secilenIslemiGoster(self, secim):
        print("")
        secimler = {
            1: "Seçilen İşlem >>> Tüm Gönderileri İndir",
            2: "Seçilen İşlem >>> Tüm Gönderileri Beğen",
            3: "Seçilen İşlem >>> Tüm Gönderileri Beğenmekten Vazgeç",
            4: "Seçilen İşlem >>> Toplu Takipten Çıkma",
            5: "Seçilen İşlem >>> Bir Gönderiye Toplu Yorum Yapma",
            6: "Seçilen İşlem >>> Takip Etmeyenleri Takipten Çıkma",
            7: "Seçilen İşlem >>> Toplu Mesaj Silme",
            8: "Seçilen İşlem >>> Öne Çıkan Hikaye İndirme",
            9: "Seçilen İşlem >>> Hikaye İndirme",
            10: "Seçilen İşlem >>> Tek Gönderi İndirme",
            11: "Seçilen İşlem >>> IG TV Video İndirme",
            12: "Seçilen İşlem >>> Bir Kullanıcının Takipçilerini Takip Etme",
            13: "Seçilen İşlem >>> Bir Dosyadaki Tüm Kullanıcıları Takip Etme",
            14: "Seçilen İşlem >>> Bir Gönderiyi Beğenleri Takip Etme",
            15: "Seçilen İşlem >>> Etikete Göre Gönderileri Beğenme",
            16: "Seçilen İşlem >>> Etikete Göre Kullanıcıları Takip Etme",
            17: "Seçilen İşlem >>> Tek Gönderi Beğenme",
            18: "Seçilen İşlem >>> Tek Gönderi Beğenmekten Vazgeçme",
            19: "Seçilen İşlem >>> Bir Gönderiye Yorum Yapma",
            20: "Seçilen İşlem >>> Kullanıcı Takip Etme",
            21: "Seçilen İşlem >>> Kullanıcı Takip Etmekten Vazgeçme",
            22: "Seçilen İşlem >>> Kullanıcı Engelleme",
            23: "Seçilen İşlem >>> Kullanıcı Engeli Kaldırma",
            24: "Seçilen İşlem >>> İnstagram Çıkış Yapma",
            25: "Seçilen İşlem >>> Uygulama'dan Çıkış Yapma",
        }
        print(self.uyariOlustur(secimler.get(secim, "Geçersiz seçim!"), 1))
        if secim < 24:
            print(self.uyariOlustur(" [*] Ana menüye dönmek için  'menu' komutunu giriniz", 3))
        print("")

    def anaMenuyeDonsunMu(self,deger):
        if deger == "menu":
            self.menu()

    def profilSec(self, secim):
        kullanici = input(" İşlem yapmak istediğiniz profilin kullanıcı adı >> ").strip()

        if not kullanici:
            self.profilSec(secim)

        self.anaMenuyeDonsunMu(kullanici)

        if self.kullaniciKontrol(kullanici):
            print("[*] Tarayıcı {kullanici} profiline yönlendiriliyor...".format(kullanici=kullanici))
            if secim == 1:
                self.gonderileriIndir(kullanici, secim)
            elif secim == 2:
                self.gonderileriBegen(kullanici, secim)
            elif secim == 3:
                self.gonderileriBegen(kullanici, secim, False)
            elif secim==9:
                self.hikayeIndir(kullanici,secim)
            elif secim==12:
                self.kullaniciTakipcileriniTakipEt(kullanici,secim)
            elif secim==20:
                self.kullaniciTakipEt(kullanici, secim)
            elif secim==21:
                self.kullaniciTakipEt(kullanici, secim,False)
            elif secim == 22:
                self.kullaniciEngelle(kullanici, secim)
            elif secim == 23:
                self.kullaniciEngelle(kullanici, secim,False)
        else:
            print(self.uyariOlustur("[-] {kullanici} adında bir kullanıcı bulunamadı ".format(kullanici=kullanici), 2))
            self.profilSec(secim)

    def kullaniciProfilineYonlendir(self,kullanici):
        self.driver.get(self.BASE_URL + kullanici)
        time.sleep(5)

    def urlYonlendir(self,url):
        self.driver.get(url)
        time.sleep(5)

    def tarayiciThreadOlustur(self):
        t1 = threading.Thread(target=self.tarayiciBaslat)
        t1.daemon = True
        t1.start()

    def tarayiciBaslat(self):
        print(self.uyariOlustur("[*] Tarayıcı Başlatılıyor...", 1))
        self.driver = webdriver.Firefox(firefox_profile=self.dilDegistir(),
                                        executable_path="E:\\Python\\Uygulamalar\\Intagram-Bot\\Instagram-Bot\\geckodriver.exe")
        self.driver.get(self.BASE_URL + 'accounts/login/')

    def mesajSil(self,mesaj):
        mesaj.click()
        time.sleep(self.beklemeSuresiBelirle(1, 2))
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button[1]").click()

    def topluMesajSilme(self):
        try:
            print("[*] Toplu mesaj silme işlemi başladı.")
            self.kullaniciProfilineYonlendir('direct/inbox/')
            devamEtsinMi = True
            silinenMesajlar = set()
            self.indexSifirla()
            while devamEtsinMi:
                mesajListesi = self.driver.find_elements_by_css_selector("div.N9abW  a.rOtsg")
                if len(mesajListesi) == 0:
                    print("[*] Mesaj kutusunda mesaj bulunmamaktadır.")
                    break
                for mesaj in mesajListesi:
                    if mesaj not in silinenMesajlar:
                        silinenMesajlar.add(mesaj)
                        kullaniciAdi = mesaj.find_element_by_css_selector("._7UhW9.xLCgt.MMzan.KV-D4.fDxYl").text
                        print(self.uyariOlustur("[*] {index} -) {kullaniciAdi} ile yapılan mesajlaşma silinecek.".format(index=self.index,kullaniciAdi=kullaniciAdi),1))
                        self.mesajSil(mesaj)
                        print(self.uyariOlustur("[*] {index} -) {kullaniciAdi} ile yapılan mesajlaşma başarıyla silindi.".format(index=self.index, kullaniciAdi=kullaniciAdi), 1))
                        self.indexArtir()
                        time.sleep(self.beklemeSuresiBelirle(5,15))
                    break

            print("[*] Toplu mesaj silme işlemi tamamlandı.")
            self.menu()
        except Exception as error:
            print(self.uyariOlustur(
                '[-] Toplu mesaj  aşağıda kaydırma işlemi sırasında bir hata oluştu: {hata}'.format(hata=str(error)),
                2))
            self.menu()



    def degerVarMi(self, yorum):
        if len(yorum) > 0:
            return True
        else:
            return False

    def yorumUzunlukBelirle(self, yorum):
        return yorum[0:randint(5,100)]

    def yorumYap(self, yorum):
        try:

            textarea = self.driver.find_element_by_class_name('Ypffh')
            self.inputTemizle(textarea)
            textarea.click()
            textarea = self.driver.find_element_by_class_name('Ypffh')

            textarea.send_keys(yorum)
            textarea.send_keys(Keys.ENTER)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] {url} gönderisine yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)),
                2))

    def rastgeleYorumGetir(self):
        try:
            return requests.get("http://metaphorpsum.com/paragraphs/1/1").text
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Rastgele yorum getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

    def yorumLimitiAsildiMi(self, yorumSayisi):
        if yorumSayisi > 50:
            return True
        else:
            return False

    def dosyaİceriginiAl(self, dosya):
        try:
            icerik = set()
            with open(dosya, "r", encoding="utf-8") as satirlar:
                for satir in satirlar:
                    if len(satir.strip()) > 0:
                        icerik.add(satir)
            return icerik
        except Exception as error:
            print(self.uyariOlustur("[-] Seçilen dosyanın yüklenme işlemi sırasında bir hata oluştu:{hata}".format(hata=str(error)), 2))
            return False

    def dosyaİcerigiAlindiMi(self, icerik):
        if icerik:
            return True
        else:
            return False

    def topluYorumYapma(self, url=None, yorumSayisi=None, secilenIslem=None):
        try:
            if not url:
                url = input("Yorum yapmak istediğiniz gönderi url'isini giriniz >> ").strip()

                self.anaMenuyeDonsunMu(url)

                if self.urlKontrol(url):
                    print("[*] {url}  gönderisine yönlendiriliyor...".format(url=url))
                    self.urlYonlendir(url)

                    if not self.sayfaMevcutMu():
                        print(self.uyariOlustur("[-] {url} url'sine ulaşılamadı!".format(url=url), 2))
                        self.topluYorumYapma()

                    if self.hesapGizliMi():
                        print(self.uyariOlustur(
                            "[-] {url} gönderisinin sahibinin hesabı gizli hesap olduğundan dolayı toplu yorum yapma işlemi gerçekleştirilemiyor".format(
                                url=url), 2))
                        self.topluYorumYapma()
                else:
                    print(self.uyariOlustur("[-] Gönderi url'si girmediniz!!", 2))
                    self.topluYorumYapma()

            if not yorumSayisi:
                yorumSayisi = input("Yapmak istediğiniz yorum sayısını giriniz >> ").strip()
                self.anaMenuyeDonsunMu(yorumSayisi)
                if yorumSayisi.isnumeric() and int(yorumSayisi) > 0:
                    yorumSayisi = int(yorumSayisi)
                    if self.yorumLimitiAsildiMi(yorumSayisi):
                        yorumSayisi = 50
                        print(self.uyariOlustur(
                            "[*] En fazla 50 yorum yapabilirsiniz.Yorum sayısı 50 olarak belirlenmiştir!", 2))
                else:
                    print(self.uyariOlustur("[-] Yapmak istediğiniz yorum sayısını girmediniz!", 2))
                    self.topluYorumYapma(url=url, yorumSayisi=None, secilenIslem=None)

            if not secilenIslem:
                print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                print(self.uyariOlustur("Uygulama ile oluşturan rastgele yorumlar ile işlem yapmak için 1,", 3))
                print(
                    self.uyariOlustur("Txt dosyasından olarak oluşturduğunuz yorumlar ile işlem yapmak için 2 giriniz.",
                                      3))
                print("")
                secilenIslem = str(input("Uygulama ile oluşturan rastgele yorumlar seçilsin mi? >> ").strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                print(
                    self.uyariOlustur("Seçilen İşlem >>> Uygulama ile oluşturan rastgele yorumlar ile işlem yapma", 1))
                print("[*] {url}  gönderisine toplu yorum yapma işlemi başladı.".format(url=url))
                try:
                    for i in range(yorumSayisi):
                        yorum = self.rastgeleYorumGetir()
                        yorum = self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        print("[*] {index}.yorum yapıldı.".format(index=i + 1))
                        time.sleep(self.beklemeSuresiBelirle(5,20))
                except Exception as error:
                    print(self.uyariOlustur(
                        "[-] {url} gönderisine toplu yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(
                            url=url,
                            hata=str(
                                error)),
                        2))
            elif secilenIslem == "2":
                print(self.uyariOlustur(
                    "Seçilen İşlem >>> Txt dosyasından olarak oluşturduğunuz yorumlar ile işlem yapma", 1))
                dosya = self.dosyaSec(1)
                yorumlar = self.dosyaİceriginiAl(dosya)
                if self.dosyaİcerigiAlindiMi(yorumlar):
                    print("[*] {url}  gönderisine toplu yorum yapma işlemi başladı.".format(url=url))
                    for index, yorum in enumerate(yorumlar):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        print("[*] {index}.yorum yapıldı.".format(index=index + 1))
                        if (index + 1) == yorumSayisi:
                            break
                        time.sleep(self.beklemeSuresiBelirle(5,20))
                else:
                    self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=secilenIslem)
            else:
                print(
                    self.uyariOlustur("[-] Bir seçim yapmadınız!.Lütfen yapmak istediğiniz işlemin numarasını giriniz!",
                                      2))
                print("")
                self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=None)

            print("[*] {url}  gönderisine toplu yorum yapma işlemi tamamlandı.".format(url=url))
            self.topluYorumYapma()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] {url} gönderisine toplu yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(url=url,
                                                                                                          hata=str(
                                                                                                              error)),
                2))
            self.topluYorumYapma()



    def gonderiYorumYapma(self, url=None, yorum=None):
        try:
            if not url:
                url = input("Yorum yapmak istediğiniz gönderi url'isini giriniz >> ").strip()
                self.anaMenuyeDonsunMu(url)
            if not yorum:
                yorum = input("Yorumunuzu giriniz >> ").strip()
                self.anaMenuyeDonsunMu(yorum)

            if self.urlKontrol(url):
                self.urlYonlendir(url)

                if not self.sayfaMevcutMu():
                    print(
                        self.uyariOlustur("[-] Yorum yapmak istediğiniz öne çıkan hikayenin url'sine ulaşılamadı!", 2))
                    self.gonderiYorumYapma()

                if not self.hesapGizliMi():
                    if self.degerVarMi(yorum):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        print("[*] {url}  gönderisine yorum yapma işlemi başladı.".format(url=url))
                        self.yorumYap(yorum)
                        print("[*] {url}  gönderisine yorum yapma işlemi tamamlandı.".format(url=url))
                    else:
                        print(
                            self.uyariOlustur("[-] Yorum girişi yapmadınız!", 2))
                        self.gonderiYorumYapma(url=url, yorum=None)
                else:
                    print(self.uyariOlustur(
                        "[-] {url} gönderisinin sahibinin hesabı gizli hesap olduğundan dolayı yorum yapma işlemi gerçekleştirilemiyor".format(
                            url=url), 2))
            else:
                print(self.uyariOlustur("[-] {url} url'sine ulaşılamadı!".format(url=url), 2))
                self.gonderiYorumYapma(url=None, yorum=yorum)
            self.gonderiYorumYapma()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] {url} gönderisine yorum yapma işlemi sırasında bir hata oluştu: {hata}".format(url=url,
                                                                                                    hata=str(error)),
                2))
            self.gonderiYorumYapma()

    def gonderiIlerlet(self):
        try:
            self.driver.find_element_by_css_selector("a._65Bje").click()
        except:
            pass

    def etiketGetir(self):
        try:
            etiket = input("Bir etiket adı giriniz >> ").strip()
            self.anaMenuyeDonsunMu(etiket)

            if self.degerVarMi(etiket):
                url = "{BASE_URL}explore/tags/{etiket}".format(BASE_URL=self.BASE_URL, etiket=str(etiket))
                print("[*] {url}  sayfasına yönlendiriliyor...".format(url=url))
                self.urlYonlendir(url)
                if not self.sayfaMevcutMu():
                    print(self.uyariOlustur("[-] {etiket} etiketine ait bir gönderi bulunamadı!".format(etiket=etiket),
                                            2))
                    return self.etiketGetir()
                return etiket
            else:
                print(self.uyariOlustur("[-] Bir etiket girişi yapmadınız!", 2))
                return self.etiketGetir()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Etiket belirleme işlemi yapma sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

    def etiketeGoreIslemLimitiGetir(self, islemNo):
        try:
            if islemNo == 1:
                limit = input("Beğenmek istediğiniz gönderi sayısını giriniz >> ").strip()
            elif islemNo == 2:
                limit = input("Takip etmek istediğiniz kullanıcı sayısını giriniz >> ").strip()

            self.anaMenuyeDonsunMu(limit)
            if limit.isnumeric() and int(limit) > 0:
                return int(limit)
            else:
                print(self.uyariOlustur("[-] Bir sayı girişi yapmadınız!", 2))
                return self.etiketeGoreIslemLimitiGetir(islemNo=islemNo)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Belirleyen etikete göre işlem yapma limiti belirleme işlemi yapma sırasında bir hata oluştu: {hata}".format(
                    hata=str(error)), 2))
            if islemNo == 1:
                self.etiketeGoreBegenme()
            elif islemNo == 2:
                self.etiketeGoreTakipEtme()


    def etiketeGoreTakipEtme(self):
        try:
            etiket = self.etiketGetir()

            limit = self.etiketeGoreIslemLimitiGetir(2)

            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            ilkGonderi = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")
            ilkGonderi.click()
            time.sleep(1)
            self.indexSifirla()

            print("[*] {etiket}  etiketine göre kullanıcı takip etme işlemi başladı.".format(etiket=etiket))
            while True:
                kullanici = self.driver.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]")
                kullaniciAdi = kullanici.find_element_by_css_selector("a.sqdOP").text
                btn_takip = kullanici.find_element_by_css_selector("button.oW_lN")
                if btn_takip.text != "Following":
                    btn_takip.click()
                    print(self.uyariOlustur(
                        "[+] {index}-) {kullanici} takip edilmeye başlandı.".format(index=self.index,
                                                                                    kullanici=kullaniciAdi), 1))
                    self.indexArtir()
                    if self.index-1 >= limit:
                        break
                    time.sleep(0.50)
                    self.gonderiIlerlet()
                    time.sleep(self.beklemeSuresiBelirle(5,20))
                else:
                    print(self.uyariOlustur("[*] {kullanici} zaten takip ediliyor.".format(kullanici=kullaniciAdi), 1))
                    self.gonderiIlerlet()
                    time.sleep(5)
            print("[*] {etiket}  etiketine göre kullanıcı takip etme işlemi tamamlandı.".format(etiket=etiket))
            self.etiketeGoreTakipEtme()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Etikete göre beğeni işlemi yapma sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.etiketeGoreTakipEtme()

    def begenButonuGetir(self):
        return self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")

    def begenButonuDurumGetir(self, buton):
        return str(buton.find_element_by_tag_name("svg").get_attribute("aria-label")).lower()

    def etiketeGoreBegenme(self):
        try:
            etiket = self.etiketGetir()
            limit = self.etiketeGoreIslemLimitiGetir(1)
            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            ilkGonderi = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")
            ilkGonderi.click()
            time.sleep(1)
            self.indexSifirla()

            print("[*] {etiket}  etiketine göre beğeni yapma işlemi başladı.".format(etiket=etiket))
            while True:
                btn_begen = self.begenButonuGetir()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if begeniDurum != "unlike":
                    btn_begen.click()
                    print(self.uyariOlustur("[+] {index}-) {url} gönderisi beğenildi.".format(index=self.index,
                                                                                              url=self.driver.current_url),
                                            1))
                    self.indexArtir()
                    if self.index-1 >= limit:
                        break
                    time.sleep(0.50)
                    self.gonderiIlerlet()
                    time.sleep(self.beklemeSuresiBelirle(5,15))
                else:
                    print(self.uyariOlustur(
                        "[*] {url} gönderisi daha önce beğenildi.".format(url=self.driver.current_url), 1))
                    self.gonderiIlerlet()
                    time.sleep(5)
            print("[*] {etiket}  etiketine göre beğeni yapma işlemi tamamlandı.".format(etiket=etiket))
            self.etiketeGoreBegenme()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Etikete göre beğeni işlemi yapma sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.etiketeGoreBegenme()

    def hikayeVarMi(self):
        try:
            durum = self.driver.find_element_by_css_selector("div.RR-M-").get_attribute("aria-disabled")
            if durum == "false":
                return True
            else:
                return False
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Hikaye olup olmadığı işleminin kontrolü sırasına bir hata oluştu: {hata}".format(hata=str(error)),
                2))

    def hikayeVideoMu(self):
        try:
            self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5")
            return True
        except:
            return False

    def hikayeSayisiGetir(self):
        try:
            hikayeSayisi = self.driver.find_elements_by_css_selector("div.w9Vr-  > div._7zQEa")
            return len(hikayeSayisi)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Hikaye sayısı getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

    def hikayeleriGetir(self):
        try:
            for i in range(self.hikayeSayisiGetir()):
                if self.hikayeVideoMu():
                    url = self.driver.find_element_by_css_selector("div.qbCDp > video.y-yJ5 > source").get_attribute(
                        "src")
                    self.dosyaIndir(url, 2)
                else:
                    foto_srcset = str(
                        self.driver.find_element_by_css_selector("div.qbCDp >  img.y-yJ5").get_attribute("srcset"))
                    url = (foto_srcset.split(",")[-1]).split(" ")[0]
                    self.dosyaIndir(url, 1)
                btn_ileri = self.driver.find_element_by_css_selector("button.ow3u_")
                btn_ileri.click()
                time.sleep(1)
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

    def hikayeIndir(self,kullanici,secim):
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                if self.hikayeVarMi():
                    self.driver.find_element_by_css_selector("div.RR-M-").click()
                    time.sleep(3)
                    print("[*] {kullanici} kullanıcısının hikayelerini indirme işlemi başladı.".format(
                        kullanici=kullanici))
                    self.klasorOlustur(kullanici)
                    self.indexSifirla()
                    self.hikayeleriGetir()
                    self.klasorDegistir("../")
                    print("[*] {kullanici} kullanıcısının hikayelerini indirme işlemi tamamlandı.".format(
                        kullanici=kullanici))
                else:
                    print(self.uyariOlustur("[-] Hikaye bulunamadı!", 2))
            else:
                print(self.uyariOlustur(
                    "[-] {kullanici} adlı kişinin hesabı gizli hesap olduğundan takipçileri takip edilemiyor!".format(
                        kullanici=kullanici), 2))
            self.profilSec(secim)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Hikayeleri indirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.profilSec(secim)



    def indexSifirla(self):
        self.index = 1

    def indexArtir(self):
        self.index = self.index + 1

    def oneCikanHikayeIndir(self):
        try:
            url = input("Öne çıkan hikaye url giriniz >> ").strip()
            self.anaMenuyeDonsunMu(url)
            if self.urlKontrol(url):
                self.urlYonlendir(url)

                if not self.sayfaMevcutMu():
                    print(self.uyariOlustur("[-] İndirmek istediğiniz öne çıkan hikayenin url'sine ulaşılamadı!", 2))
                    self.oneCikanHikayeIndir()

                print("[*] {url}  öne çıkan hikayesini indirme işlemi başladı".format(url=url))
                btn_oynat = self.driver.find_element_by_css_selector("button._42FBe")
                btn_oynat.click()
                time.sleep(1)
                kullanici = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/div/div/section/header/div/div[1]/div/div/div/a").get_attribute("title")
                self.klasorOlustur(kullanici)
                self.indexSifirla()
                self.hikayeleriGetir()
                self.klasorDegistir("../")
                print("[*] {url}  öne çıkan hikayesini indirme işlemi tamamlandı.".format(url=url))
            else:
                print(self.uyariOlustur("[-] İndirmek istediğiniz öne çıkan hikayenin url'sine ulaşılamadı!", 2))
            self.oneCikanHikayeIndir()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Öne çıkan hikayeyi indirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.oneCikanHikayeIndir()

    def dosyaAdiOlustur(self,veriTuru):
        dt=str(datetime.datetime.now()).replace(":", "_").replace(" ", "")
        if veriTuru == 1:
            isim="{index}_{tarih}.jpg".format(index=str(self.index),tarih=dt)
        elif veriTuru == 2:
            isim = "{index}_{tarih}.mp4".format(index=str(self.index), tarih=dt)
        return isim

    def dosyaIndir(self, url, veriTuru):
        try:
            dosyaAdi=self.dosyaAdiOlustur(veriTuru)
            urllib.request.urlretrieve(url, dosyaAdi)
            print(self.uyariOlustur("[+] {url} indirildi".format(url=url), 1))
            self.indexArtir()
        except Exception as error:
            print(self.uyariOlustur(
                '[-] dosya indirme işlemi sırasında bir hata oluştu: {hata}'.format(hata=str(error)), 2))

    def topluTakiptenCik(self):
        try:
            print("[*] Toplu takipten çıkma işlemi başladı.")
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            takipEdilenSayisi = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
            takipEdilenSayisi = int(self.metindenKarakterSil(takipEdilenSayisi, ','))

            btn_takipEdilenler = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            btn_takipEdilenler.click()
            time.sleep(3)
            self.indexSifirla()
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = self.takipEdilenKullaniciAdiGetir(element=takip)
                    btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                    if btn_takip.text == "Following":
                        btn_takip.click()
                        time.sleep(2)
                        try:
                            btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                            btn_onay.click()
                        except Exception as error:
                            print(self.uyariOlustur(
                                '[-] {kullaniciAdi} kullanıcısını takipten çıkma işlemi sırasında bir hata oluştu: {hata}'.format(
                                    kullaniciAdi=takipEdilenKullanıcıAdi, hata=str(error)), 2))
                            continue
                        print(self.uyariOlustur(
                            "[*] {index} -) {kullaniciAdi} adlı kullanıcı takip edilmekten vazgeçildi.".format(
                                index=self.index, kullaniciAdi=takipEdilenKullanıcıAdi), 1))
                        self.indexArtir()
                        if (self.index - 1) >= takipEdilenSayisi:
                            devamEtsinMi = False
                            break
                        time.sleep(self.beklemeSuresiGetir(5, 15))
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        print(self.uyariOlustur(
                            '[-] Popup aşağıda kaydırma işlemi sırasında bir hata oluştu: {hata}'.format(
                                hata=str(error)), 2))
                        pass
                    time.sleep(3)
            self.menu()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Toplu takipten çıkma işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.menu()

    def takipEdilenSayisiGetir(self):
        takipEdilenSayisi = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
        return int(self.metindenKarakterSil(takipEdilenSayisi, ','))

    def takipEdilenKullaniciAdiGetir(self, element):
        takipEdilenKullanıcıAdi = element.find_element_by_css_selector("a.FPmhX").get_attribute('href')
        return self.metindenKarakterSil(self.metindenKarakterSil(takipEdilenKullanıcıAdi, self.BASE_URL), '/')

    def beklemeSuresiGetir(self, baslangic, bitis):
        return randint(baslangic, bitis)

    def takipEdilenleriGetir(self, takipciler):
        try:
            print("[*] Takip etmeyen kullanıcıları takipten çıkma işlemi başladı.")
            takipEdilenSayisi = self.takipEdilenSayisiGetir()

            btn_takipEdilenler = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            btn_takipEdilenler.click()
            time.sleep(5)
            self.indexSifirla()
            islemIndex = 0
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takip in takipListe:
                    takipEdilenKullanıcıAdi = self.takipEdilenKullaniciAdiGetir(element=takip)

                    if takipEdilenKullanıcıAdi not in takipciler:
                        btn_takip = takip.find_element_by_css_selector('button.sqdOP')
                        if btn_takip.text == "Following":
                            btn_takip.click()
                            time.sleep(2)
                            try:
                                btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                                btn_onay.click()
                            except Exception as error:
                                print(self.uyariOlustur(
                                    '[-] {kullaniciAdi} kullanıcısını takipten çıkma işlemi sırasında bir hata oluştu: {hata}'.format(
                                        kullaniciAdi=takipEdilenKullanıcıAdi, hata=str(error)), 2))
                                continue
                            print(self.uyariOlustur(
                                "[*] {index} -) {kullaniciAdi} adlı kullanıcı takip edilmekten vazgeçildi.".format(
                                    index=self.index, kullaniciAdi=takipEdilenKullanıcıAdi), 1))
                            self.indexArtir()
                            if self.index - 1 >= takipEdilenSayisi:
                                devamEtsinMi = False
                                break
                            time.sleep(self.beklemeSuresiBelirle(5, 15))
                    islemIndex = islemIndex + 1
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
            self.menu()

    def popupAsagiKaydir(self, secici):
        self.driver.execute_script('''
                                                    var fDialog = document.querySelector('{secici}');
                                                    fDialog.scrollTop = fDialog.scrollHeight
                                                '''.format(secici=secici))

    def takipciSayisiGetir(self):
        takipciSayisi = self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").text
        return int(self.metindenKarakterSil(takipciSayisi, ','))

    def takipcileriGetir(self):
        try:
            print("[*] Tarayıcı profilinize yönlendiriliyor.")
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            print("[*] Takipçileri listeye ekleme işlemi başladı.")
            takipciSayisi = self.takipciSayisiGetir()

            btn_takipciler = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            btn_takipciler.click()
            time.sleep(5)
            takipciler = set()
            self.indexSifirla()
            devamEtsinMi = True
            while devamEtsinMi:
                dialog_popup = self.driver.find_element_by_css_selector('div.pbNvD')
                takipcilerPopup = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                for takipci in takipcilerPopup:
                    takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                    takipciKullaniciAdi = self.metindenKarakterSil(
                        self.metindenKarakterSil(takipciKullaniciAdi, self.BASE_URL), '/')
                    if takipciKullaniciAdi not in takipciler:
                        print(self.uyariOlustur(
                            "[*] {index} -) {takipci} takipcisi listeye eklendi.".format(index=self.index,
                                                                                         takipci=takipciKullaniciAdi),
                            1))
                        takipciler.add(takipciKullaniciAdi)
                        self.indexArtir()
                        if (self.index - 1) >= takipciSayisi:
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
            self.menu()

    def takipEtmeyenleriTakiptenCik(self):
        try:

            takipciler = self.takipcileriGetir()
            print("[*] Takipçileri listeye ekleme işlemi başladı.")
            self.takipEdilenleriGetir(takipciler=takipciler)
            print("[*] Takip etmeyen kullanıcıları takipten çıkma işlemi tamamlandı.")
            self.menu()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Takip etmeyen kullanıcıları takipten çıkma işlemi sırasında bir hata oluştu: {hata}".format(
                    hata=str(error)), 2))
            self.menu()

    def metindenKarakterSil(self, metin, silinecekKarakterler):
        return metin.replace(silinecekKarakterler, '')
        # return ''.join(karakter for karakter in metin if karakter not in silinecekKarakterler)

    def gonderiBegenenleriTakipEt(self, secilenIslem=None):
        try:
            url = input("İşlem yapmak istediğiniz gönderi url >> ").strip()
            self.anaMenuyeDonsunMu(url)

            if not url:
                self.gonderiBegenenleriTakipEt()

            if self.urlKontrol(url):
                print("[*] {url}  gönderisine yönlendiriliyor...".format(url=url))
                self.urlYonlendir(url)
                hedefBegenenSayisi = None

                if secilenIslem is None:
                    print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                    print(self.uyariOlustur("Tüm takipçiler listesi içerisinden işlem yapmak için 1,", 3))
                    print(self.uyariOlustur(
                        "Belirtilen sayı kadar takipçiler listesi içerisinden işlem yapmak için 2 giriniz,", 3))
                    print("")
                    secilenIslem = str(input("Tüm takipçiler listesi içerisinde mi işlem yapılsın ? >> ").strip())
                    self.anaMenuyeDonsunMu(secilenIslem)

                if secilenIslem == "1":
                    print(
                        self.uyariOlustur("Seçilen İşlem >>> Gönderiyi beğenen tüm kullanıcıları takip etme", 1))
                elif secilenIslem == "2":
                    print(self.uyariOlustur(
                        "Seçilen İşlem >>> Belirtilen sayı kadar gönderiyi beğenen tüm kullanıcıları takip etme", 1))
                    hedefBegenenSayisi = input("İşlem yapmak için bir sayı giriniz >>> ").strip()
                    self.anaMenuyeDonsunMu(hedefBegenenSayisi)
                    if hedefBegenenSayisi.isnumeric():
                        hedefBegenenSayisi = int(hedefBegenenSayisi)
                    else:
                        print(self.uyariOlustur("[-] Bir sayı girişi yapmadınız.Lütfen bir sayı giriniz!", 2))
                        print("")
                        self.gonderiBegenenleriTakipEt( secilenIslem=secilenIslem)
                else:
                    print(self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!", 2))
                    print("")
                    self.gonderiBegenenleriTakipEt(secilenIslem=None)

                if not self.hesapGizliMi():
                    if not self.gonderiTipiVideoMu():
                        print("[*] '" + url + "'  gönderisini beğenen kullanıcıları takip etme işlemi başladı...")
                        takipIstekSayisi = 0
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
                                    time.sleep(self.beklemeSuresiGetir(5, 15))

                                self.indexArtir()
                                if hedefBegenenSayisi:
                                    if self.index-1 >= kaynakBegenenSayisi:
                                        devamEtsinMi = False
                                        break
                                else:
                                    if self.index-1 >= begenenSayisi:
                                        devamEtsinMi = False
                                        break
                            if devamEtsinMi:
                                self.popupAsagiKaydir(secici='div[role="dialog"]  .i0EQd > div:nth-child(1)')
                                time.sleep(3)
                            else:
                                print("[*] Takipçi seçme işlemi tamamlandı.")
                    else:
                        print(
                            '[*] {url} gönderisini  beğenen kullanıcıların listesi görüntülenemediğinden dolayı takip etme işlemi yapılamıyor'.format(
                                url=url))
                else:
                    print(self.uyariOlustur(
                        "[-] " + url + " gönderisinin sahibinin profili gizli hesap olduğundan dolayı, bu gönderiyi beğenen kullanıcıların listesi alınamıyor!",
                        2))
            self.gonderiBegenenleriTakipEt()
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Gönderi beğenenleri takip etme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            self.gonderiBegenenleriTakipEt()

    def kullaniciListesiTakipEt(self):
        dosya = self.dosyaSec()
        kullanicilar = self.dosyaİceriginiAl(dosya)
        if self.dosyaİcerigiAlindiMi(kullanicilar):
            self.kullanicilariTakipEt(kullanicilar, 14)
        else:
            self.kullaniciListesiTakipEt()

    def kullanicilariTakipEt(self, kullaniciListesi, secim):
        for kullanici in kullaniciListesi:
            self.kullaniciTakipEt(kullanici.strip(), secim)
            time.sleep(30)
            print(kullanici)

    def dosyaSec(self):
        try:
            dosyaAdi = input("Dosya yolunu giriniz >> ").strip()
            self.anaMenuyeDonsunMu(dosyaAdi)
            if self.dosyaMi(dosyaAdi) and self.txtDosyasiMi(dosyaAdi):
                return str(dosyaAdi)
            else:
                print(self.uyariOlustur("[-] Geçerli bir dosya yolu belirtmediniz.Sadece txt uzantılı dosyaları seçebilirsiniz!", 2))
                return self.dosyaSec()
        except Exception as error:
            print(self.uyariOlustur("[-] Dosya seçme işlemi sırasında bir hata oluştu:" + str(error), 2))
            return self.dosyaSec()

    def dosyaMi(self, path):
        if os.path.isfile(path):
            return True
        else:
            return False

    def txtDosyasiMi(self, dosya):
        if os.path.splitext(dosya)[-1].lower() == ".txt":
            return True
        else:
            return False



    def bildirimThreadOlustur(self):
        t1 = threading.Thread(target=self.bildirimPopupKapat)
        t1.daemon = True
        t1.start()

    def bildirimPopupKapat(self):
        try:
            for i in range(2):
                time.sleep(5)
                btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
                self.driver.execute_script("arguments[0].click();", btn)
        except Exception as error:
            pass

    def dilDegistir(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        return profile

    def aktifKullaniciGetir(self):
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]").click()
            kullanici = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]").get_attribute(
                "href")
            self.aktifKullanici = str(kullanici).replace(self.BASE_URL, "")
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Aktif kullanıcı adı getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))

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
                self.aktifKullaniciGetir()
                self.bildirimThreadOlustur()
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



    def hedefKaynaktanBuyukMu(self, hedef, kaynak):
        if hedef > kaynak:
            hedef = kaynak
        return hedef

    def kullaniciTakipcileriniTakipEt(self, kullanici, secim,secilenIslem=None):
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            hedefTakipciSayisi = None

            if secilenIslem is None:
                print(self.uyariOlustur("       <<< SEÇENEKLER >>>      ", 1))
                print(self.uyariOlustur("Tüm takipçiler listesi içerisinden işlem yapmak için 1,", 3))
                print(self.uyariOlustur(
                    "Belirtilen sayı kadar takipçiler listesi içerisinden işlem yapmak için 2 giriniz,", 3))
                print("")
                secilenIslem = str(input("Tüm takipçiler listesi içerisinde mi işlem yapılsın ? >> ").strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                print(
                    self.uyariOlustur("Seçilen İşlem >>> Tüm takipçiler listesi içerisindeki kullanıcıları takip etme",
                                      1))
            elif secilenIslem == "2":
                print(self.uyariOlustur(
                    "Seçilen İşlem >>> Belirtilen sayı kadar takipçiler listesi içerisindeki kullanıcıları takip etme",
                    1))
                hedefTakipciSayisi = input("İşlem yapmak için bir sayı giriniz >>> ").strip()
                self.anaMenuyeDonsunMu(hedefTakipciSayisi)
                if hedefTakipciSayisi.isnumeric():
                    hedefTakipciSayisi = int(hedefTakipciSayisi)
                else:
                    print(self.uyariOlustur("[-] Bir sayı girişi yapmadınız.Lütfen bir sayı giriniz!", 2))
                    print("")
                    self.kullaniciTakipcileriniTakipEt(kullanici, secim,  secilenIslem=secilenIslem)
            else:
                print(self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!", 2))
                print("")
                self.kullaniciTakipcileriniTakipEt(kullanici, secim, secilenIslem=None)

            print("[*] '" + kullanici + "' kullanıcısının takipçilerini takip etme işlemi başladı...")

            if not self.hesapGizliMi():
                takipIstekSayisi = 0;
                devamEtsinMi = True
                self.indexSifirla()

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
                                time.sleep(self.beklemeSuresiGetir(5, 15))
                        except:
                            pass

                        self.indexArtir()
                        if hedefTakipciSayisi:
                            if self.index-1 >= kaynakTakipciSayisi:
                                devamEtsinMi = False
                        else:
                            if self.index-1 >= takipciSayisi:
                                devamEtsinMi = False

                    if devamEtsinMi:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                        time.sleep(3)
                print("[*] '" + kullanici + "' kullanıcısının takipçilerini takip etme işlemi tamamlandı.")
            else:
                print(self.uyariOlustur(
                    "[-] " + kullanici + " adlı kişinin hesabı gizli hesap olduğundan takipçileri takip edilemiyor!",
                    2))
            self.profilSec(secim)
        except Exception as e:
            print(self.uyariOlustur(
                "[-] " + kullanici + " kullanıcısının takipçilerini takip etme işlemi sırasında hata:" + str(e), 2))
            self.profilSec(secim)

    def kullaniciKontrol(self, kullaniciadi):
        response = requests.get(self.BASE_URL + kullaniciadi)
        if response.status_code == 404:
            return False
        else:
            return True

    def kullaniciTakipDurumDegistir(self,kullanici,durum):
        if self.hesapGizliMi():
            btn_takip = self.driver.find_element_by_css_selector("button.BY3EC")
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    print(self.uyariOlustur(
                        "[+] {kullanici} kullanıcısına takip isteği gönderildi".format(kullanici=kullanici), 1))
                elif btn_text == "requested":
                    print(self.uyariOlustur(
                        "[*] {kullanici} kullanıcısına takip isteği zaten gönderildi".format(kullanici=kullanici),
                        1))
                elif btn_text == "unblock":
                    print(self.uyariOlustur(
                        "[-] {kullanici} kullanıcısı engelli durumda olduğu için takip isteği atılamıyor.".format(
                            kullanici=kullanici), 1))
            else:
                print(self.uyariOlustur(
                    "[-] {kullanici} kullanıcısını zaten takip etmiyorsunuz.".format(
                        kullanici=kullanici), 1))
        else:
            btn_takip = self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN')
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    print(self.uyariOlustur(
                        "[+] {kullanici} kullanıcısı takip edilmeye başlandı.".format(kullanici=kullanici), 1))
                elif btn_text == "unblock":
                    print(self.uyariOlustur(
                        "[-] {kullanici} kullanıcısı engelli durumda olduğu için takip isteği atılamıyor.".format(
                            kullanici=kullanici), 1))
                else:
                    ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                    if ariaLabel == "Following":
                        print(self.uyariOlustur(
                            "[-] {kullanici} kullanıcısını zaten takip ediyorsunuz.".format(
                                kullanici=kullanici), 1))
            else:
                ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                if ariaLabel == "Following":
                    btn_takip.click()
                    time.sleep(0.50)
                    self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()
                    print(self.uyariOlustur(
                        "[+] {kullanici} kullanıcısı takip edilmekten vazgeçildi.".format(kullanici=kullanici), 1))

    def kullaniciTakipEt(self, kullanici, secim,durum=True):
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print("[*] {kullanici} kullanıcısını takip etme işlemi başladı...".format(kullanici=kullanici))
            else:
                print("[*] {kullanici} kullanıcısını takipten çıkma işlemi başladı...".format(kullanici=kullanici))


            self.kullaniciTakipDurumDegistir(kullanici=kullanici,durum=durum)
            if durum:
                print("[*] {kullanici} kullanıcısını takip etme işlemi tamamlandı...".format(kullanici=kullanici))
            else:
                print("[*] {kullanici} kullanıcısını takipten çıkma işlemi tamamlandı...".format(kullanici=kullanici))
            if secim != 14:
                self.profilSec(secim)
        except Exception as error:
            if durum:
                print(self.uyariOlustur("[-] {kullanici} kullanıcısını takip etme işlemi sırasında hata:{hata}".format(kullanici=kullanici,hata=str(error)),2))
            else:
                print(self.uyariOlustur(
                    "[-] {kullanici} kullanıcısını takip etmekten vazgeçme işlemi sırasında hata:{hata}".format(kullanici=kullanici,
                                                                                                   hata=str(error)), 2))
            if secim != 14:
                self.profilSec(secim)


    def kullaniciEngelDurumDegistir(self):
        self.driver.find_element_by_css_selector("button.wpO6b").click()
        time.sleep(0.50)
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()
        time.sleep(0.50)
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()

    def kullaniciEngelle(self, kullanici, secim,durum=True):
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print("[*]  {kullanici} kullanıcısını engelleme işlemi başladı.".format(kullanici=kullanici))
            else:
                print("[*]  {kullanici} kullanıcısının engelini kaldırma işlemi başladı.".format(kullanici=kullanici))

            if self.hesapGizliMi():
                btnText = str(self.driver.find_element_by_css_selector('button.BY3EC').text).lower()
                if durum:
                    if btnText!="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        print(self.uyariOlustur("[-] {kullanici} kullanıcısı zaten engellenmiş durumda".format(kullanici=kullanici), 2))
                else:
                    if btnText=="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        print(self.uyariOlustur("[-] {kullanici} kullanıcısı zaten engellenmemiş durumda.".format(kullanici=kullanici), 2))
            else:
                btnText =str(self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN').text).lower()
                if durum:
                    if btnText != "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        print(self.uyariOlustur(
                            "[-] {kullanici} kullanıcısı zaten engellenmiş durumda.".format(kullanici=kullanici), 2))
                else:
                    if btnText == "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        print(self.uyariOlustur("[-] {kullanici} kullanıcısı zaten engellenmemiş durumda.".format(kullanici=kullanici), 2))

            if durum:
                print("[*]  {kullanici} kullanıcısını engelleme işlemi tamamlandı.".format(kullanici=kullanici))
            else:
                print("[*]  {kullanici} kullanıcısının engelini kaldırma işlemi tamamlandı.".format(kullanici=kullanici))
            self.profilSec(secim)
        except Exception as error:
            if durum:
                print(self.uyariOlustur("[-] {kullanici} kullanıcısını engelleme işlemi sırasında hata:{hata}".format(kullanici=kullanici,hata=str(error)),2))
            else:
                print(self.uyariOlustur("[-] {kullanici} kullanıcısının engelini kaldırma işlemi sırasında hata:{hata}".format(kullanici=kullanici,hata=str(error)), 2))
            self.profilSec(secim)


    def gonderiTipiVideoMu(self, element=None):
        try:
            if element:
                element.find_element_by_css_selector("video.tWeCl")
            else:
                self.driver.find_element_by_css_selector("video.tWeCl")
            return True
        except:
            return False

    def AlbumIcerikSayisiGetir(self):
        try:
            return len(self.driver.find_elements_by_css_selector("div.Yi5aA"))
        except Exception as error:
            print(self.uyariOlustur(
                "[-] {url} gönderisinin album içerik sayısını getirme işlemi sırasında hata:{hata}".format(
                    url=str(self.driver.current_url), hata=str(error)), 2))
            return None

    def gonderiAlbumMu(self):
        try:
            self.driver.find_element_by_css_selector("div.Yi5aA")
            return True
        except:
            return False

    def albumUrlGetir(self):
        try:
            album = set()
            ul = self.driver.find_element_by_css_selector("article ul.vi798")
            for i in range(self.AlbumIcerikSayisiGetir()):
                liste = ul.find_elements_by_css_selector("li.Ckrof")
                for li in liste:
                    [url, veriTuru] = self.albumIcerikUrlGetir(li)
                    if url not in album and url is not None:
                        album.add(url)
                        self.dosyaIndir(url, veriTuru)
                btn_ileri = self.driver.find_element_by_css_selector("button._6CZji div.coreSpriteRightChevron")
                btn_ileri.click()
                time.sleep(1)
        except:
            pass

    def albumIcerikUrlGetir(self, element):
        try:
            veriTuru = None
            if self.gonderiTipiVideoMu(element):
                url = element.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                veriTuru = 2
            else:
                url = element.find_element_by_css_selector("img.FFVAD").get_attribute("src")
                veriTuru = 1
            return url, veriTuru
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Gönderi url'si getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            return None, None

    def gonderiUrlGetir(self, durum=True):
        try:
            veriTuru = None
            if self.gonderiTipiVideoMu():
                url = self.driver.find_element_by_css_selector("video.tWeCl").get_attribute("src")
                veriTuru = 2
            else:
                if durum:
                    url = self.driver.find_element_by_xpath(
                        "/html/body/div[4]/div[2]/div/article/div[2]/div/div/div[1]/img").get_attribute("src")
                else:
                    url = self.driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div[1]/article/div[2]/div/div/div[1]/img").get_attribute(
                        "src")
                veriTuru = 1
            return url, veriTuru
        except Exception as error:
            print(self.uyariOlustur(
                "[-] Gönderi url'si getirme işlemi sırasında bir hata oluştu: {hata}".format(hata=str(error)), 2))
            return None, None

    def gonderiVarMi(self, kullanici, gonderiSayisi, secim):
        if gonderiSayisi < 1:
            print(self.uyariOlustur(
                "[-] {kullanici} adlı kullanıcının gönderileri bulunmamaktadır.".format(kullanici=kullanici), 2))
            self.profilSec(secim)

    def gonderileriIndir(self, kullanici, secim):
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print("[*] {kullanici}  adlı kullanıcının gönderilerini indirme işlemi başladı".format(
                    kullanici=kullanici))
                gonderiSayisi = int(self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text)
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)

                ilkGonderi = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]")
                ilkGonderi.click()
                time.sleep(1)
                self.klasorOlustur(kullanici)
                self.indexSifirla()
                for index in range(gonderiSayisi):
                    if self.gonderiAlbumMu():
                        self.klasorOlustur(str(self.index) + "_album")
                        tempIndex = self.index
                        self.indexSifirla()
                        self.albumUrlGetir()
                        self.klasorDegistir("../")
                        self.index = tempIndex + 1
                    else:
                        [url, veriTuru] = self.gonderiUrlGetir()
                        if url is not None:
                            self.dosyaIndir(url, veriTuru)
                        else:
                            continue
                    self.gonderiIlerlet()
                    time.sleep(3)
                self.klasorDegistir("../")
                print("[*] {kullanici}  adlı kullanıcının gönderilerini indirme işlemi tamamlandı.".format(
                    kullanici=kullanici))
            else:
                print(self.uyariOlustur(
                    "[-] {kullanici} adlı kişinin hesabı gizli hesap olduğundan gönderileri indirme işlemi yapılamıyor!".format(
                        kullanici=kullanici), 2))

            self.profilSec(secim)
        except Exception as error:
            print(self.uyariOlustur(
                "[-] {kullanici} kullanıcısının gönderilerini indirme işlemi sırasında bir hata oluştu:{hata}".format(
                    kullanici=kullanici, hata=error), 2))
            self.profilSec(secim)

    def gonderiIndir(self):
        try:
            url = input("İndirmek istediğiniz gönderi url >> ").strip()
            self.anaMenuyeDonsunMu(url)
            if not url:
                print(self.uyariOlustur("[-] Gönderi url'si girmediniz!!", 2))
                self.gonderiIndir()

            if self.urlKontrol(url):
                print("[*] {url}  gönderisine yönlendiriliyor...".format(url=url))
                self.urlYonlendir(url)
                if not self.hesapGizliMi():
                    print("[*] {url} adresindeki gönderinin indirme işlemi başladı.".format(url=url))
                    kullanici = self.driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div[1]/article/header/div[2]/div[1]/div/span/a").text
                    self.klasorOlustur(kullanici)
                    if self.gonderiAlbumMu():
                        self.indexSifirla()
                        self.klasorOlustur(str(self.index) + "_album")
                        self.albumUrlGetir()
                        self.klasorDegistir("../")
                    else:
                        [url, veriTuru] = self.gonderiUrlGetir(durum=False)
                        if url is not None:
                            self.dosyaIndir(url, veriTuru)
                    print("[*] {url} adresindeki gönderinin indirme işlemi tamamlandı.".format(url=url))
                    self.klasorDegistir("../")
                else:
                    print(self.uyariOlustur(
                        "[-] {url} gönderisinin sahibinin profili gizli hesap olduğundan indirme işlemi yapılamıyor!".format(
                            url=url), 2))
            self.gonderiIndir()
        except Exception as error:
            print(
                self.uyariOlustur("[-] gönderi indirme işlemi sırasında bir hata oluştu:{hata}".format(hata=error), 2))
            self.gonderiIndir()

    def gonderiBegenDurumDegistir(self, btn):
        btn.click()
        self.indexArtir()
        time.sleep(0.50)
        self.gonderiIlerlet()
        time.sleep(self.beklemeSuresiGetir(5, 15))

    def gonderileriBegen(self, kullanici, secim, durum=True):
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print("[*] {kullanici}  adlı kullanıcının gönderilerini beğenme işlemi başladı".format(
                    kullanici=kullanici))
                gonderiSayisi = int(self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text)
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)
                ilkGonderi = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]")
                ilkGonderi.click()
                time.sleep(1)
                self.klasorOlustur(kullanici)
                self.indexSifirla()
                for index in range(gonderiSayisi):
                    btn_begen = self.begenButonuGetir()
                    begeniDurum = self.begenButonuDurumGetir(btn_begen)
                    if durum:
                        if begeniDurum == "like":
                            print(self.uyariOlustur(
                                "[+] {index}-) {url} gönderisi beğenildi.".format(index=str(self.index),
                                                                                  url=self.driver.current_url), 1))
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            print(self.uyariOlustur(
                                "[*] {url} gönderisi daha önce beğenildi.".format(url=self.driver.current_url), 1))
                            self.gonderiIlerlet()
                            time.sleep(5)
                    else:
                        if begeniDurum == "unlike":
                            print(self.uyariOlustur(
                                "[+] {index}-) {url} gönderisi beğenilmekten vazgeçildi.".format(index=str(self.index),
                                                                                                 url=self.driver.current_url),
                                1))
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            print(self.uyariOlustur(
                                "[*] {url} gönderisi zaten beğenilmedi.".format(url=self.driver.current_url), 1))
                            self.gonderiIlerlet()
                            time.sleep(5)
                print("[*] {kullanici}  adlı kullanıcının gönderilerini beğenme işlemi tamamlandı.".format(
                    kullanici=kullanici))
                self.profilSec(secim)
            else:
                if durum:
                    print(self.uyariOlustur(
                        "[-] {kullanici} adlı kişinin hesabı gizli hesap olduğundan gönderileri beğenme işlemi yapılamıyor!".format(
                            kullanici=kullanici), 2))
                else:
                    print(self.uyariOlustur(
                        "[-] {kullanici} adlı kişinin hesabı gizli hesap olduğundan gönderileri beğenmekten vazgeçme işlemi yapılamıyor!".format(
                            kullanici=kullanici), 2))
                self.profilSec(secim)
        except Exception as error:
            if durum:
                print(self.uyariOlustur(
                    "[-] {kullanici} kullanıcısının gönderilerini beğenme işlemi sırasında bir hata oluştu:{hata}".format(
                        kullanici=kullanici, hata=error), 2))
            else:
                print(self.uyariOlustur(
                    "[-] {kullanici} kullanıcısının gönderilerini beğenmekten vazgeçme işlemi sırasında bir hata oluştu:{hata}".format(
                        kullanici=kullanici, hata=error), 2))
            self.profilSec(secim)

    def gonderiBegen(self, durum=True):
        try:
            if durum:
                url = input("Beğenmek istediğiniz gönderi url >> ").strip()
            else:
                url = input("Beğenmekten vazgeçmek istediğiniz gönderi url >> ").strip()

            self.anaMenuyeDonsunMu(url)
            if not url:
                print(self.uyariOlustur("[-] Gönderi url'si girmediniz!!", 2))
                self.gonderiBegen(durum)

            if self.urlKontrol(url):
                print("[*] {url}  gönderisine yönlendiriliyor...".format(url=url))
                self.urlYonlendir(url)
                if not self.hesapGizliMi():
                    if durum:
                        print("[*] {url} adresindeki gönderinin beğenme işlemi başladı...".format(url=url))
                    else:
                        print("[*] {url} adresindeki gönderinin beğenmekten vazgeçme işlemi başladı...".format(url=url))
                    btn_begen = self.driver.find_element_by_xpath(
                        "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                    begeniDurum = self.begenButonuDurumGetir(btn_begen)
                    if durum:
                        if begeniDurum == "like":
                            btn_begen.click()
                            print(
                                self.uyariOlustur("[+] {url} gönderisi beğenildi.".format(url=self.driver.current_url),
                                                  1))
                        else:
                            print(self.uyariOlustur(
                                "[*] {url} gönderisi daha önce beğenildi.".format(url=self.driver.current_url), 1))
                    else:
                        if begeniDurum == "unlike":
                            btn_begen.click()
                            print(self.uyariOlustur(
                                "[+] {url} gönderisi beğenilmekten vazgeçildi.".format(url=self.driver.current_url), 1))
                        else:
                            print(self.uyariOlustur(
                                "[*] {url} gönderisi zaten beğenilmedi.".format(url=self.driver.current_url), 1))
                    if durum:
                        print("[*] {url} adresindeki gönderinin beğenme işlemi tamamlandı.".format(url=url))
                    else:
                        print(
                            "[*] {url} adresindeki gönderinin beğenmekten vazgeçme işlemi tamamlandı.".format(url=url))
                else:
                    if durum:
                        print(self.uyariOlustur(
                            "[-] {url} gönderisinin sahibinin profili gizli hesap olduğundan beğeni işlemi yapılamıyor!".format(
                                url=url), 2))
                    else:
                        print(self.uyariOlustur(
                            "[-] {url} gönderisinin sahibinin profili gizli hesap olduğundan beğenmektez vazgeçme işlemi yapılamıyor!".format(
                                url=url), 2))
            self.gonderiBegen(durum)
        except Exception as error:
            if durum:
                print(
                    self.uyariOlustur("[-] gönderi beğenme işlemi sırasında bir hata oluştu:{hata}".format(hata=error),
                                      2))
            else:
                print(self.uyariOlustur(
                    "[-] gönderi beğenmekten vazgeçme işlemi sırasında bir hata oluştu:{hata}".format(hata=error), 2))
            self.gonderiBegen(durum)

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
            self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div").click()
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
            self.driver.quit()
            exit()

try:
    instagram = Instagram()
except KeyboardInterrupt:
    print("\n [*] Python uygulamasından çıkış yapılıyor...")
    exit()


