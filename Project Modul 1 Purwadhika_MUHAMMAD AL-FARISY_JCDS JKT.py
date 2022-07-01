print("Nama    : MUHAMMAD AL-FARISY")
print("Kelas   : JCDS April - Agustus 2022")

stock_Gudang = [
    {'KODE':'CT 756','NAMA PRODUK':'MAGNIFICA ECM','MERK':'DELONGHI','WARNA':'HITAM','STOCK':10,'HARGA':19450000},
    {'KODE':'CT WE8','NAMA PRODUK':'JURA WE8','MERK':'JURAA','WARNA':'HITAM','STOCK':20,'HARGA':8450000},
    {'KODE':'CT AE8','NAMA PRODUK':'PIANINT','MERK':'JURAA','WARNA':'HITAM','STOCK':30,'HARGA':37400000},
    {'KODE':'CT 8G2','NAMA PRODUK':'JURA GIGA','MERK':'JURAA','WARNA':'HITAM','STOCK':25,'HARGA' : 161150000},
    {'KODE':'CT ZX8','NAMA PRODUK':'Z8 ALUMUNIUM','MERK':'JURAA','WARNA':'HITAM','STOCK':18,'HARGA':85800000},
    {'KODE':'CT M73','NAMA PRODUK':'MESIN KAPSUL','MERK':'JURAA','WARNA':'WHITE','STOCK' : 2,'HARGA':7350000},
    {'KODE':'CT 717','NAMA PRODUK':'CAPPUCINO 717','MERK':'JURAA','WARNA':'MERAH','STOCK':50,'HARGA':7950000},
    {'KODE':'CT S8A','NAMA PRODUK':'JURAS8899','MERK':'JURAA','WARNA':'WHITE','STOCK' : 9,'HARGA':35000000},
    {'KODE':'CT Z6A','NAMA PRODUK':'JURAZ61AL','MERK':'JURAA','WARNA':'MERAH','STOCK':8,'HARGA':80000000},
    {'KODE':'CT 215','NAMA PRODUK':'OXONE215','MERK':'JURAA','WARNA':'MERAH','STOCK':5,'HARGA':120000000}]


#Menu Awal
def menu_awal():
    a = 0
    while a < 1:
        print("\n\t\t\t\t\tSELAMAT DATANG DI ACEH COFFEE TOOLS\n\t\t\t\t\t")
        print("Pilihan Menu Aplikasi : ")
        print("\t\t\t\t\t1. Daftar Data Persediaan Barang")
        print("\t\t\t\t\t2. Menambah Data Persediaan Barang")
        print("\t\t\t\t\t3. Update Data Persediaan Barang")
        print("\t\t\t\t\t4. Menghapus Data Persediaan Barang")
        print("\t\t\t\t\t5. Exit")
        
        menu_input = str(input("Masukan Pilihan Anda [1-5] : ").upper())

        if menu_input == '1':
            menu_daftar_persediaan_barang()
        
        elif menu_input == '2':
            menu_membuat_data_baru()
            
        elif menu_input == '3':
            menu_update_data()    

        elif menu_input == '4':
            menu_menghapus_data()   

        elif menu_input == '5':
            print("END")
            break

        else:
            print("\n**Pilihan Yang Anda Masukan Salah**")

### . 1. Daftar Data Persediaan Barang
def menu_daftar_persediaan_barang():
    b = 0
    while b < 1:
        print("\n\t\t\t\t\t1. Data Persediaan (Seluruh) ")
        print("\t\t\t\t\t2. Data Persediaan (Tertentu) ")
        print("\t\t\t\t\t3. Kembali Ke Menu Utama\n")
        tanya = str(input("Masukan Pilihan Menu [1-3] : ").upper())
        if tanya == '1':
            seluruh_data_persediaan()
        elif tanya == '2':
            data_tertentu()
        elif tanya == '3':
            break
        else:
            print("\n**Pilihan Yang Anda Masukan Salah**")

def seluruh_data_persediaan():
    print("\n\t\t\t\t\tStock tersedia di Gudang : ")
    print("--------------------------------------------------------------------------------------------------------------")
    print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
    if stock_Gudang != 0:
        for c in range(len(stock_Gudang)) :
            daftar_data_persediaan(c)
            continue
    else :
        print("\n**Tidak Ada Data*")

def data_tertentu():
    katakunci = str(input("Masukan KODE PRODUK : ").upper())
    for d in range(len(stock_Gudang)):
        if katakunci == stock_Gudang[d]['KODE']:
            print("--------------------------------------------------------------------------------------------------------------")
            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
            daftar_data_persediaan(d)
            break
    else:
        print("\n**Tidak Ada Data**")

