import random
import os
import sys
import time


################################################## KONSOL AYARI ####################################################


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
clear = lambda: os.system('cls')
clear()

konum = os.getcwd()
dosyaYolu =  sys.argv[1]


################################################## FONKSİYONLAR ####################################################


# 1 den 9 a kadar rastgele sayı üretir fakat sayıların üretilme olasılığı sayının büyüklüğü ile ters orantılıdır.
def rastgeleSayiUret():
    result = ""
    for i in range(1):
        num = random.choices(range(1, 10), weights=[1 / i for i in range(1, 10)])[0]
        result += str(num)
    return result


# Oyun tahtasını oluşturur.
def oyunTahtası(dosyaYolu, satir, sutun):
    with open(dosyaYolu, "w") as dosya:
        for i in range(satir):
            for j in range(sutun):
                deger = rastgeleSayiUret()
                dosya.write(str(deger))
            dosya.write("\n")


# 2 boyutlu diziyi dosyadan okur.
def dosyadanDiziye(dosyaYolu):
    with open(dosyaYolu, "r") as dosya:
        matris = []
        for line in dosya:
            line = line.strip()
            matris.append([char for char in line])
    return matris


# Oyun tahtasını ekrana yazdırır.
def printboard(board):
    color_codes = {
        1: bcolors.OKBLUE,
        2: bcolors.FAIL,
        3: bcolors.OKGREEN,
        4: bcolors.WARNING,
        5: bcolors.OKCYAN,
        6: bcolors.HEADER,
        7: bcolors.ENDC,
        8: bcolors.ENDC,
        9: bcolors.ENDC
    }

    for i in range(len(board)):
        p = ""
        for j in range(len(board[0])):
            try:
                num = int(board[i][j])
            except ValueError:
                num = board[i][j]
            color = color_codes.get(num, bcolors.ENDC)
            p += f"{color}{num} "
        print(p)
    return board


# Dizinin seçilen elemana temas eden aynı değerde elemanı kontrol eder. (iç içe fonksiyon kullanıldı)
def sayiKontrol(tahta, satir, sutun, s=0):
    karakter = tahta[satir][sutun]
    toplam = 1
    if karakter != " ":
        if satir < len(tahta)-1 and karakter == tahta[satir+1][sutun]:
            tahta[satir][sutun] = " "
            toplam += sayiKontrol(tahta, satir+1, sutun, 1)

        if satir > 0 and karakter == tahta[satir-1][sutun]:
            tahta[satir][sutun] = " "
            toplam += sayiKontrol(tahta, satir-1, sutun, 1)

        if sutun > 0 and karakter == tahta[satir][sutun-1]:
            tahta[satir][sutun] = " "
            toplam += sayiKontrol(tahta, satir, sutun-1, 1)

        if sutun < len(tahta[0])-1 and karakter == tahta[satir][sutun+1]:
            tahta[satir][sutun] = " "
            toplam += sayiKontrol(tahta, satir, sutun+1, 1)

        if s < 1 and toplam < 2:
            return 0

    tahta[satir][sutun] = " "
    return toplam


# Oyun tahtasında boş kalan yerlere üstteki elemanların gelmesi için.
def dusur(tahta):
    for satir in range(len(tahta)-1):
        for sutun in range(len(tahta[satir])):
            if tahta[satir+1][sutun] == " " and tahta[satir][sutun] != " ":
                tahta[satir+1][sutun] = tahta[satir][sutun]
                tahta[satir][sutun] = " "
                dusur(tahta)
    return tahta


# Fibonacci fonksiyonu
def fibonaci(n):
    if n <= 1:
        return n
    else:
        return (fibonaci(n-1) + fibonaci(n-2))


# Eğer bir sütun tamamen silinirse sağdaki tüm hücreler sola kayması için.
def kaydir(tahta):
    for sutun in range(len(tahta[0])-1):
        p = 0
        for satir in range(len(tahta)):
            if tahta[satir][sutun] == " ":
                p += 1
        if p == len(tahta):    
            for i in range(len(tahta)):
                tahta[i][sutun] = tahta[i][sutun+1]
                tahta[i][sutun+1] = " "
    return tahta   


# Tur sonrası değişikleri uygulama.
def tur(tahta, satir, sutun):
    karakter = tahta[satir][sutun]
    if karakter != " ":
        sayac = sayiKontrol(tahta, satir, sutun, 0)
        puan = int(karakter) * fibonaci(sayac)
        dusur(tahta)
        kaydir(tahta)
    return puan
    

