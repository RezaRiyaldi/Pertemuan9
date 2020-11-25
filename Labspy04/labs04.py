# LIST
_nama = []
_nim = []
_nilaiTugas = []
_nilaiUTS = []
_nilaiUAS = []
_nilaiAkhir = []

# Input
while True:
    _nama.append(input("Masukan nama : "))
    _nim.append(input("Masukan NIM  : "))
    nilaiTugas = int(input("Nilai tugas  : ")); _nilaiTugas.append(nilaiTugas)
    nilaiUTS   = int(input("Nilai UTS    : ")); _nilaiUTS.append(nilaiUTS)
    nilaiUAS   = int(input("Nilai UAS    : ")); _nilaiUAS.append(nilaiUAS)

    _nilaiAkhir.append(nilaiTugas * 30/100 + nilaiUTS * 35/100 + nilaiUAS * 35/100)

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
for nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir in zip(_nama, _nim, _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir):
    no += 1    
    print("| {0:>2} | {1:<18} | {2:>7} | {3:>5} | {4:>5} | {5:>5} | {6:>7.2f} |".format(no, nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir))
print(71*"=")