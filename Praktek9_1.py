def FileWrite():
    nama = input("nama kalian: ")
    umur = input("umur kalian: ")
    alamat = input("alamat kalian: ")
    email = input("email kalian: ")
    dosen = input("dosen kalian: ")

    file = open("data.txt", "w")
    file.write("nama: "+ nama +"\n umur: " + umur +"\n alamat:"+ alamat +"\n email:"+ email +"\n dosen:"+ dosen)
    file.close()
    
def FileRead():
    read = open("data.txt", "r")
    text = read.read()
    print("berikut data kamu")
    print(text)
    read.close()
    
    
FileWrite()
FileRead()