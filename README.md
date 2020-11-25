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
         * [Dictionary dan Variable](https://github.com/RezaRiyaldi/Pertemuan9/#--membuat-dictionary-sebagai-databasenya)
         * [Function Tambahan](https://github.com/RezaRiyaldi/Pertemuan9/#--membuat-function-tambahan-agar-bisa-dipanggil-ketika-dibutuhkan)
         * [Function Tambah Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-tambah-data)
         * [Function Lihat Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-lihat-data)
         * [Function Ubah Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-ubah-data)
         * [Function Hapus Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-hapus-data)
         * [Function Cari Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-cari-data)  
         * [Menu](https://github.com/RezaRiyaldi/Pertemuan9/#menu)         
        
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
_nama = []
_nim = []
_nilaiTugas = []
_nilaiUTS = []
_nilaiUAS = []
_nilaiAkhir = []
```

2. Membuat program _infinite loop_ (loop tak terbatas)
```python
while True:
```

3. Pada program inputan langsung ditambahkan ke _LIST_ dengan method `.append`, sedangkan untuk nilai(Tugas, UTS, UAS) dimasukan ke variable terlebih dahulu untuk perhitungan nilai akhir
```python
_nama.append(input("Masukan nama : "))
_nim.append(input("Masukan NIM  : "))
nilaiTugas = int(input("Nilai tugas  : ")); _nilaiTugas.append(nilaiTugas)
nilaiUTS   = int(input("Nilai UTS    : ")); _nilaiUTS.append(nilaiUTS)
nilaiUAS   = int(input("Nilai UAS    : ")); _nilaiUAS.append(nilaiUAS)

_nilaiAkhir.append(nilaiTugas * 30/100 + nilaiUTS * 35/100 + nilaiUAS * 35/100)
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
for nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir in zip(_nama, _nim, _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir):
```

7. Membuat isi table sesuai dengan inisialisi diatas, dengan format string agar terlihat rapih
```python
no += 1
print("| {0:>2} | {1:<18} | {2:>7} | {3:>5} | {4:>5} | {5:>5} | {6:>7.2f} |".format(no, nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir))
```

8. Untuk membuat garis paling bawah ketika looping isi table selesai
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

#### Membuat Function dan Deklarasi Variable
##### - Membuat Dictionary sebagai Databasenya
```python
# Deklarasi Variable
Data_Mahasiswa = {} 
loop = True
```

##### - Membuat Function tambahan agar bisa dipanggil ketika dibutuhkan
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
    
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

##### - Function Tambah Data
1. Program Tambah Data dijalankan
- Memasukan data
- Jika sudah, maka data akan dimasukkan kedalam `Dict Data_Mahasiswa`
- Dimana Nama sebagai `key` dan sisanya `values` yang dimasukkan kedalam `list`
- Jika berhasil maka akan mengeluarkan "Berhasil menambahkan data '`nama`' dengan NIM : `nim`!"
```python
def tambah():
    print("Tambah data")
    nim        = input("NIM         : ")
    nama       = input("Nama        : ")
    nilaiTugas = int(input("Nilai Tugas : "))
    nilaiUTS   = int(input("Nilai UTS   : "))
    nilaiUAS   = int(input("Nilai UAS   : "))
    nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
    Data_Mahasiswa[nama] = [nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]
    print(f"Berhasil menambahkan data '{nama}' dengan NIM : {nim}!")
```
Maka program cari data akan seperti berikut.

![tambah](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/Output-tambah.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

##### - Function Lihat Data
1. Apabila `Dict Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
```python
def lihat():
    print("Daftar Mahasiswa")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
```
Seperti gambar berikut.

![takda-l](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output_lihat-1.PNG)

2. Program Lihat Data Dijalankan
- Menggunakan looping untuk mengeluarkan data
- Dan menggunakan `f-string` agar tidak terlalu panjang dan `format.string` agar tampilan terlihat rapih
```python
else:
     no = 0
     header()
     for data in Data_Mahasiswa.items():
         no += 1 
         print(f"| {no:>2} | {data[1][0]:>7} | {data[0]:<18} | {data[1][1]:>5} | {data[1][2]:>5} | {data[1][3]:>5} | {data[1][4]:>7.2f} |")               
     garis() 
```
Maka program cari data akan seperti berikut.

![lihat](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output_lihat-2.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

##### - Function Ubah Data
1. Apabila `Dict Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
```python
def ubah():
    print("Ubah Data Mahasiswa berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
```
Seperti gambar berikut.

![takda-u](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-1.PNG)

2. Program ubah data dijalankan
- Memasukan nama sebagai `key` dan akan memunculkan isi data dari `key` tersebut
- Jika salah memasukkan nama, maka akan mengeluarkan "data `nama` tidak ditemukan!"
- Selanjutnya akan diberi pilihan apa yang ingin diubah, jika ingin membatalkan maka ketik `0`
- Jika salah memasukkan pilihan maka mengeluarkan "Pilihan `input` tidak ada! Silahkan masukan [1-3]"
```python
else:
   nama = str(input("Masukan nama : ")) 
   if nama in Data_Mahasiswa.keys():
      print(f"Nama        = {nama}")
      print(f"NIM         = {Data_Mahasiswa[nama][0]}")
      print(f"Nilai Tugas = {Data_Mahasiswa[nama][1]}")
      print(f"Nilai UTS   = {Data_Mahasiswa[nama][2]}")
      print(f"Nilai UAS   = {Data_Mahasiswa[nama][3]}")
      print(25*"=")
      print("1. Nama\n2. NIM\n3. Nilai\n0. Kembali")
      tanya = int(input("Apa yang ingin diubah? [1-3] : "))
      ...      
      elif tanya == 0:
          pass
          
      else:
          print(f"Pilihan {tanya} tidak ada! Silahkan masukan [1-3]")
   else:
      print(f"Data {nama} tidak ditemukan!") 
```
Maka program akan seperti berikut.

![ubah-2](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-3.PNG)

3. Ubah Nama
- Memasukan nama baru, nama akan berubah, maka akan mengeluarkan "Berhasil merubah Nama!"
```python
if tanya == 1:
    _nama = input("Masukan Nama Baru : ")
    Data_Mahasiswa[_nama] = Data_Mahasiswa.pop(nama)
    print("Berhasil merubah Nama! ")
```
Maka program ubah nama akan seperti berikut.

![ubah-nama](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-nama.PNG)

4. Ubah NIM
- Memasukan NIM baru, NIM akan berubah, maka akan mengeluarkan "Berhasil merubah NIM!"
```python
elif tanya == 2:
    _nim = input("Masukan Nim Baru : ")
    Data_Mahasiswa[nama][0] = _nim
    print("Berhasil merubah NIM!")
```
Maka program ubah Nim akan seperti berikut.

![ubah-nim](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-NIM.PNG)

5. Ubah Nilai
- Memasukan nilai baru, nilai akan berubah, maka akan mengeluarkan "Berhasil merubah data nilai!"
```python
elif tanya == 3:
    _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
    _nilaiUTS = int(input("Masukan Nilai UTS Baru : "))
    _nilaiUAS = int(input("Masukan Nilai UAS Baru : "))
    _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
    Data_Mahasiswa[nama][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
    print("Berhasil merubah data nilai!")
```
Maka program ubah Nilai akan seperti berikut.

![ubah-nilai](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-ubah-nilai.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

##### - Function Hapus Data
1. Apabila `Dict Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
```python
def hapus():
    print("Hapus Data Mahasiswa berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
```

Seperti gambar berikut.

![takda-h](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-hapus-1.PNG)

2. Program Hapus Data Dijalankan
- Memasukan nama sebagai `key` data yang ingin dihapus
- Jika salah memasukan nama ,maka akan mengeluarkan "data `nama` tidak ditemukan!"
```python
else:
     nama = str(input("Masukan nama : "))
     if(nama in Data_Mahasiswa):
         del Data_Mahasiswa[nama]
         print(f"Data {nama} berhasil dihapus!")
     else:
         print(f"Data {nama} tidak ditemukan!") 
```
Maka program Hapus Data akan seperti berikut.

![hapus](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-hapus-2.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

##### - Function Cari Data
1. Apabila `Dict Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
```python
def cari():
    print("Cari Data Mahasiswa berdasarkan nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
```

Seperti gambar berikut.

![takda-c](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-cari-1.PNG)

2. Program Cari Data Dijalankan
- Memasukan nama sebagai `key` data yang ingin dicari
- Jika salah memasukan nama ,maka akan mengeluarkan "data `nama` tidak ditemukan!"
- Ketika nama sudah benar maka akan muncul data yang dicari
```python
else:
     nama = input("Masukan nama : ")
     if(nama in Data_Mahasiswa):
         no = 1            
         print(f"\nNama        = {nama}")
         print(f"NIM         = {Data_Mahasiswa[nama][0]}")
         print(f"Nilai Tugas = {Data_Mahasiswa[nama][1]}")
         print(f"Nilai UTS   = {Data_Mahasiswa[nama][2]}")
         print(f"Nilai UAS   = {Data_Mahasiswa[nama][3]}")                  
         print(f"Nilai Akhir = {Data_Mahasiswa[nama][4]}")        
     else:
         print(f"Data {nama} tidak ditemukan!") 
```
Maka program Cari data akan seperti berikut.

![cari](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/gambar/output-cari-2.PNG)

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)

##### Menu 
1. Program menu dijalankan
- Menggunakan _infinite loop_ sampai loopnya jadi false
- Apabila salah memasukkkan inputan maka akan muncul "Menu '`menu`' tidak ada! Silahkan masukan [T/L/U/H/C/K]"
- Jika benar maka function yang sudah dibuat akan dijalankan
```python
while loop: 
    print()
    menu = input("[(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar] : ")
    print(71*"-")
    print()

    if menu == 'T' or menu == 't':
        tambah()

    elif menu == 'L' or menu == 'l':
        lihat()       

    elif menu == "U" or menu == "u":
        ubah() 

    elif menu == "H" or menu == "h":
        hapus()

    elif menu == "C" or menu == "c":
        cari() 

    elif menu == "K" or menu == "k":
        print("Program selesai, Terima Kasih")
        loop = False 

    else:
        print(f"Menu '{menu}' tidak ada! Silahkan masukan [T/L/U/H/C/K]")
```

[Kembali ke Daftar Isi](https://github.com/RezaRiyaldi/Pertemuan9#daftar-isi)
