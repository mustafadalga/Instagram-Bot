from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime
import os
import urllib.request
import requests
import getpass
from termcolor import colored
from colorama import init
import threading
from random import randint
import json

class Instagram():
    def __init__(self):
        init(convert=True)
        self.config=None
        self.dil = None
        self.ayarlarYukle()
        self.dilYukle()
        self.ayarlar()
        self.script()
        self.tarayiciThreadOlustur()
        self.girisYapildimi = False
        self.tarayiciAcildimi = False
        self.aktifKullanici = ""
        self.index = 1
        self.BASE_URL = "https://www.instagram.com/"
        self.girisYap()

    def BASE_AYARLAR(self):
        try:
            return "languages.{dil}.ayarlar.".format(dil=self.dil)
        except Exception as error:
            self.uyariOlustur(error,2)

    def ayarlar(self,durum=True):
        if durum:
            ayarlar=self.configGetir(self.BASE_AYARLAR()+"ana_ekran.secenekler")
            for secenek in ayarlar:
                self.uyariOlustur(secenek,3)
        secilenIslem=input("Yapmak istediğiniz işlemin başındaki sayısı giriniz >> ")

        if secilenIslem=="1":
            self.dilAyarlari()
        elif secilenIslem=="2":
            self.tarayiciAyarlari()
        elif secilenIslem=="3":
            self.menu()
        else:
            self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!", 2)
            self.ayarlar(durum=False)


    def dilAyarlari(self,durum=True):
        if durum:
            ayarlar=self.configGetir(self.BASE_AYARLAR()+"dil_ayarlari.secenekler")
            for secenek in ayarlar:
                self.uyariOlustur(secenek,3)
        secilenIslem=input("Yapmak istediğiniz işlemin başındaki sayısı giriniz >>")

        if secilenIslem=="1":
            self.dilSec()
        elif secilenIslem=="2":
            self.ayarlar()
        elif secilenIslem=="3":
            self.menu()
        else:
            self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!",2)
            self.dilAyarlari(durum=False)

    def dilSec(self,durum=True):
        if durum:
            ayarlar=self.configGetir(self.BASE_AYARLAR()+"dil_ayarlari.dil_degistir.secenekler")
            for secenek in ayarlar:
                self.uyariOlustur(secenek,3)
        secilenIslem=input("Yapmak istediğiniz işlemin başındaki sayısı giriniz >>")

        if secilenIslem in ["1","2"]:
            self.uygulamaDilDegistir(dilNo=secilenIslem)
            self.ayarlar()
        elif secilenIslem=="3":
            self.dilAyarlari()
        elif secilenIslem=="4":
            self.ayarlar()
        elif secilenIslem=="5":
            self.menu()
        else:
            self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!",2)
            self.dilSec(durum=False)

    def uygulamaDilDegistir(self,dilNo):
        try:
            if dilNo=="1":
                dil="tr"
            elif dilNo=="2":
                dil="en"
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                veri = json.load(dosya)
                veri["language"]=dil
                dosya.seek(0)
                json.dump(veri, dosya, indent=4,ensure_ascii=False)
                dosya.truncate()
            self.uyariOlustur("[*] Uygulama dili başarıyla değiştirildi.Değişikliği görmek için uygulamayı yeniden başlatın",1)
        except Exception as error:
            self.uyariOlustur("[-] Uygulama dili değiştirme işlemi sırasında bir hata oluştu:{hata}".format(hata=str(error)), 2)

    def tarayiciAyarlari(self,durum=True):
        if durum:
            ayarlar=self.configGetir(self.BASE_AYARLAR()+"tarayici_ayarlari.secenekler")
            for secenek in ayarlar:
                self.uyariOlustur(secenek,3)
        secilenIslem=input("Yapmak istediğiniz işlemin başındaki sayısı giriniz >>")

        if secilenIslem=="1":
            self.tarayiciGorunmeDurumuAyarlari()
        elif secilenIslem=="2":
            self.tarayiciPathAyarlari()
        elif secilenIslem=="3":
            self.ayarlar()
        elif secilenIslem=="4":
            self.menu()
        else:
            self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!",2)
            self.tarayiciAyarlari(durum=False)

    def tarayiciPathAyarlari(self,durum=True):
        if durum:
            ayarlar=self.configGetir(self.BASE_AYARLAR()+"tarayici_ayarlari.path_degistir.secenekler")
            for secenek in ayarlar:
                self.uyariOlustur(secenek,3)

        secilenIslem = input("Yapmak istediğiniz işlemin başındaki sayısı giriniz >>")
        if secilenIslem=="1":
            self.tarayiciPathDegistir()
            self.ayarlar()
        elif secilenIslem=="2":
            self.tarayiciAyarlari()
        elif secilenIslem=="3":
            self.ayarlar()
        elif secilenIslem=="4":
            self.menu()
        else:
            self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!",2)
            self.tarayiciPathAyarlari(durum=False)


    def tarayiciPathDegistir(self):
        try:
            path = input("Tarayıcı sürü yolunu giriniz >>")
            if self.dosyaMevcutMu(path):
                with open('config.json', 'r+', encoding="utf-8") as dosya:
                    veri = json.load(dosya)
                    veri["driver_path"]=path
                    dosya.seek(0)
                    json.dump(veri, dosya, indent=4,ensure_ascii=False)
                    dosya.truncate()
                self.uyariOlustur("[*] Tarayıcı sürücü yolu başarıyla değiştirildi.Değişikliği görmek için uygulamayı yeniden başlatın.",1)
            else:
                self.uyariOlustur("[-] Belirttiğiniz dosya mevcut değil!", 2)
                self.tarayiciPathAyarlari()
        except Exception as error:
            self.uyariOlustur("[-] Tarayıcı sürücü yolu  değiştirme işlemi sırasında bir hata oluştu:{hata}".format(hata=str(error)), 2)


    def tarayiciGorunmeDurumuAyarlari(self,durum=True):
        if durum:
            ayarlar=self.configGetir(self.BASE_AYARLAR()+"tarayici_ayarlari.gorunme_durumu_degistir.secenekler")
            for secenek in ayarlar:
                self.uyariOlustur(secenek,3)
        secilenIslem=input("Yapmak istediğiniz işlemin başındaki sayısı giriniz >>")
        if secilenIslem in ["1","2"]:
            self.tarayiciGorunmeDurumDegistir(durum=secilenIslem)
            self.ayarlar()
        elif secilenIslem=="3":
            self.tarayiciAyarlari()
        elif secilenIslem=="4":
            self.ayarlar()
        elif secilenIslem=="5":
            self.menu()
        else:
            self.uyariOlustur("[-] Geçerli bir seçim yapmadınız.Lütfen geçerli bir seçim yapınız!",2)
            self.tarayiciGorunmeDurumuAyarlari(durum=False)

    def tarayiciGorunmeDurumDegistir(self,durum):
        try:
            if durum=="1":
                headless="true"
            elif durum=="2":
                headless="false"
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                veri = json.load(dosya)
                veri["headless"]=headless
                dosya.seek(0)
                json.dump(veri, dosya, indent=4,ensure_ascii=False)
                dosya.truncate()
            self.uyariOlustur("[*] Tarayıcı görünme durumu başarıyla değiştirildi.Değişikliği görmek için uygulamayı yeniden başlatın.",1)
        except Exception as error:
            self.uyariOlustur("[-] Tarayıcı görünme durumu değiştirme işlemi sırasında bir hata oluştu:{hata}".format(hata=str(error)), 2)


    def ayarlarYukle(self):
        if self.dosyaMevcutMu("config.json"):
            with open('config.json', 'r+', encoding="utf-8") as dosya:
                self.config = json.load(dosya)
        else:
            self.uyariOlustur("Config file is missing - Config dosyası eksik !",2)
            exit()

    def configGetir(self,anahtar):
        deger=self.config
        for key in anahtar.split('.'):
            deger = deger[key]
        return deger

    def dilYukle(self):
        self.dil=self.configGetir("language")

    def script(self):
        print("")
        self.uyariOlustur("  _____           _                                    ____        _   ", 1)
        self.uyariOlustur(" |_   _|         | |                                  |  _ \      | |  ", 1)
        self.uyariOlustur("   | |  _ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___   | |_) | ___ | |_ ", 1)
        self.uyariOlustur("   | | | '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \  |  _ < / _ \| __|", 1)
        self.uyariOlustur("  _| |_| | | \__ \ || (_| | (_| | | | (_| c | | | | | | |_) | (_) | |_ ", 1)
        self.uyariOlustur(" |_____|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_| |____/ \___/ \__|", 1)
        self.uyariOlustur("                            __/ |                                      ", 1)
        self.uyariOlustur("                           |___/                                       ", 1)
        self.uyariOlustur("# ==============================================================================", 1)
        self.uyariOlustur("# author       :Mustafa Dalga", 1)
        self.uyariOlustur("# linkedin     :https://www.linkedin.com/in/mustafadalga", 1)
        self.uyariOlustur("# github       :https://github.com/mustafadalga", 1)
        self.uyariOlustur("# email        :mustafadalgaa < at > gmail[.]com", 1)
        self.uyariOlustur("# date         :15.07.2019", 1)
        self.uyariOlustur("# version      :2.0", 1)
        self.uyariOlustur("# python_version:3.8.1", 1)
        self.uyariOlustur("# ==============================================================================", 1)
        print("")

    def menu(self):
        menu = self.configGetir("languages.{dil}.menu".format(dil=self.dil))
        for secenek in menu:
            self.uyariOlustur(secenek, 3)
        self.islemSec()

    def islemSec(self):
        base_warnings=self.BASE_UYARI(metod=self.islemSec,warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.islemSec, inputs=True)
        secim = input(self.configGetir(base_inputs+"input1")).strip()
        if secim:
            try:
                secim = int(secim)
                if 0 < secim < 27:
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
                    elif secim == 15:
                        self.etiketeGoreTakipEtme()
                    elif secim==16:
                        self.etiketeGoreBegenme()
                    elif secim==17:
                        self.gonderiBegen()
                    elif secim==18:
                        self.gonderiBegen(False)
                    elif secim==19:
                        self.gonderiYorumYapma()
                    elif secim==24:
                        self.ayarlar()
                    elif secim==25:
                        self.oturumKapat()
                    elif secim==26:
                        self.quit()
                else:
                    self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                    self.islemSec()
            except Exception:
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.islemSec()
        else:
            self.islemSec()

    def secilenIslemiGoster(self, secim):
        base_warnings = self.BASE_UYARI(metod=self.secilenIslemiGoster, warnings=True)
        secimler = self.configGetir("languages.{dil}.warnings.secilenIslemiGoster.secimler".format(dil=self.dil))
        print("")
        self.uyariOlustur(secimler.get(str(secim), self.configGetir(base_warnings+"warning1")), 1)
        if secim < 24:
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 3)
        print("")

    def anaMenuyeDonsunMu(self,deger):
        if deger == "menu":
            self.menu()

    def profilSec(self, secim):
        base_warnings=self.BASE_UYARI(metod=self.profilSec,warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.profilSec, inputs=True)

        kullanici = input(self.configGetir(base_inputs+"input1")).strip()

        if not kullanici:
            self.profilSec(secim)

        self.anaMenuyeDonsunMu(kullanici)

        if self.kullaniciKontrol(kullanici):
            print(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici))
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
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici), 2)
            self.profilSec(secim)

    def kullaniciProfilineYonlendir(self,kullanici):
        self.driver.get(self.BASE_URL + kullanici)
        sleep(5)

    def urlYonlendir(self,url):
        self.driver.get(url)
        sleep(5)

    def urlKontrol(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 404:
                return False
            else:
                return True
        except:
            return False

    def urlGirildiMi(self,url,metod):
        base_warnings = self.BASE_UYARI(metod=self.urlGirildiMi, warnings=True)
        if not url or len(url)<12:
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
            metod

    def urlGecerliMi(self,url,metod):
        if not self.urlKontrol(url):
            base_warnings = self.BASE_UYARI(metod=self.urlGecerliMi, warnings=True)
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
            metod

    def tarayiciThreadOlustur(self):
        t1 = threading.Thread(target=self.tarayiciBaslat)
        t1.daemon = True
        t1.start()

    def BASE_UYARI(self,metod,warnings=None,inputs=None):
        try:
            if warnings:
                return "languages.{dil}.warnings.{metod}.warnings.".format(dil=self.dil,metod=metod.__name__)
            elif inputs:
                return "languages.{dil}.warnings.{metod}.inputs.".format(dil=self.dil, metod=metod.__name__)
            else:
                return "languages.{dil}.warnings.{metod}.".format(dil=self.dil, metod=metod.__name__)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.BASE_UYARI, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)))


    def tarayiciBaslat(self):
        base_warnings=self.BASE_UYARI(metod=self.tarayiciBaslat,warnings=True)

        self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 1)
        self.driver = webdriver.Firefox(firefox_profile=self.tarayiciDilDegistir(),
                                        executable_path="E:\\Python\\Uygulamalar\\Intagram-Bot\\Instagram-Bot\\geckodriver.exe")
        self.driver.get(self.BASE_URL + 'accounts/login/')

    def mesajSil(self,mesaj):
        mesaj.click()
        sleep(self.beklemeSuresiBelirle(1, 2))
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[1]/div/div/div[3]/button").click()
        sleep(1)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/div[2]/div[3]/div[1]/button").click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button[1]").click()

    def topluMesajSilme(self):
        base_warnings = self.BASE_UYARI(metod=self.topluMesajSilme, warnings=True)
        try:

            print(self.configGetir(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir('direct/inbox/')
            devamEtsinMi = True
            silinenMesajlar = set()
            self.indexSifirla()
            while devamEtsinMi:
                mesajListesi = self.driver.find_elements_by_css_selector("div.N9abW  a.rOtsg")
                if len(mesajListesi) == 0:
                    print(self.configGetir(base_warnings+"warning2"))
                    break
                for mesaj in mesajListesi:
                    if mesaj not in silinenMesajlar:
                        silinenMesajlar.add(mesaj)
                        kullaniciAdi = mesaj.find_element_by_css_selector("._7UhW9.xLCgt.MMzan.KV-D4.fDxYl").text
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(index=self.index,kullaniciAdi=kullaniciAdi),1)
                        self.mesajSil(mesaj)
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(index=self.index, kullaniciAdi=kullaniciAdi), 1)
                        self.indexArtir()
                        sleep(self.beklemeSuresiBelirle(5,15))
                    break

            print(self.configGetir(base_warnings+"warning5"))
            self.menu()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(hata=str(error)),2)
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
            base_warnings = self.BASE_UYARI(metod=self.yorumYap, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)

    def rastgeleYorumGetir(self):
        try:
            return requests.get("http://metaphorpsum.com/paragraphs/1/1").text
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.rastgeleYorumGetir, warnings=True)
            self.uyariOlustur(
                str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)

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
            base_warnings = self.BASE_UYARI(metod=self.dosyaİceriginiAl, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            return False

    def dosyaİcerigiAlindiMi(self, icerik):
        if icerik:
            return True
        else:
            return False

    def topluYorumYapma(self, url=None, yorumSayisi=None, secilenIslem=None):
        base_warnings = self.BASE_UYARI(metod=self.topluYorumYapma, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.topluYorumYapma, inputs=True)
        try:
            if not url:
                url = input(self.configGetir(base_inputs+"input1")).strip()
                self.anaMenuyeDonsunMu(url)


                self.urlGecerliMi(url,self.topluYorumYapma())


                print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
                self.urlYonlendir(url)

                if not self.sayfaMevcutMu():
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(url=url), 2)
                    self.topluYorumYapma()

                if self.hesapGizliMi():
                    self.uyariOlustur(
                        str(self.configGetir(base_warnings+"warning3")).format(
                            url=url), 2)
                    self.topluYorumYapma()

            if not yorumSayisi:
                yorumSayisi = input(self.configGetir(base_inputs+"input2")).strip()
                self.anaMenuyeDonsunMu(yorumSayisi)
                if yorumSayisi.isnumeric() and int(yorumSayisi) > 0:
                    yorumSayisi = int(yorumSayisi)
                    if self.yorumLimitiAsildiMi(yorumSayisi):
                        yorumSayisi = 50
                        self.uyariOlustur(
                            self.configGetir(base_warnings+"warning4"), 2)
                else:
                    self.uyariOlustur(self.configGetir(base_warnings+"warning5"), 2)
                    self.topluYorumYapma(url=url, yorumSayisi=None, secilenIslem=None)

            if not secilenIslem:
                for uyari in self.configGetir(base_warnings + "warning6"):
                    self.uyariOlustur(uyari, 1)
                secilenIslem = str(input(self.configGetir(base_inputs+"input3")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                self.uyariOlustur(self.configGetir(base_warnings+"warning7"), 1)
                print(str(self.configGetir(base_warnings+"warning8")).format(url=url))
                for i in range(yorumSayisi):
                    yorum = self.rastgeleYorumGetir()
                    yorum = self.yorumUzunlukBelirle(yorum)
                    self.yorumYap(yorum)
                    print(str(self.configGetir(base_warnings+"warning9")).format(index=i + 1))
                    sleep(self.beklemeSuresiBelirle(5, 20))
            elif secilenIslem == "2":
                self.uyariOlustur(self.configGetir(base_warnings+"warning10"), 1)
                dosya = self.dosyaSec(1)
                yorumlar = self.dosyaİceriginiAl(dosya)
                if self.dosyaİcerigiAlindiMi(yorumlar):
                    print(str(self.configGetir(base_warnings+"warning11")).format(url=url))
                    for index, yorum in enumerate(yorumlar):
                        yorum = self.yorumUzunlukBelirle(yorum)
                        self.yorumYap(yorum)
                        print(str(self.configGetir(base_warnings+"warning12")).format(index=index + 1))
                        if (index + 1) == yorumSayisi:
                            break
                        sleep(self.beklemeSuresiBelirle(5,20))
                else:
                    self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=secilenIslem)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning13"),2)
                print("")
                self.topluYorumYapma(url=url, yorumSayisi=yorumSayisi, secilenIslem=None)

            print(str(self.configGetir(base_warnings+"warning14")).format(url=url))
            self.topluYorumYapma()
        except Exception as error:
            self.uyariOlustur(
                str(self.configGetir(base_warnings+"warning15")).format(url=url,hata=str(error)),
                2)
            self.topluYorumYapma()


    def gonderiYorumYapma(self, url=None, yorum=None):
        base_warnings = self.BASE_UYARI(metod=self.gonderiYorumYapma, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiYorumYapma, inputs=True)
        try:

            if not url:
                url = input(self.configGetir(base_inputs+"input1")).strip()
                self.anaMenuyeDonsunMu(url)
            if not yorum:
                yorum = input(self.configGetir(base_inputs+"input2")).strip()
                self.anaMenuyeDonsunMu(yorum)


            self.urlGecerliMi(url,self.gonderiYorumYapma(url=None,yorum=yorum))


            if not self.degerVarMi(yorum):
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                self.gonderiYorumYapma(url=url, yorum=None)

            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)

            if not self.sayfaMevcutMu():
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                self.gonderiYorumYapma()

            if not self.hesapGizliMi():
                yorum = self.yorumUzunlukBelirle(yorum)
                print(str(self.configGetir(base_warnings+"warning4")).format(url=url))
                self.yorumYap(yorum)
                print(str(self.configGetir(base_warnings+"warning5")).format(url=url))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(url=url), 2)
            self.gonderiYorumYapma()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(url=url,hata=str(error)),
                              2)
            self.gonderiYorumYapma()

    def gonderiIlerlet(self):
        try:
            self.driver.find_element_by_css_selector("a._65Bje").click()
        except:
            pass

    def etiketGetir(self):
        base_warnings = self.BASE_UYARI(metod=self.etiketGetir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.etiketGetir, inputs=True)
        try:
            etiket = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(etiket)

            if self.degerVarMi(etiket):
                url = "{BASE_URL}explore/tags/{etiket}".format(BASE_URL=self.BASE_URL, etiket=str(etiket))
                print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
                self.urlYonlendir(url)
                if not self.sayfaMevcutMu():
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(etiket=etiket),
                                      2)
                    return self.etiketGetir()
                return etiket
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                return self.etiketGetir()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(hata=str(error)), 2)

    def etiketeGoreIslemLimitiGetir(self, islemNo):
        base_warnings = self.BASE_UYARI(metod=self.etiketeGoreIslemLimitiGetir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.etiketeGoreIslemLimitiGetir, inputs=True)
        try:

            if islemNo == 1:
                limit = input(self.configGetir(base_inputs+"input1")).strip()
            elif islemNo == 2:
                limit = input(self.configGetir(base_inputs+"input2")).strip()

            self.anaMenuyeDonsunMu(limit)
            if limit.isnumeric() and int(limit) > 0:
                return int(limit)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                return self.etiketeGoreIslemLimitiGetir(islemNo=islemNo)
        except Exception as error:
            self.uyariOlustur(
                str(self.configGetir(base_warnings+"warning2")).format(
                    hata=str(error)), 2)
            if islemNo == 1:
                self.etiketeGoreBegenme()
            elif islemNo == 2:
                self.etiketeGoreTakipEtme()


    def etiketeGoreTakipEtme(self):
        base_warnings = self.BASE_UYARI(metod=self.etiketeGoreTakipEtme, warnings=True)
        try:
            etiket = self.etiketGetir()

            limit = self.etiketeGoreIslemLimitiGetir(2)

            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            ilkGonderi = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")
            ilkGonderi.click()
            sleep(1)
            self.indexSifirla()

            print(str(self.configGetir(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                kullanici = self.driver.find_element_by_xpath(
                    "/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]")
                kullaniciAdi = kullanici.find_element_by_css_selector("a.sqdOP").text
                btn_takip = kullanici.find_element_by_css_selector("button.oW_lN")
                if btn_takip.text != "Following":
                    btn_takip.click()
                    self.uyariOlustur(
                        str(self.configGetir(base_warnings+"warning2")).format(index=self.index,
                                                                               kullanici=kullaniciAdi), 1)
                    self.indexArtir()
                    if self.index-1 >= limit:
                        break
                    sleep(0.50)
                    self.gonderiIlerlet()
                    sleep(self.beklemeSuresiBelirle(5,20))
                else:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(kullanici=kullaniciAdi), 1)
                    self.gonderiIlerlet()
                    sleep(5)
            print(str(self.configGetir(base_warnings+"warning4")).format(etiket=etiket))
            self.etiketeGoreTakipEtme()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.etiketeGoreTakipEtme()

    def begenButonuGetir(self):
        return self.driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")

    def begenButonuDurumGetir(self, buton):
        return str(buton.find_element_by_tag_name("svg").get_attribute("aria-label")).lower()

    def etiketeGoreBegenme(self):
        base_warnings = self.BASE_UYARI(metod=self.etiketeGoreBegenme, warnings=True)
        try:
            etiket = self.etiketGetir()
            limit = self.etiketeGoreIslemLimitiGetir(1)
            kaynakGonderiSayisi = int(
                self.metindenKarakterSil(self.driver.find_element_by_css_selector("span.g47SY").text, ','))
            limit = self.hedefKaynaktanBuyukMu(limit, kaynakGonderiSayisi)
            ilkGonderi = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]")
            ilkGonderi.click()
            sleep(1)
            self.indexSifirla()

            print(str(self.configGetir(base_warnings+"warning1")).format(etiket=etiket))
            while True:
                btn_begen = self.begenButonuGetir()
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if begeniDurum != "unlike":
                    btn_begen.click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(index=self.index,url=self.driver.current_url),1)
                    self.indexArtir()
                    if self.index-1 >= limit:
                        break
                    sleep(0.50)
                    self.gonderiIlerlet()
                    sleep(self.beklemeSuresiBelirle(5,15))
                else:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(url=self.driver.current_url), 1)
                    self.gonderiIlerlet()
                    sleep(5)
            print(str(self.configGetir(base_warnings+"warning4")).format(etiket=etiket))
            self.etiketeGoreBegenme()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.etiketeGoreBegenme()

    def hikayeVarMi(self):

        try:
            durum = self.driver.find_element_by_css_selector("div.RR-M-").get_attribute("aria-disabled")
            if durum == "false":
                return True
            else:
                return False
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.hikayeVarMi, warnings=True)
            self.uyariOlustur(
                str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)),
                2)

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
            base_warnings = self.BASE_UYARI(metod=self.hikayeSayisiGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)

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
                sleep(1)
        except Exception as error:
            base_warnings = self.BASE_UYARI(metod=self.hikayeleriGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)

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
        base_warnings = self.BASE_UYARI(metod=self.hikayeIndir, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                if self.hikayeVarMi():
                    self.driver.find_element_by_css_selector("div.RR-M-").click()
                    sleep(3)
                    print(str(self.configGetir(base_warnings+"warning1")).format(
                        kullanici=kullanici))
                    self.klasorOlustur(kullanici)
                    self.indexSifirla()
                    self.hikayeleriGetir()
                    self.klasorDegistir("../")
                    print(str(self.configGetir(base_warnings+"warning2")).format(
                        kullanici=kullanici))
                else:
                    self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                    kullanici=kullanici), 2)
            self.profilSec(secim)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.profilSec(secim)



    def indexSifirla(self):
        self.index = 1

    def indexArtir(self):
        self.index = self.index + 1

    def oneCikanHikayeIndir(self):
        base_warnings = self.BASE_UYARI(metod=self.oneCikanHikayeIndir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.oneCikanHikayeIndir, inputs=True)
        try:
            url = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url,self.oneCikanHikayeIndir())
            self.urlGecerliMi(url,self.oneCikanHikayeIndir())

            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)

            if not self.sayfaMevcutMu():
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.oneCikanHikayeIndir()

            print(str(self.configGetir(base_warnings+"warning3")).format(url=url))
            btn_oynat = self.driver.find_element_by_css_selector("button._42FBe")
            btn_oynat.click()
            sleep(1)
            kullanici = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/div/div/section/header/div/div[1]/div/div/div/a").get_attribute("title")
            self.klasorOlustur(kullanici)
            self.indexSifirla()
            self.hikayeleriGetir()
            self.klasorDegistir("../")
            print(str(self.configGetir(base_warnings+"warning4")).format(url=url))
            self.oneCikanHikayeIndir()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.oneCikanHikayeIndir()

    def dosyaAdiOlustur(self,veriTuru):
        dt=str(datetime.now()).replace(":", "_").replace(" ", "")
        if veriTuru == 1:
            isim="{index}_{tarih}.jpg".format(index=str(self.index),tarih=dt)
        elif veriTuru == 2:
            isim = "{index}_{tarih}.mp4".format(index=str(self.index), tarih=dt)
        return isim

    def dosyaIndir(self, url, veriTuru):
        base_warnings = self.BASE_UYARI(metod=self.dosyaIndir, warnings=True)
        try:
            dosyaAdi=self.dosyaAdiOlustur(veriTuru)
            urllib.request.urlretrieve(url, dosyaAdi)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(url=url), 1)
            self.indexArtir()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)

    def topluTakiptenCik(self):
        base_warnings = self.BASE_UYARI(metod=self.topluTakiptenCik, warnings=True)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            takipEdilenSayisi = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/span").text
            takipEdilenSayisi = int(self.metindenKarakterSil(takipEdilenSayisi, ','))

            btn_takipEdilenler = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            btn_takipEdilenler.click()
            sleep(3)
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
                        sleep(2)
                        try:
                            btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                            btn_onay.click()
                        except Exception as error:
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(
                                kullaniciAdi=takipEdilenKullanıcıAdi, hata=str(error)), 2)
                            continue
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                            index=self.index, kullaniciAdi=takipEdilenKullanıcıAdi), 1)
                        self.indexArtir()
                        if (self.index - 1) >= takipEdilenSayisi:
                            devamEtsinMi = False
                            break
                        sleep(self.beklemeSuresiGetir(5, 15))
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(3)
            self.menu()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
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
        base_warnings = self.BASE_UYARI(metod=self.takipEdilenleriGetir, warnings=True)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            takipEdilenSayisi = self.takipEdilenSayisiGetir()

            btn_takipEdilenler = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            btn_takipEdilenler.click()
            sleep(5)
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
                            sleep(2)
                            try:
                                btn_onay = self.driver.find_element_by_css_selector("div.mt3GC > button.aOOlW")
                                btn_onay.click()
                            except Exception as error:
                                self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(
                                    kullaniciAdi=takipEdilenKullanıcıAdi, hata=str(error)), 2)
                                continue
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                                index=self.index, kullaniciAdi=takipEdilenKullanıcıAdi), 1)
                            self.indexArtir()
                            if self.index - 1 >= takipEdilenSayisi:
                                devamEtsinMi = False
                                break
                            sleep(self.beklemeSuresiBelirle(5, 15))
                    islemIndex = islemIndex + 1
                    if islemIndex >= takipEdilenSayisi:
                        devamEtsinMi = False
                        break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(3)

        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(
                hata=str(error)), 2)
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
        base_warnings = self.BASE_UYARI(metod=self.takipcileriGetir, warnings=True)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            self.kullaniciProfilineYonlendir(self.aktifKullanici)
            print(self.configGetir(base_warnings+"warning2"))
            takipciSayisi = self.takipciSayisiGetir()

            btn_takipciler = self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            btn_takipciler.click()
            sleep(3)
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
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(index=self.index,
                                                                                                 takipci=takipciKullaniciAdi),
                                          1)
                        takipciler.add(takipciKullaniciAdi)
                        self.indexArtir()
                        if (self.index - 1) >= takipciSayisi:
                            devamEtsinMi = False
                            break
                if devamEtsinMi:
                    try:
                        self.popupAsagiKaydir(secici='div[role="dialog"] .isgrP')
                    except Exception as error:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                            hata=str(error)), 2)
                        pass
                    sleep(3)
            btn_close_dialog = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[1]/div/div[2]/button")
            btn_close_dialog.click()
            return takipciler
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=str(error)), 2)
            self.menu()

    def takipEtmeyenleriTakiptenCik(self):
        base_warnings = self.BASE_UYARI(metod=self.takipEtmeyenleriTakiptenCik, warnings=True)
        try:
            takipciler = self.takipcileriGetir()
            print(self.configGetir(base_warnings+"warning1"))
            self.takipEdilenleriGetir(takipciler=takipciler)
            print(self.configGetir(base_warnings+"warning2"))
            self.menu()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                hata=str(error)), 2)
            self.menu()

    def metindenKarakterSil(self, metin, silinecekKarakterler):
        return metin.replace(silinecekKarakterler, '')

    def gonderiBegenenleriTakipEt(self, secilenIslem=None):
        base_warnings = self.BASE_UYARI(metod=self.gonderiBegenenleriTakipEt, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiBegenenleriTakipEt, inputs=True)
        try:
            url = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(url)

            self.urlGirildiMi(url,self.gonderiBegenenleriTakipEt())
            self.urlGecerliMi(url,self.gonderiBegenenleriTakipEt())

            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)
            hedefBegenenSayisi = None

            if secilenIslem is None:
                for uyari in self.configGetir(base_warnings + "warning2"):
                    self.uyariOlustur(uyari,1)
                secilenIslem = str(input(self.configGetir(base_inputs+"input2")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 1)
            elif secilenIslem == "2":
                self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 1)
                hedefBegenenSayisi = input(self.configGetir(base_inputs+"input3")).strip()
                self.anaMenuyeDonsunMu(hedefBegenenSayisi)
                if hedefBegenenSayisi.isnumeric():
                    hedefBegenenSayisi = int(hedefBegenenSayisi)
                else:
                    self.uyariOlustur(self.configGetir(base_warnings+"warning5"), 2)
                    print("")
                    self.gonderiBegenenleriTakipEt( secilenIslem=secilenIslem)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning6"), 2)
                print("")
                self.gonderiBegenenleriTakipEt(secilenIslem=None)

            if not self.hesapGizliMi():
                if not self.gonderiTipiVideoMu():
                    print(str(self.configGetir(base_warnings+"warning7")).format(url=url))
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
                    sleep(5)

                    while devamEtsinMi:
                        dialog_popup = self.driver.find_element_by_css_selector("div.pbNvD")
                        begenenlerKullanicilar = dialog_popup.find_elements_by_css_selector('div.HVWg4')
                        for begenenKullanici in begenenlerKullanicilar:
                            begenenKullaniciAdi = begenenKullanici.find_element_by_css_selector(
                                "div.Igw0E > div.Igw0E > div._7UhW9  a").get_attribute('href')
                            begenenKullaniciAdi = begenenKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                            btn_takip = begenenKullanici.find_element_by_css_selector("div.Igw0E > button.sqdOP")
                            if btn_takip.text == "Follow":
                                self.uyariOlustur(str(self.configGetir(base_warnings+"warning8")).format(
                                    index=takipIstekSayisi + 1, kullaniciAdi=begenenKullaniciAdi), 1)
                                btn_takip.click()
                                takipIstekSayisi = takipIstekSayisi + 1
                                if takipIstekSayisi == begenenSayisi:
                                    devamEtsinMi = False
                                    break
                                sleep(self.beklemeSuresiGetir(5, 15))

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
                            sleep(3)
                        else:
                            print(self.configGetir(base_warnings+"warning9"))
                else:
                    print(str(self.configGetir(base_warnings+"warning10")).format(
                        url=url))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning11")).format(url=url),
                                  2)
            self.gonderiBegenenleriTakipEt()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning12")).format(hata=str(error)), 2)
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
            if self.kullaniciKontrol(kullanici):
                self.kullaniciTakipEt(kullanici.strip(), secim)
                sleep(self.beklemeSuresiGetir(10,45))

    def dosyaSec(self):
        base_warnings = self.BASE_UYARI(metod=self.dosyaSec, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.dosyaSec, inputs=True)
        try:
            dosyaAdi = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(dosyaAdi)
            if self.dosyaMevcutMu(dosyaAdi) and self.txtDosyasiMi(dosyaAdi):
                return str(dosyaAdi)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
                return self.dosyaSec()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(hata=str(error)), 2)
            return self.dosyaSec()

    def dosyaMevcutMu(self, path):
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
                sleep(5)
                btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
                self.driver.execute_script("arguments[0].click();", btn)
        except:
            pass

    def tarayiciDilDegistir(self):
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
            base_warnings = self.BASE_UYARI(metod=self.aktifKullaniciGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            self.aktifKullaniciGetir()

    def girisYap(self, username=False, password=False):
        base_warnings = self.BASE_UYARI(metod=self.girisYap, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.girisYap, inputs=True)
        try:
            if not username and not password:
                print(" ")
                print(" ")
                self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 1)
                username = input(self.configGetir(base_inputs+"input1"))
                password = getpass.getpass(prompt=self.configGetir(base_inputs+"input2"))
            elif not username:
                username = input(self.configGetir(base_inputs+"input1"))
            elif not password:
                password = getpass.getpass(prompt=self.configGetir(base_inputs+"input2"))

            if not username and not password:
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
                self.girisYap()
            elif not username:
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 2)
                self.girisYap(False, password)
            elif not password:
                self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 2)
                self.girisYap(username, False)

            self.uyariOlustur(self.configGetir(base_warnings+"warning5"), 1)
            sleep(15)
            usernameInput = self.driver.find_elements_by_css_selector('form input')[0]
            passwordInput = self.driver.find_elements_by_css_selector('form input')[1]
            usernameInput.send_keys(username.strip())
            passwordInput.send_keys(password.strip())
            passwordInput.send_keys(Keys.ENTER)
            sleep(5)
            self.girisKontrol()
            if self.girisYapildimi:
                self.aktifKullaniciGetir()
                self.bildirimThreadOlustur()
                self.menu()
            else:
                self.inputTemizle(usernameInput)
                self.inputTemizle(passwordInput)
                self.girisYap()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(hata=str(error)), 2)

    def girisKontrol(self):
        base_warnings = self.BASE_UYARI(metod=self.girisKontrol, warnings=True)
        if "The username you entered doesn't belong to an account. Please check your username and try again." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"),2)
        elif "Sorry, your password was incorrect. Please double-check your password." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
        elif self.BASE_URL + "accounts/login/two_factor" in self.driver.current_url:
            self.girisDogrulama()
        elif self.driver.current_url != self.BASE_URL + "accounts/login/":
            self.uyariOlustur(self.configGetir(base_warnings+"warning3"), 1)
            self.girisYapildimi = True
        else:
            self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 2)

    def girisDogrulama(self, durum=True):
        base_warnings = self.BASE_UYARI(metod=self.girisDogrulama, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.girisDogrulama, inputs=True)
        kod = input(self.configGetir(base_inputs+"input1")).strip()
        if not kod:
            self.girisYap(durum)

        if durum:
            sleep(5)
        kodInput = self.driver.find_elements_by_css_selector('form input')[0]
        kodInput.send_keys(kod)
        kodInput.send_keys(Keys.ENTER)
        sleep(5)
        if "A security code is required." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning1"), 2)
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif "Please check the security code and try again." in self.driver.page_source:
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 2)
            self.inputTemizle(kodInput)
            self.girisDogrulama(False)
        elif self.BASE_URL + "accounts/login/two_factor" not in self.driver.current_url:
            self.girisYapildimi = True
            self.uyariOlustur(self.configGetir(base_warnings+"warning3"),1)
        else:
            self.uyariOlustur(self.configGetir(base_warnings+"warning4"),2)

    def inputTemizle(self, inpt):
        inpt.clear()

    def hedefKaynaktanBuyukMu(self, hedef, kaynak):
        if hedef > kaynak:
            hedef = kaynak
        return hedef

    def kullaniciTakipcileriniTakipEt(self, kullanici, secim,secilenIslem=None):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciTakipcileriniTakipEt, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.kullaniciTakipcileriniTakipEt, inputs=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            hedefTakipciSayisi = None

            if secilenIslem is None:
                for uyari in self.configGetir(base_warnings+"warning1"):
                    self.uyariOlustur(uyari, 1)
                secilenIslem = str(input(self.configGetir(base_inputs+"input1")).strip())
                self.anaMenuyeDonsunMu(secilenIslem)

            if secilenIslem == "1":
                self.uyariOlustur(self.configGetir(base_warnings+"warning2"),1)
            elif secilenIslem == "2":
                self.uyariOlustur(self.configGetir(base_warnings+"warning3"),1)
                hedefTakipciSayisi = input(self.configGetir(base_inputs+"input2")).strip()
                self.anaMenuyeDonsunMu(hedefTakipciSayisi)
                if hedefTakipciSayisi.isnumeric():
                    hedefTakipciSayisi = int(hedefTakipciSayisi)
                else:
                    self.uyariOlustur(self.configGetir(base_warnings+"warning4"), 2)
                    print("")
                    self.kullaniciTakipcileriniTakipEt(kullanici, secim,  secilenIslem=secilenIslem)
            else:
                self.uyariOlustur(self.configGetir(base_warnings+"warning5"), 2)
                print("")
                self.kullaniciTakipcileriniTakipEt(kullanici, secim, secilenIslem=None)

            print(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici))

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
                sleep(5)

                while devamEtsinMi:
                    dialog_popup = self.driver.find_element_by_css_selector('div._1XyCr')
                    takipciListe = dialog_popup.find_elements_by_css_selector('div.PZuss > li')
                    for takipci in takipciListe:
                        takipciKullaniciAdi = takipci.find_element_by_css_selector("a.FPmhX").get_attribute('href')
                        takipciKullaniciAdi = takipciKullaniciAdi.replace(self.BASE_URL, '').replace('/', '')
                        try:
                            btn_takip = takipci.find_element_by_css_selector('button.sqdOP')
                            if btn_takip.text == "Follow":
                                self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(
                                    index=takipIstekSayisi + 1, takipci=takipciKullaniciAdi), 1)
                                btn_takip.click()
                                takipIstekSayisi = takipIstekSayisi + 1
                                if takipIstekSayisi == takipciSayisi:
                                    devamEtsinMi = False
                                    break
                                sleep(self.beklemeSuresiGetir(5, 15))
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
                        sleep(3)
                print(str(self.configGetir(base_warnings+"warning8")).format(kullanici=kullanici))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning9")).format(kullanici=kullanici),
                                  2)
            self.profilSec(secim)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(kullanici=kullanici,hata=str(error)), 2)
            self.profilSec(secim)

    def kullaniciKontrol(self, kullanici):
        return self.urlKontrol(self.BASE_URL + kullanici)

    def kullaniciTakipDurumDegistir(self,kullanici,durum):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciTakipDurumDegistir, warnings=True)
        if self.hesapGizliMi():
            btn_takip = self.driver.find_element_by_css_selector("button.BY3EC")
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici), 1)
                elif btn_text == "requested":
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici),
                                      1)
                elif btn_text == "unblock":
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                        kullanici=kullanici), 1)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                    kullanici=kullanici), 1)
        else:
            btn_takip = self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN')
            btn_text = str(btn_takip.text).lower()
            if durum:
                if btn_text in ["follow","follow back"]:
                    btn_takip.click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(kullanici=kullanici), 1)
                elif btn_text == "unblock":
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici), 1)
                else:
                    ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                    if ariaLabel == "Following":
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(
                            kullanici=kullanici), 1)
            else:
                ariaLabel = btn_takip.find_element_by_tag_name("span").get_attribute("aria-label")
                if ariaLabel == "Following":
                    btn_takip.click()
                    sleep(0.50)
                    self.driver.find_elements_by_css_selector("div.mt3GC >button.aOOlW")[0].click()
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning8")).format(kullanici=kullanici), 1)

    def kullaniciTakipEt(self, kullanici, secim,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciTakipEt, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici))


            self.kullaniciTakipDurumDegistir(kullanici=kullanici,durum=durum)
            if durum:
                print(str(self.configGetir(base_warnings+"warning3")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici))
            if secim != 14:
                self.profilSec(secim)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(kullanici=kullanici,hata=str(error)),2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici,
                                                                                         hata=str(error)), 2)
            if secim != 14:
                self.profilSec(secim)


    def kullaniciEngelDurumDegistir(self):
        self.driver.find_element_by_css_selector("button.wpO6b").click()
        sleep(0.50)
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()
        sleep(0.50)
        self.driver.find_elements_by_css_selector("div.mt3GC > button.aOOlW")[0].click()

    def kullaniciEngelle(self, kullanici, secim,durum=True):
        base_warnings = self.BASE_UYARI(metod=self.kullaniciEngelle, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if durum:
                print(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning2")).format(kullanici=kullanici))

            if self.hesapGizliMi():
                btnText = str(self.driver.find_element_by_css_selector('button.BY3EC').text).lower()
                if durum:
                    if btnText!="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(kullanici=kullanici), 2)
                else:
                    if btnText=="unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici), 2)
            else:
                btnText =str(self.driver.find_element_by_css_selector('span.vBF20 > button._5f5mN').text).lower()
                if durum:
                    if btnText != "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(kullanici=kullanici), 2)
                else:
                    if btnText == "unblock":
                        self.kullaniciEngelDurumDegistir()
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(kullanici=kullanici), 2)

            if durum:
                print(str(self.configGetir(base_warnings+"warning7")).format(kullanici=kullanici))
            else:
                print(str(self.configGetir(base_warnings+"warning8")).format(kullanici=kullanici))
            self.profilSec(secim)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning9")).format(kullanici=kullanici,hata=str(error)),2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(kullanici=kullanici,hata=str(error)), 2)
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
            base_warnings = self.BASE_UYARI(metod=self.albumIcerikUrlGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format( url=str(self.driver.current_url), hata=str(error)), 2)
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
                sleep(1)
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
            base_warnings = self.BASE_UYARI(metod=self.albumIcerikUrlGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
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
            base_warnings = self.BASE_UYARI(metod=self.gonderiUrlGetir, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(hata=str(error)), 2)
            return None, None

    def gonderiVarMi(self, kullanici, gonderiSayisi, secim):
        if gonderiSayisi < 1:
            base_warnings = self.BASE_UYARI(metod=self.gonderiVarMi, warnings=True)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(kullanici=kullanici), 2)
            self.profilSec(secim)

    def gonderileriIndir(self, kullanici, secim):
        base_warnings = self.BASE_UYARI(metod=self.gonderileriIndir, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings+"warning1")).format(
                    kullanici=kullanici))
                gonderiSayisi = int(self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text)
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)

                ilkGonderi = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]")
                ilkGonderi.click()
                sleep(1)
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
                    sleep(3)
                self.klasorDegistir("../")
                print(str(self.configGetir(base_warnings+"warning2")).format(
                    kullanici=kullanici))
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(
                    kullanici=kullanici), 2)

            self.profilSec(secim)
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(kullanici=kullanici, hata=error), 2)
            self.profilSec(secim)

    def gonderiIndir(self):
        base_warnings = self.BASE_UYARI(metod=self.gonderiIndir, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiIndir, inputs=True)
        try:
            url = input(self.configGetir(base_inputs+"input1")).strip()
            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url,self.gonderiIndir())
            self.urlGecerliMi(url,self.gonderiIndir())

            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)
            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings+"warning2")).format(url=url))
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
                print(str(self.configGetir(base_warnings+"warning3")).format(url=url))
                self.klasorDegistir("../")
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(
                    url=url), 2)
            self.gonderiIndir()
        except Exception as error:
            print(
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(hata=error), 2))
            self.gonderiIndir()

    def gonderiBegenDurumDegistir(self, btn):
        btn.click()
        self.indexArtir()
        sleep(0.50)
        self.gonderiIlerlet()
        sleep(self.beklemeSuresiGetir(5, 15))

    def gonderileriBegen(self, kullanici, secim, durum=True):
        base_warnings = self.BASE_UYARI(metod=self.gonderileriBegen, warnings=True)
        try:
            self.kullaniciProfilineYonlendir(kullanici)
            if not self.hesapGizliMi():
                print(str(self.configGetir(base_warnings+"warning1")).format(
                    kullanici=kullanici))
                gonderiSayisi = int(self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span").text)
                self.gonderiVarMi(kullanici, gonderiSayisi, secim)
                ilkGonderi = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]")
                ilkGonderi.click()
                sleep(1)
                self.klasorOlustur(kullanici)
                self.indexSifirla()
                for index in range(gonderiSayisi):
                    btn_begen = self.begenButonuGetir()
                    begeniDurum = self.begenButonuDurumGetir(btn_begen)
                    if durum:
                        if begeniDurum == "like":
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning2")).format(index=str(self.index),
                                                                                                     url=self.driver.current_url), 1)
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(url=self.driver.current_url), 1)
                            self.gonderiIlerlet()
                            sleep(5)
                    else:
                        if begeniDurum == "unlike":
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(index=str(self.index),
                                                                                                     url=self.driver.current_url),
                                              1)
                            self.gonderiBegenDurumDegistir(btn_begen)
                        else:
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(url=self.driver.current_url), 1)
                            self.gonderiIlerlet()
                            sleep(5)
                print(str(self.configGetir(base_warnings+"warning6")).format(
                    kullanici=kullanici))
                self.profilSec(secim)
            else:
                if durum:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(
                        kullanici=kullanici), 2)
                else:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning8")).format(
                        kullanici=kullanici), 2)
                self.profilSec(secim)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning9")).format(
                    kullanici=kullanici, hata=error), 2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(
                    kullanici=kullanici, hata=error), 2)
            self.profilSec(secim)

    def gonderiBegen(self, durum=True):
        base_warnings = self.BASE_UYARI(metod=self.gonderiBegen, warnings=True)
        base_inputs = self.BASE_UYARI(metod=self.gonderiBegen, inputs=True)

        try:
            if durum:
                url = input(self.configGetir(base_inputs+"input1")).strip()
            else:
                url = input(self.configGetir(base_inputs+"input2")).strip()

            self.anaMenuyeDonsunMu(url)
            self.urlGirildiMi(url, self.gonderiBegen(durum))
            self.urlGecerliMi(url,self.gonderiBegen(durum))

            print(str(self.configGetir(base_warnings+"warning1")).format(url=url))
            self.urlYonlendir(url)
            if not self.hesapGizliMi():
                if durum:
                    print(str(self.configGetir(base_warnings+"warning2")).format(url=url))
                else:
                    print(str(self.configGetir(base_warnings+"warning3")).format(url=url))
                btn_begen = self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
                begeniDurum = self.begenButonuDurumGetir(btn_begen)
                if durum:
                    if begeniDurum == "like":
                        btn_begen.click()
                        print(
                            self.uyariOlustur(str(self.configGetir(base_warnings+"warning4")).format(url=self.driver.current_url),
                                              1))
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning5")).format(url=self.driver.current_url), 1)
                else:
                    if begeniDurum == "unlike":
                        btn_begen.click()
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning6")).format(url=self.driver.current_url), 1)
                    else:
                        self.uyariOlustur(str(self.configGetir(base_warnings+"warning7")).format(url=self.driver.current_url), 1)
                if durum:
                    print(str(self.configGetir(base_warnings+"warning8")).format(url=url))
                else:
                    print(str(self.configGetir(base_warnings+"warning9")).format(url=url))
            else:
                if durum:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning10")).format(
                        url=url), 2)
                else:
                    self.uyariOlustur(str(self.configGetir(base_warnings+"warning11")).format(
                        url=url), 2)
            self.gonderiBegen(durum)
        except Exception as error:
            if durum:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning12")).format(hata=error),2)
            else:
                self.uyariOlustur(str(self.configGetir(base_warnings+"warning13")).format(hata=error), 2)
            self.gonderiBegen(durum)



    def uyariOlustur(self, mesaj, durum):
        if durum == 1:
            uyari= colored(mesaj, "green")
        elif durum == 2:
            uyari=  colored(mesaj, "red")
        elif durum == 3:
            uyari=  colored(mesaj, "blue")
        print(uyari)

    def klasorOlustur(self, klasor):
        base_warnings = self.BASE_UYARI(metod=self.klasorOlustur, warnings=True)
        if not os.path.exists(klasor):
            os.mkdir(klasor)
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning1")).format(klasor=klasor), 1)
            self.klasorDegistir(klasor)
            print(str(self.configGetir(base_warnings+"warning2")).format(klasor=klasor))
        else:
            print(str(self.configGetir(base_warnings+"warning3")).format(klasor=klasor))
            self.klasorDegistir(klasor)
            print(str(self.configGetir(base_warnings+"warning4")).format(klasor=klasor))

    def klasorDegistir(self, klasor):
        os.chdir(klasor)

    def oturumKapat(self):
        base_warnings = self.BASE_UYARI(metod=self.oturumKapat, warnings=True)
        print(self.configGetir(base_warnings+"warning1"))
        try:
            self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]").click()
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div").click()
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 1)
            self.driver.get(self.BASE_URL + 'accounts/login/')
            self.girisYapildimi = False
            self.girisYap()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(hata=str(error)), 2)
            self.menu()

    def quit(self):
        base_warnings = self.BASE_UYARI(metod=self.quit, warnings=True)
        try:
            print(self.configGetir(base_warnings+"warning1"))
            self.driver.quit()
            self.uyariOlustur(self.configGetir(base_warnings+"warning2"), 1)
            exit()
        except Exception as error:
            self.uyariOlustur(str(self.configGetir(base_warnings+"warning3")).format(hata=str(error)), 2)
            self.driver.quit()
            exit()

try:
    instagram = Instagram()
except KeyboardInterrupt:
    print("\n [*] Python uygulamasından çıkış yapılıyor...")
    exit()