def daftar_data_persediaan(z):
    print("--------------------------------------------------------------------------------------------------------------")
    print(" {}\t| {}\t| {}\t | {}\t| {}\t\t| {}\t\t|  {}\t".format(z,stock_Gudang[z]['KODE'],stock_Gudang[z]['NAMA PRODUK'],stock_Gudang[z]['MERK'],stock_Gudang[z]['WARNA'],stock_Gudang[z]['STOCK'],stock_Gudang[z]['HARGA']))


### 2. Menambah Data Persediaan Barang
def menu_membuat_data_baru():
    e = 0
    while e < 1:
        print("\n\t\t\t\t\t1. Membuat Data Persediaan Baru")
        print("\t\t\t\t\t2. Menu Utama\n")
        tanya = str(input("Masukan Pilihan Menu [1-2] : ").upper())
        if tanya == '1' :
            simpan_data_baru()
        elif tanya == '2':
            break
        else:
            print("\n**Pilihan Yang Anda Masukan Salah**")    

def simpan_data_baru():
    cek_data_barang = str(input("Masukan KODE PRODUK untuk di Cek : ").upper())
    for f in range(len(stock_Gudang)):
        if cek_data_barang == stock_Gudang[f]['KODE']:
            print(f"\nStock Barang Dengan Kode {cek_data_barang} Sudah Ada")
            break
        elif f == len(stock_Gudang)-1:
            print(f"\nKODE {cek_data_barang} belum ada\n")
            print("Silahkan Input Kelengkapan Data Persediaan\n")
            input_kode_produk = str(input("Masukan KODE PRODUK\t\t: ").upper())
            input_nama_produk = str(input("Masukan NAMA PRODUK\t\t: ").upper())                
            input_merk_produk = str(input("Masukan MERK PRODUK\t\t: ").upper())
            input_warna_produk = str(input("Masukan WARNA PRODUK\t\t: ").upper())
            input_stock_produk = int(input("Masukan STOCK PRODUK (ANGKA)\t: "))
            input_harga_produk = int(input("Masukan HARGA PRODUK (ANGKA)\t: "))
            print("------------------------------------------------------------------------------------------------------------")
            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
            print("------------------------------------------------------------------------------------------------------------")
            print(" {}\t| {}\t| {}\t  | {}\t| {}\t\t| {}\t| {}\t".format(1,input_kode_produk,input_nama_produk,input_merk_produk,input_warna_produk,input_stock_produk,input_harga_produk))
            g = 0
            while g < 1:
                tanya = str(input("\n\tApakah Anda Ingin Menyimpan Data di Atas ? (Y/T) : ").upper())
                if tanya == "Y":
                    stock_Gudang.append({'KODE': input_kode_produk,'NAMA PRODUK': input_nama_produk,'MERK': input_merk_produk,'WARNA': input_warna_produk,'STOCK': input_stock_produk,'HARGA': input_harga_produk})
                    print("\n\tData Berhasil Di Simpan")
                    break
                elif tanya == "T":
                    print("\nData Batal Di Simpan")
                    break
                else:
                    print("\n**Pilihan Yang Anda Masukan Salah**")


# ### 3. Update Data Persediaan Barang
def menu_update_data():
    h = 0
    while h < 1:
        print("\n\t\t\t\t\t1. Mengedit Data Persediaan")
        print("\t\t\t\t\t2. Menu Utama\n")
        tanya = str(input("Masukan Pilihan Menu [1-2] : ").upper())
        if tanya == '1' :
            updatedataterbaru()
        elif tanya == '2':
            break
        else:
            print("\n**Pilihan Yang Anda Masukan Salah**")
    
