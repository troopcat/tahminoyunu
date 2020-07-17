from colorama import *
import random
import os

init(autoreset=True)

puan = 0
zorluk = 0
hak = 5

s1 = 5

sayi = random.randrange(1,s1,1)

print(Fore.GREEN+"Belirtilen sayılar arasında tahmin yap doğru cevapta puan ve hak kazanacaksın 30 bölüm kolaydan zora giden bir oyun.")
while True:
    try:


        print(Fore.MAGENTA+f"Tahmin(1-{s1} arası): ",end="")
        tahmin = int(input())

        if tahmin == 402896996: # Hile kodu
            puan = puan + 99999
            hak = hak + 99999
            tahmin = sayi

        if tahmin == sayi:
            puan = puan + 5
            hak = hak + 1
            print(Fore.GREEN+f"Doğru Cevap!\n5 puan eklendi 1 hak kazandınız. Puanınız {puan}, Hakkınız {hak}")

            zorluk = zorluk + 1
            for i in range(1,s1):
                if i == zorluk:
                    s1 = s1 + 5
                    sayi = random.randrange(1,s1,1)
            if s1 >= 30:
                print(Fore.GREEN+"\nTebrikler oyunu kazandınız!")
                break

        else:
            hak = hak - 1
            if hak <= 0:
                print(Back.RED+Fore.WHITE+"Yanlış cevap. Kalan hakkınız kalmamıştır!")
                break
            else:

                print(Back.RED+Fore.WHITE+f"Yanlış cevap. Cevap {sayi} idi yeni sayı oluşturuluyor. Kalan hakkınız {hak}")
                sayi = random.randrange(1,s1,1)

    except:
        print(Back.RED+Fore.WHITE+"Bir sayı giriniz!")
