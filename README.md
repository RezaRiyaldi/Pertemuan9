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
Konsep Program:
- Progam meminta memasukkan data sebanyak-banyaknya (gunakan perulangan)
- Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban t (Tidak), maka program akan menampilkan daftar datanya.
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)

Berikut [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy04/labs04.py)-nya
```python
# LIST
namaMahasiswa = []
nimMahasiswa = []
nilaiTugasMahasiswa = []
nilaiUTSMahasiswa = []
nilaiUASMahasiswa = []

# Input
while True:
    namaMahasiswa.append(input("Masukan nama : "))
    nimMahasiswa.append(int(input("Masukan NIM  : ")))
    _nilaiTugas = int(input("Nilai tugas  : ")); nilaiTugasMahasiswa.append(_nilaiTugas)
    _nilaiUTS = int(input("Nilai UTS    : ")); nilaiUTSMahasiswa.append(_nilaiUTS)
    _nilaiUAS = int(input("Nilai UAS    : ")); nilaiUASMahasiswa.append(_nilaiUAS)
    print()
    _tanya = input("Tambah data lagi? [y/t]: ")
    print()
    if(_tanya == "t" or _tanya =="T"):
        break

# Output
print(71*"=")
print("| {0:^2} | {1:^18} | {2:^7} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "Nama", "NIM", "Tugas", "UTS", "UAS", "Akhir"))
print(71*"=")

no = 0
for nama, nim, nilaiTugas, nilaiUTS, nilaiUAS in zip(namaMahasiswa, nimMahasiswa, nilaiTugasMahasiswa, nilaiUTSMahasiswa, nilaiUASMahasiswa):
    no += 1    
    tugas = _nilaiTugas * 30/100
    UTS = _nilaiUTS * 35/100
    UAS = _nilaiUAS * 35/100
    nilaiAkhir = tugas + UTS + UAS
    print("| {0:>2} | {1:<18} | {2:>7} | {3:>5} | {4:>5} | {5:>5} | {6:>7.2f} |".format(no, nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir))
print(71*"=")

```

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

Maka Program Seperti berikut.
![Output Labspy04](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy04/gambar/labspy04-output.PNG)

### Labspy 05