# Oyun bittikten sonra puanı ve oyun tahtasını dosyaya yazdırır.
def matrisDosyayaYaz(tahta, dosyaYolu, puan):
    with open(dosyaYolu, "w+") as dosya:
        dosya.write(f"puan: {puan}" + "\n")
        for satir in tahta:
            for eleman in satir:
                dosya.write(str(eleman) + " ")
            dosya.write("\n")
        

# Girilen input'un sayı olup olmadığını kontrol eder.
def isItInt(prompt, limit):
    while True:
        try:
            number = int(input(prompt))
            if 1 <= number <= limit:
                return number
            else:
                print(bcolors.WARNING + f"Girilen sayı 0-{limit + 1} aralığında olmalıdır." + bcolors.ENDC + "\n")
                time.sleep(0.4)
        except ValueError:
            print(bcolors.FAIL + "Lütfen geçerli bir sayı girin." + bcolors.ENDC + "\n")




##################################################### OYUN #########################################################


print(bcolors.WARNING + "Oyuna hoşgeldiniz!"  + bcolors.ENDC + "\n") 
time.sleep(0.6)
print(bcolors.WARNING + "Kurallar: "  + bcolors.ENDC + "\n")
time.sleep(0.8)
print(bcolors.WARNING + "1 - Oyun zemini boyutunu seçiniz. örn (8x6), max (50x50)" + bcolors.ENDC)
time.sleep(1.4)
print(bcolors.WARNING + "2 - Oynuycağınız tur sayısını seçiniz. max 20" + bcolors.ENDC)
time.sleep(1.4)
print(bcolors.WARNING + "3 - Aynı sayıları yan yana bulmaya çalışın, değeri yüksek sayılar daha fazla puan getirir." + bcolors.ENDC + "\n")
time.sleep(1.8)
clear()
print(bcolors.WARNING + "--------------------------" + bcolors.ENDC)
print("      Oyun Başladı")
print(bcolors.WARNING + "--------------------------" + bcolors.ENDC)


tekrarOyna = True


while tekrarOyna:
    satir = int(isItInt("Satır boyutunu giriniz: ", 50))
    sutun = int(isItInt("Sütun boyutunu giriniz: ", 50))
    
    print(" ")
    
    turSayisi = int(isItInt("Oynamak istediğiniz tur sayısını giriniz: ", 20))
    time.sleep(0.4)
    clear()

    oyunTahtası(sys.argv[1],satir, sutun)
    tahta = dosyadanDiziye(sys.argv[1])

    puan = 0

    for i in range(turSayisi):
        print(bcolors.OKGREEN + f"Puanınız: {puan}" + bcolors.ENDC + "\n")
        print(bcolors.WARNING + "--------------------------" + bcolors.ENDC + "\n")
        printboard(tahta)
        print(" ")
        print(bcolors.WARNING + "--------------------------" + bcolors.ENDC + "\n")
        secilenSatir = isItInt("Satır seçiniz: ",satir) - 1
        secilenSutun = isItInt("Sütun seçiniz: ",sutun) - 1
        time.sleep(0.4)

        if tahta[secilenSatir][secilenSutun] != " ":
            puan += tur(tahta, secilenSatir, secilenSutun)
            clear()
        else:
            print("\n" + bcolors.FAIL + "Seçilen değer boş!" + bcolors.ENDC)
            print(bcolors.FAIL + "Lütfen yeni bir değer giriniz." +  bcolors.ENDC)
            time.sleep(1.4)
            clear()

    print("Tahtanın son şekli:")
    time.sleep(0.2)
    print(bcolors.WARNING + "--------------------------" + bcolors.ENDC + "\n")
    printboard(tahta)
    print(" ")
    print(bcolors.WARNING + "--------------------------" + bcolors.ENDC)
    time.sleep(0.2)
    print(bcolors.OKCYAN + "Oyun İstatistikleri" + bcolors.ENDC + "\n\n")
    time.sleep(0.2)
    print(bcolors.HEADER + f"Toplam oynanan tur sayısı: {turSayisi}" + bcolors.ENDC + "\n")
    time.sleep(0.2)
    print(bcolors.OKGREEN + f"Toplam Puanınız: {puan}" + bcolors.ENDC)
    time.sleep(0.4)
    print(bcolors.WARNING + "--------------------------" + bcolors.ENDC + "\n")
    print("Tekrar oynamak için 1'e basınız.")
    print("Programı kapatmak için 2'ye basınız.")
    tekrarOynaKontrol = int(isItInt("",2))
    if tekrarOynaKontrol == 1:
        tekrarOyna = True
        time.sleep(0.2)
        clear()
    else:   
        matrisDosyayaYaz(tahta, sys.argv[2], puan)
        tekrarOyna= False
        clear()
        time.sleep(0.8)
        print("Oynadığınız için teşekkürler!" + "\n") 
        time.sleep(0.5)
        quit()        