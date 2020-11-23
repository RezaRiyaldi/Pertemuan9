class Mahasiswa:
    # Inisialisasi/Memasukan data inputan ke Dictionary
    def __init__(self, _nama, _nim, _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir):
        self.nama       = str(_nama) 
        self.nim        = str(_nim) 
        self.nilaiTugas = int(_nilaiTugas)
        self.nilaiUTS   = int(_nilaiUTS)
        self.nilaiUAS   = int(_nilaiUAS)
        self.nilaiAkhir = float(_nilaiAkhir)

    # Untuk merubah data dari Dictionary Data_Mahasiswa
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

    # Menampilkan/mengambil data dari dictionary
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

# Program
print(23*"=")
print("= Program Input Nilai =")
print(23*"=")

while loop: 
    print()
    menu = input("[(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar] : ")
    print(71*"-")
    print()
    
    # Tambah Data {
    if menu == 'T' or menu == 't':
        print("Tambah data")
        nim        = input("NIM         : ")
        nama       = input("Nama        : ")
        nilaiTugas = int(input("Nilai Tugas : "))
        nilaiUTS   = int(input("Nilai UTS   : "))
        nilaiUAS   = int(input("Nilai UAS   : "))
        nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
        mhs = Mahasiswa(nama, nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir) 
        Data_Mahasiswa[nim] = mhs 
    # }

    # Lihat Data {
    elif menu == 'L' or menu == 'l':
        print("Daftar Mahasiswa")
        if len(Data_Mahasiswa) <= 0:  
            header()          
            print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
            garis()
        else:
            no = 0
            header()
            for i in Data_Mahasiswa:
                no += 1 
                L_Data = Data_Mahasiswa[i]
                print(f"| {no:>2} | {L_Data.getNim():>7} | {L_Data.getNama():<18} | {L_Data.getNilaiTugas():>5} | {L_Data.getNilaiUTS():>5} | {L_Data.getNilaiUAS():>5} | {L_Data.getNilaiAkhir():>7.2f} |")                
            garis()        
    # }

    # Ubah Data {
    elif menu == "U" or menu == "u":
        print("Ubah Data Mahasiswa berdasarkan NIM")
        if len(Data_Mahasiswa) <= 0:  
            header()          
            print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
            garis()

        else:
            nim = str(input("Masukan nim : ")) 
            if(nim in Data_Mahasiswa):
                U_data = Data_Mahasiswa[nim]
                print(f"Nama        = {U_data.getNama()}")
                print(f"NIM         = {U_data.getNim()}")
                print(f"Nilai Tugas = {U_data.getNilaiTugas()}")
                print(f"Nilai UTS   = {U_data.getNilaiUTS()}")
                print(f"Nilai UAS   = {U_data.getNilaiUAS()}")
                print(25*"=")
                print("1. Nama\n2. NIM\n3. Nilai")
                tanya = int(input("Apa yang ingin diubah? [1-3] : "))
                if tanya == 1:
                    namaBaru = str(input("Masukan Nama Baru : ")) 
                    U_data.setNama(namaBaru) 

                elif tanya == 2:
                    nimBaru = str(input("Masukan Nim Baru : ")) 
                    Data_Mahasiswa[nim].setNim(nimBaru) 
                    mhs = Data_Mahasiswa[nim] 
                    Data_Mahasiswa[nimBaru] = mhs 
                    del Data_Mahasiswa[nim] 

                elif tanya == 3:
                    nilaiTugasBaru = int(input("Masukan Nilai Tugas Baru : "))
                    nilaiUTSBaru = int(input("Masukan Nilai UTS Baru : "))
                    nilaiUASBaru = int(input("Masukan Nilai UAS Baru : "))
                    U_data.setNilaiTugas(nilaiTugasBaru)
                    U_data.setNilaiUTS(nilaiUTSBaru)
                    U_data.setNilaiUAS(nilaiUASBaru)
                    nilaiAkhirBaru = nilaiTugasBaru * 30/100 + nilaiUTSBaru * 35/100 + nilaiUASBaru * 35/100
                    U_data.setNilaiAkhir(nilaiAkhirBaru)

                else:
                    print("Pilihan yang anda masukan tidak ada!")

            else:
                print("Data tidak ditemukan!!!") 
    # }

    # Hapus Data {
    elif menu == "H" or menu == "h":
        print("Hapus Data Mahasiswa berdasarkan NIM")
        if len(Data_Mahasiswa) <= 0:  
            header()          
            print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
            garis()

        else:
            nim = str(input("Masukan NIM : "))
            if(nim in Data_Mahasiswa):
                del Data_Mahasiswa[nim] 
            else:
                print("Data tidak ditemukan!!!") 
    # }

    # Cari Data {
    elif menu == "C" or menu == "c":
        print("Cari Data Mahasiswa berdasarkan NIM")
        if len(Data_Mahasiswa) <= 0:  
            header()          
            print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
            garis()
        else:
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
    # }

    # Keluar {
    elif menu == "K" or menu == "k":
        print("Selesai")
        loop = False 
    # }

    else:
        print("Menu tidak ada atau anda salah memasukan nilai!") 