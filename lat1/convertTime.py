Detik = int(input("memasukan satuan detik"))

Hari = Detik // 86400
Detik = Detik % 86400
Jam = Detik // 3600
Detik %= 3600
Menit = Detik // 60
Detik %= 60
print(Detik)
Sisa_detik = Detik
print(Hari,":" ,Jam,":", Menit, ":",Sisa_detik)