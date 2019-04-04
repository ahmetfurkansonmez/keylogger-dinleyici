import socket
# baglanti kurmak dinlemek v.b islemler icin kullandigimiz kutuphane

dinleyici = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# dinleyicimizi tanimlayip icine kullanacagimiz protokolu ve socket tipini belirliyoruz

dinleyici.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)

dinleyici.bind(("192.168.0.106", 8080))

# kendi agimiza baglanip 8080 portundaki baglantilari dinliyoruz.

dinleyici.listen(0)

print("Dinleniyor...")

(baglanti, adres) = dinleyici.accept()

# gelen herhangi bir baglantiyi kabul edip baglantinin adresini ekrana yazdiriyoruz.

print(adres)

# sonsuz bir dongu olusturup baglanti uzerinden gelen verileri gelen_veriler adli bir degiskene kaydedip gelen verileri ekranda cikti olarak gosteriyoruz.

while True:

    gelen_veriler = baglanti.recv(1024)

    print(str(gelen_veriler))

#-------------------------------------------ahmetfurkansonmez12@gmail.com-------------------------------------------