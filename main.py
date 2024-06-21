# ornek_metin.txt dosyasını açar ve okuma + yazma yetkisi verir.
with open(r"ornek_metin.txt", "r+") as f:
    # kalanlar.txt dosyasını açar ve yazma yetkisi verir.
    with open("kalanlar.txt", "w") as g:
        # gecenler.txt dosyasını açar ve yazma yetkisi verir.
        with open("gecenler.txt", "w") as b:

            # ornek_metin.txt içeriğini icerik adlı değişkenin içerisine satır biçiminde aktarır.
            icerik = f.readlines()
            m = 0
            # icerik'in satırlarını döngü ile satir değişkenine aktarır ve işler.
            for satir in icerik:
                # ornek_metin.txt içerisindeki ilk satırı atlar.
                if m == 0:
                    m += 1
                    continue

                # Her bir satırdaki yeni satır karakterini kaldırır.
                satir = satir.replace("\n", "")
                
                # Satırdaki boşluk karakterlerinin sayısını ve konumlarını belirler.
                bosluk_karakteri = 0
                bosluk_indexleri = []
                index = 0

                # Satırdaki her karakteri kontrol eder ve boşluk karakterlerini sayar.
                for karakter in satir:
                    if karakter == " ":
                        bosluk_karakteri += 1
                        bosluk_indexleri.append(index)
                    index += 1

                # Ad ve soyadı ayırır.
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")
                
                # Notları ayırır ve sayısal değerlere dönüştürür.
                notlar = satir.split(" ")[-1]
                notlar = notlar.split("/")
                vize1 = int(notlar[0])
                vize2 = int(notlar[1])
                final = int(notlar[2])

                # Ortalama hesaplar.
                ortalama = vize1 * 0.3 + vize2 * 0.3 + final * 0.4

                # Durumu belirler (Geçti veya Kaldı).
                durum = " "
                if ortalama >= 50 and final >= 70:
                    durum = "Gecti"
                else:
                    durum = "Kaldi"

                # Bölümü belirler.
                bolum = satir[bosluk_indexleri[0] + 1:bosluk_indexleri[-1]]

                # Duruma göre öğrenciyi ilgili dosyaya yazar.
                if durum == "Gecti":
                    b.write(ad)
                    b.write(" " * (25 - len(ad)))
                    b.write(soyad)
                    b.write(" " * (25 - len(soyad)))
                    b.write(bolum)
                    b.write(" " * (25 - len(bolum)))
                    b.write(str(round(ortalama, 1)))
                    b.write(" " * 21)
                    b.write(durum)
                    b.write("\n")
                else:
                    g.write(ad)
                    g.write(" " * (25 - len(ad)))
                    g.write(soyad)
                    g.write(" " * (25 - len(soyad)))
                    g.write(bolum)
                    g.write(" " * (25 - len(bolum)))
                    g.write(str(round(ortalama, 1)))
                    g.write(" " * 21)
                    g.write(durum)
                    g.write("\n")
