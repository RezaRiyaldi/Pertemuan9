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
# Function biasa
def garis():
    print(71*"=")

def header():
    garis()
    print("| {0:^2} | {1:^7} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "NIM", "Nama", "Tugas", "UTS", "UAS", "Akhir"))
    garis()

# Deklarasi Variable
Data_Mahasiswa = {} 
loop = True
```

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


#### Lihat Data (L)
1. Apabila Menu yang dipilih adalah (l/L) maka akan masuk ke Daftar Mahasiswa
```python
# Lihat Data {
elif menu == 'L' or menu == 'l':
```

2. Percabangan apabila data tidak ada maka akan tampil "TIDAK ADA DATA"
```python
print("Daftar Mahasiswa")
if len(Data_Mahasiswa) <= 0:  
   header()          
   print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
   garis()
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
