Nik = str(input('Masukan NIK : '))
Nama = str(input('Masukan Nama : '))
Gol = int(input('Masukan Golongan : '))
JamKerja = int(input('Masukan Jam Kerja : '))

if(Gol == 1):
    GajiPokok = 1750000
    Tunjangan = 0.125
else:
    GajiPokok = 2300000
    Tunjangan = 0.15

BesarTunjangan =Tunjangan * GajiPokok

JamLembur = JamKerja - 208
Potongan = 0
#menentukan jam lembur dan besarnya
if (JamLembur < 0):
    JamKurang = 208-JamKerja
    Hari = JamKurang / 8
    Sisa = JamKurang % 8
    Potongan = Hari * 50000 + Sisa * 10000
    JamLembur = 0

Lembur = JamLembur* 25000
GajiBersih = GajiPokok + BesarTunjangan + Lembur + Potongan

print('NIK : ', Nik)
print('Nama : ',Nama)
print('Golongan : ',Gol)
print('Jumlah Jam Kerja/Bulan : ',JamKerja)
print('Gaji Pokok : ',GajiPokok)
print('Tunjangan : ',Tunjangan )
print('Lembur    : ',JamLembur)
print('           : ',Lembur)
print('Potongan  : ',Potongan)
print('Gaji Bersih :', GajiBersih)
