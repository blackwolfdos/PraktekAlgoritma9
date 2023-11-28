def MembuatFile():
    namaf = input("Nama File: ")
    nama = input("Nama Anda: ")
    nim = input("Nim Anda: ")
    tahun = input("Tahun Angkatan: ")
    
    file = open(namaf, "w")
    file.write("nama: "+nama+"\nNim: "+nim+"\nTahun: "+tahun)
    file.close()
    
    print("\nFile Berhasil di buat\n")
    
def MembacaFile():
    namaf = input("Nama File: ")
    file = open(namaf, "r")
    print(file.read())
    file.close()
    
def Menambah():
    namaf = input("Nama File: ")
    sahabat = input("Masukkan Nama Sahabatmu: ")
    note = input("Masukkan Note Tambahan: ")
    
    file = open(namaf, "a")
    file.write("\nNama Sahabat: "+sahabat+"\nNote: "+note)
    file.close()
    
while True:
    print("\n----------File Handling----------")
    print("1. Membuat File Baru")
    print("2. Membaca File")
    print("3. Mengedit File")
    print("9. Keluar")
    pilih = int(input("Pilihan(1/2/3/9): "))

    if pilih == 1:
        MembuatFile()
    elif pilih == 2:
        MembacaFile()
    elif pilih == 3:
        Menambah()
    elif pilih == 9:
        print("Bye Bye :3")
        break