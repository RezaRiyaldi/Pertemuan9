# Pertemuan 9
## List, Tuple, Dictionary

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Reza Riyaldi Irawan |
| **NIM** | 312010284 |
| **Kelas** | TI.20.A.2 |
| **Mata Kuliah** | Bahasa Pemrograman |

## Daftar Isi
* [Pertemuan 9](https://github.com/RezaRiyaldi/Pertemuan9#pertemuan-9)
    * [Labspy04](https://github.com/RezaRiyaldi/Pertemuan9#Labspy-04) | [direktori](https://github.com/RezaRiyaldi/Pertemuan9/tree/main/Labspy04) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy04/labs04.py)
    * [Labspy05](https://github.com/RezaRiyaldi/Pertemuan9#Labspy-05) | [direktori](https://github.com/RezaRiyaldi/Pertemuan9/tree/main/Labspy05) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/labs05.py)
         * [Membuat Kerangka](https://github.com/RezaRiyaldi/Pertemuan9#membuat-kerangka)
         * [Program](https://github.com/RezaRiyaldi/Pertemuan9#program)
         * [Tambah Data](https://github.com/RezaRiyaldi/Pertemuan9#tambah-data-t)
         * [Lihat Data](https://github.com/RezaRiyaldi/Pertemuan9#lihat-data-l)
         * [Ubah Data](https://github.com/RezaRiyaldi/Pertemuan9#ubah-data-u)
         * [Hapus Data](https://github.com/RezaRiyaldi/Pertemuan9#hapus-data-h)
         * [Cari Data](https://github.com/RezaRiyaldi/Pertemuan9#cari-data-c)
         * [Keluar Program](https://github.com/RezaRiyaldi/Pertemuan9#keluar-dari-program-k)
         
 
        
### Labspy 04
Konsep Program :
- Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
- Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya.
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)

Pada Labspy04 ini saya akan menjelaskan program yang saya buat. Berikut [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy04/labs04.py)-nya

Penjelasan
1. Deklarasi list, ketika menginput data maka akan dimasukan ke dalam list ini
```python
# LIST
namaMahasiswa = []
nimMahasiswa = []
nilaiTugasMahasiswa = []
nilaiUTSMahasiswa = []
nilaiUASMahasiswa = []
```

2. Membuat program _infinite loop_ (loop tak terbatas)
```python
while True:
```

3. Pada program inputan langsung ditambahkan ke _LIST_ dengan method `.append`, sedangkan untuk nilai(Tugas, UTS, UAS) dimasukan ke variable terlebih dahulu untuk perhitungan nilai akhir
```python
namaMahasiswa.append(input("Masukan nama : "))
nimMahasiswa.append(int(input("Masukan NIM  : ")))
_nilaiTugas = int(input("Nilai tugas  : ")); nilaiTugasMahasiswa.append(_nilaiTugas)
_nilaiUTS = int(input("Nilai UTS    : ")); nilaiUTSMahasiswa.append(_nilaiUTS)
_nilaiUAS = int(input("Nilai UAS    : ")); nilaiUASMahasiswa.append(_nilaiUAS)
```

4. Program input tanya tambah data [y/t], apabila jawaban t, maka program inputan terhenti `break` dan akan menampilkan data yang sudah diinput
```python
_tanya = input("Tambah data lagi? [y/t]: ")
print()
if(_tanya == "t" or _tanya =="T"):
    break
```

5. Untuk membuat header table, pada `print(71*"=")`, membuat "=" sebanyak 71 sebagai garis, dan penggunaan format string agar terlihat rapih. 
```python
print(71*"=")
print("| {0:^2} | {1:^18} | {2:^7} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
print(71*"=")
```

6. Deklarasi `no = 0` untuk membuat nomor pada isi table, lalu membuat perulang `for`
- Inisialisasi `nama, nim, nilaiTugas, nilaiUTS, nilaiUAS`, sesuai urutan yang ada di dalam `zip`
- Pada list yang dimaksud, `in zip` berfungsi untuk membungkus semua list
```python
no = 0
for nama, nim, nilaiTugas, nilaiUTS, nilaiUAS in zip(namaMahasiswa, nimMahasiswa, nilaiTugasMahasiswa, nilaiUTSMahasiswa, nilaiUASMahasiswa):
```

7. Untuk membuat nomor dimulai dari 1 maka `no +=1`, lalu membuat perhitungan untuk nilai akhir
```python
no += 1    
tugas = _nilaiTugas * 30/100
UTS = _nilaiUTS * 35/100
UAS = _nilaiUAS * 35/100
nilaiAkhir = tugas + UTS + UAS
```

8. Membuat isi table sesuai dengan inisialisi diatas, dengan format string agar terlihat rapih
```python
print("| {0:>2} | {1:<18} | {2:>7} | {3:>5} | {4:>5} | {5:>5} | {6:>7.2f} |".format(no, nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir))
```

9. Untuk membuat garis paling bawah ketika looping isi table selesai
```python
print(71*"=")
```

Maka program seperti berikut.

![Output Labspy04](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy04/gambar/labspy04-output.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

### Labspy 05
Konsep Program :
- Program dibuat dengan menggunakan Dictionary
- Tampilkan menu pilihan: (Tambah Data, Tampilkan Data, Ubah Data, Hapus Data, Cari Data)
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)

Pada Labspy05 ini saya akan menjelaskan program yang saya buat. Berikut [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/labs05.py)-nya

#### Membuat kerangka
1. Membuat kerangka _(Blueprint)_ untuk membentuk suatu objek
```python
class Mahasiswa:
```

2. Menambahkan method `__init__()`, agar setiap class dipanggil maka program akan memprioritaskan function `__init__()` dan untuk menangkap data dari program inputan
```python
 def __init__(self, _nama, _nim, _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir):
```

3. Mengakses Variable yang ada di dalam class menggunakan `self`
```python
self.nama       = str(_nama) 
self.nim        = str(_nim) 
self.nilaiTugas = int(_nilaiTugas)
self.nilaiUTS   = int(_nilaiUTS)
self.nilaiUAS   = int(_nilaiUAS)
self.nilaiAkhir = float(_nilaiAkhir)
```

4. Membuat function input data `Data_Mahasiswa()`
```python
def setNama(self, _nama):
   self.nama = _nama

def setNim(self, _nim):
   self.nim = _nim

def setNilaiTugas(self, _nilaiTugas):
   self.nilaiTugas = _nilaiTugas

def setNilaiUTS(self, _nilaiUTS):
   self.nilaiUTS = _nilaiUTS

def setNilaiUAS(self, _nilaiUAS):
   self.nilaiUAS = _nilaiUAS

def setNilaiAkhir(self, _nilaiAkhir):
   self.nilaiAkhir = _nilaiAkhir
```

5. Membuat function menampilkan data, yang menggunakan method `return`
```python
def getNama(self):
  return self.nama 

def getNim(self):
   return self.nim 

def getNilaiTugas(self):
   return self.nilaiTugas 

def getNilaiUTS(self):
   return self.nilaiUTS 

def getNilaiUAS(self):
   return self.nilaiUAS 

def getNilaiAkhir(self):
   return self.nilaiAkhir 
```

6. Membuat function dan deklarasi variable
```python
# Function2an
def garis():
    print(71*"=")

def header():
    garis()
    print("| {0:^2} | {1:^7} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "NIM", "Nama", "Tugas", "UTS", "UAS", "Akhir"))
    garis()
  
def tidakAdaData(): 
    header()          
    print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
    garis()

# Deklarasi Variable
Data_Mahasiswa = {} 
loop = True
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Program
1. Membuat judul
```python
print(23*"=")
print("= Program Input Nilai =")
print(23*"=")
```

2. Membuat perulangan tak terhingga _Infinite Loop_ dari variable `loop = True`
```python
while(loop):
```

3. Membuat Menu dan inputan yang dimasukan kedalam variable menu
```python
print()
menu = input("[(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar] : ")
print(71*"-")
print()
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Tambah Data (T)
1. Apabila Menu yang dipilih adalah (t/T) maka akan masuk ke tambah data
```python
# Tambah Data {
if menu == 'T' or menu == 't':
      print("Tambah data") 
```

2. Menginput dan memasukannya kedalam variable
```python
nim        = input("NIM         : ")
nama       = input("Nama        : ")
nilaiTugas = int(input("Nilai Tugas : "))
nilaiUTS   = int(input("Nilai UTS   : "))
nilaiUAS   = int(input("Nilai UAS   : "))
```

3. Membuat perhitungan nilai akhir
```python
nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
```

4. Memasukan data ke dalam class `Mahasiswa` dan diteruskan ke dictionary `Data_Mahasiswa`
```python
mhs = Mahasiswa(nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir) 
Data_Mahasiswa[nim] = mhs 
```

Maka program Tambah akan seperti berikut.

![output-tambah](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/Output-tambah.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Lihat Data (L)
1. Apabila Menu yang dipilih adalah (l/L) maka akan masuk ke Daftar Mahasiswa
```python
# Lihat Data {
elif menu == 'L' or menu == 'l':
```

2. Percabangan, apabila data tidak ada maka akan tampil "TIDAK ADA DATA" dengan function `tidakAdaData()`
```python
print("Daftar Mahasiswa")
if len(Data_Mahasiswa) <= 0:  
   tidakAdaData()
```

Seperti gambar berikut.

![output-lihat-1](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output_lihat-1.PNG)

3. Namun apabila data lebih dari `>= 0` maka data akan keluar
- Menggunakan looping `for` yang ada di dalam `Data_Mahasiswa`
- Akses datanya melalui `function` yang mereturn data
- Deklarasi var `L_data = Data_Mahasiswa[i]`
- Penggunakan `f-string + format string` untuk output-an
- Untuk nilai akhir agar dibelakang (,) hanya 2 digit, menggunakan `.2f`
```python
else:
   no = 0
   header()
   for i in Data_Mahasiswa:
       no += 1 
       L_Data = Data_Mahasiswa[i]
       print(f"| {no:>2} | {L_Data.getNim():>7} | {L_Data.getNama():<18} | {L_Data.getNilaiTugas():>5} | {L_Data.getNilaiUTS():>5} | {L_Data.getNilaiUAS():>5} | {L_Data.getNilaiAkhir():>7.2f} |")                
   garis()        
```

Maka program Lihat data akan seperti berikut.

![output-lihat-2](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output_lihat-2.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Ubah Data (U)
1. Apabila Menu yang dipilih adalah (u/U) maka akan masuk ke Ubah Data Mahasiswa Berdasarkan NIM
```python
# Ubah Data {
elif menu == "U" or menu == "u":
```

2. Percabangan, apabila data tidak ada maka akan tampil "TIDAK ADA DATA" dengan function `tidakAdaData()`
```python
print("Ubah Data Mahasiswa berdasarkan NIM")
if len(Data_Mahasiswa) <= 0:  
   tidakAdaData()
```

Seperti gambar berikut.

![output-u-1](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-1.PNG)

3. Namun apabila data lebih dari `>= 0` maka data akan keluar
- Dimulai dengan memasukkan NIM yang ingin diubah, jika salah memasukkan NIM maka akan keluar "Data tidak ditemukan!!!".

Seperti gambar berikut.

![output-u-2](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-2.PNG)

- Jika NIM benar maka akan tampil Nama, NIM, Nilai (Tugas, UTS, UAS). dengan memanggil function yang mereturn data
```python
else:
   nim = str(input("Masukan nim : ")) 
   if(nim in Data_Mahasiswa):
       U_data = Data_Mahasiswa[nim]
       print(f"Nama        = {U_data.getNama()}")
       print(f"NIM         = {U_data.getNim()}")
       print(f"Nilai Tugas = {U_data.getNilaiTugas()}")
       print(f"Nilai UTS   = {U_data.getNilaiUTS()}")
       print(f"Nilai UAS   = {U_data.getNilaiUAS()}")
       ....
       
    else:
       print("Data tidak ditemukan!!!") 
```

4. Data menu apa yang ingin di ubah
```python
print(25*"=")
print("1. Nama\n2. NIM\n3. Nilai")
tanya = int(input("Apa yang ingin diubah? [1-3] : "))
```

Seperti gambar berikut.

![output-u-3](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-3.PNG)


5. Jika memilih `1 Nama` hanya memasukkan nama baru, lalu dimasukkan menggunakan function setNama()
```python
if tanya == 1:
     namaBaru = str(input("Masukan Nama Baru : ")) 
     U_data.setNama(namaBaru) 
```

Maka program Ubah Nama data akan seperti berikut.

![output-u-nama](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-nama.PNG)

6. Jika memilih `2 NIM`
- Memasukkan NIM baru
- Data dimasukkan menggunakan function setNim()
- Menghapus data yang memilik NIM yang lama dengan method `del`
```python
elif tanya == 2:
     nimBaru = str(input("Masukan Nim Baru : ")) 
     Data_Mahasiswa[nim].setNim(nimBaru)
     Data_Mahasiswa[nimBaru] = Data_Mahasiswa[nim] 
     del Data_Mahasiswa[nim]
```

Maka program Ubah NIM data akan seperti berikut.

![output-u-nim](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-NIM.PNG)

7. Jika memilih `3 Nilai`
- Memasukkan nilai (Tugas, UTS, UAS) yang baru
- Data akan dimasukan dengan function setNilai(Tugas, UTS, UAS) yang baru
- Lalu membuat perhitungan untuk nilai akhir, dan dimasukkan ke function setNilaiAkhir() yang baru
```python
elif tanya == 3:
     nilaiTugasBaru = int(input("Masukan Nilai Tugas Baru : "))
     nilaiUTSBaru = int(input("Masukan Nilai UTS Baru : "))
     nilaiUASBaru = int(input("Masukan Nilai UAS Baru : "))
     U_data.setNilaiTugas(nilaiTugasBaru)
     U_data.setNilaiUTS(nilaiUTSBaru)
     U_data.setNilaiUAS(nilaiUASBaru)
     nilaiAkhirBaru = nilaiTugasBaru * 30/100 + nilaiUTSBaru * 35/100 + nilaiUASBaru * 35/100
     U_data.setNilaiAkhir(nilaiAkhirBaru)
```

Maka program Ubah Nilai data akan seperti berikut.

![output-u-nim](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-nilai.PNG)

8. Jika data salah dimasukkan maka akan muncul "Pilihan yang dimasukkan tidak ada!"
```python
else:
     print("Pilihan yang anda masukan tidak ada!")
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Hapus Data (H)
1. Apabila Menu yang dipilih adalah (h/H) maka akan masuk ke Hapus Data Mahasiswa Berdasarkan NIM
```python
# Hapus Data {
elif menu == "H" or menu == "h":
```


2. Percabangan, apabila data tidak ada maka akan tampil "TIDAK ADA DATA" dengan function `tidakAdaData()`
```python
print("Hapus Data Mahasiswa berdasarkan NIM")
if len(Data_Mahasiswa) <= 0:  
   tidakAdaData()
```

Seperti gambar berikut.

![output-h-1](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-hapus-1.PNG)

3. Namun apabila data lebih dari `>= 0` maka program dijalankan
- memasukkan NIM yang ingin di hapus

Maka program Hapus data akan seperti berikut..

![output-h-2](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-hapus-2.PNG)

- Jika NIM yang dimaksud tidak ada/salah, maka akan keluar "Data tidak ditemukan!!!"
```python
else:
   nim = str(input("Masukan NIM : "))
   if(nim in Data_Mahasiswa):
       del Data_Mahasiswa[nim] 
       
   else:
       print("Data tidak ditemukan!!!") 
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Cari Data (C)
1. Apabila Menu yang dipilih adalah (c/C) maka akan masuk ke Cari Data Mahasiswa Berdasarkan NIM
```python
elif menu == "C" or menu == "c":
```

2. Percabangan, apabila data tidak ada maka akan tampil "TIDAK ADA DATA"
```python
if len(Data_Mahasiswa) <= 0:  
   tidakAdaData()
```

Seperti gambar berikut.

![output-c-1](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-cari-1.PNG)

3. Namun apabila data lebih dari `>= 0` maka program dijalankan
- Memasukkan NIM yang ingin di cari

Maka program Cari data akan seperti berikut.

![output-c-2](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-cari-2.PNG)

- Jika NIM yang dimaksud tidak ada/salah, maka akan keluar "Data tidak ditemukan!!!"
```python
nim = str(input("Masukan NIM : ")) 
   if(nim in Data_Mahasiswa):
       no = 0
       header()
       no += 1 
       C_Data = Data_Mahasiswa[nim]
       print(f"| {no:>2} | {C_Data.getNim():>7} | {C_Data.getNama():<18} | {C_Data.getNilaiTugas():>5} | {C_Data.getNilaiUTS():>5} | {C_Data.getNilaiUAS():>5} | {C_Data.getNilaiAkhir():>7.2f} |")                  
       garis()  
       
   else:
       print("Data tidak ditemukan!!!") 
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

#### Keluar dari Program (K)
1. Apabila Menu yang dipilih adalah (k/K) maka program selesai dengan mengganti variable loop = False
```python
# Keluar {
elif menu == "K" or menu == "k":
     print("Selesai")
     loop = False 
# }
```

Seperti gambar berikut.

![output-k](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-keluar.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)
