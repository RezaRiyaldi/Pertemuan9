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