def updatedataterbaru():
        katakunci = str(input("Masukan KODE PRODUK yang akan di Update : ").upper())
        for i in range(len(stock_Gudang)):
            if katakunci == stock_Gudang[i]['KODE']:
                print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t|  HARGA\t")
                daftar_data_persediaan(i)
                while True:
                    print("\n\t\t\t\t\tPilihan Menu Yang Mau Di Update")
                    print("\t\t\t\t\t1. Update Data Kode Barang")
                    print("\t\t\t\t\t2. Update Nama Barang")
                    print("\t\t\t\t\t3. Update Merk Barang")
                    print("\t\t\t\t\t4. Update Warna Barang")
                    print("\t\t\t\t\t5. Update Stock Barang")
                    print("\t\t\t\t\t6. Update Harga Barang")
                    print("\t\t\t\t\t7. Kembali Ke Menu Sebelumnya")
                    
                    tanya = str(input("Masukan Pilihan Menu [1-7]: "))
                    
                    if tanya == '1':
                        konfirmasi = str(input("Apakah anda Yakin Mengupdate Data (Y/T) : ").upper())
                        if konfirmasi == "Y":
                            stock_Gudang[i]["KODE"] = str(input("Input KODE Baru : ").upper())
                            print("\n**KODE BERHASIL DI UPDATE**\n")
                            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                            daftar_data_persediaan(i)
                        elif konfirmasi == "T":
                            continue
                        else:
                            print("\n**Pilihan Yang Anda Masukan Salah**")
                            
                                         
                    elif tanya == '2':
                        konfirmasi = str(input("Apakah anda Yakin Mengupdate Data (Y/T) : ").upper())
                        if konfirmasi == "Y":
                            stock_Gudang[i]["NAMA PRODUK"] = str(input("Input NAMA PRODUK Baru : ").upper())
                            print("\n**KODE BERHASIL DI UPDATE**\n")
                            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                            daftar_data_persediaan(i)
                        elif konfirmasi == "T":
                            continue   
                        else:
                            print("\n**Pilihan Yang Anda Masukan Salah**")
                            
                    elif tanya == '3':
                        konfirmasi = str(input("Apakah anda Yakin Mengupdate Data (Y/T) : ").upper())
                        if konfirmasi == "Y":
                            stock_Gudang[i]["MERK"] = str(input("Input MERK PRODUK Baru : ").upper())
                            print("\n**KODE BERHASIL DI UPDATE**\n")
                            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                            daftar_data_persediaan(i)
                        elif konfirmasi == "T":
                            continue   
                        else:
                            print("\n**Pilihan Yang Anda Masukan Salah**")
                            
                            
                    elif tanya == '4':
                        konfirmasi = str(input("Apakah anda Yakin Mengupdate Data (Y/T) : ").upper())
                        if konfirmasi == "Y":
                            stock_Gudang[i]["WARNA"] = str(input("Input WARNA PRODUK Baru : ").upper())
                            print("\n**KODE BERHASIL DI UPDATE**\n")
                            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                            daftar_data_persediaan(i)
                        elif konfirmasi == "T":
                            continue   
                        else:
                            print("\n**Pilihan Yang Anda Masukan Salah**")  
                            
                            
                    elif tanya == '5':
                        konfirmasi = str(input("Apakah anda Yakin Mengupdate Data (Y/T) : ").upper())
                        if konfirmasi == "Y":
                            stock_Gudang[i]["STOCK"] = str(input("Input STOCK PRODUK Baru : ").upper())
                            print("\n**KODE BERHASIL DI UPDATE**\n")
                            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                            daftar_data_persediaan(i)
                        elif konfirmasi == "T":
                            continue   
                        else:
                            print("\n**Pilihan Yang Anda Masukan Salah**")
                            
                    elif tanya == '6':
                        konfirmasi = str(input("Apakah anda Yakin Mengupdate Data (Y/T) : ").upper())
                        if konfirmasi == "Y":
                            stock_Gudang[i]["HARGA"] = str(input("Input HARGA PRODUK Baru : ").upper())
                            print("\n**KODE BERHASIL DI UPDATE**\n")
                            print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                            daftar_data_persediaan(i)
                        elif konfirmasi == "T":
                            break   
                        else:
                            print("\n**Pilihan Yang Anda Masukan Salah**")                        
     
                    elif tanya == '7':
                        break
                break
        
            elif i == len(stock_Gudang)-1:
                print("**Data Yang Anda Cari Tidak Ada**")
                break
                    
                
### 4. Menghapus Data Persediaan Barang
def menu_menghapus_data():
    j = 0
    while j < 1:
        print("\t\t\t\t\t1. Menghapus Data")
        print("\t\t\t\t\t2. Kembali Ke Menu Utama")
        tanya = str(input("Masukan Pilihan Anda : ").upper())
        if tanya == '1':
            hapus_data()
        elif tanya == '2':
            break
        else:
            print("\n**Pilihan Yang Anda Masukan Salah**")

def hapus_data():
        print("\n**Silahkan Input KODE Data Yang Ingin Anda Hapus**\n ")
        katakunci = str(input("Masukan KODE / PRIMARY KEY Yang Akan Anda Hapus : ").upper())
        for k in range(len(stock_Gudang)):
            if katakunci == stock_Gudang[k]["KODE"]:
                print("Data Yang Akan Di Hapus :")
                print(" Nomor\t| KODE\t \t| NAMA PRODUK\t | MERK\t \t| WARNA\t\t| STOCK\t\t| HARGA\t")
                daftar_data_persediaan(k)
                konfirmasi = str(input("Apakah Anda Yakin Ingin Menghapus Data ? (Y/T): ").upper())
                if konfirmasi == "Y":
                    del stock_Gudang[k]
                    print(f"\n**DATA KODE {katakunci} BERHASIL DI HAPUS**")
                    break
                    
                elif konfirmasi == "T" and konfirmasi != "Y":
                    print("\n**Data Batal Di Hapus**")
                    break
                else:
                    print("\n**Pilihan Yang Anda Masukan Salah**")
                    break
                
        else:
            print("Data Yang Anda Cari Tidak Ada")
 
menu_awal()