import os
import sys
total = []
def clear_screen():
    os.system('clear' if(os.name=='nt') else 'clear')
def kembali():
    print("\n")
    input("Tekan tombol apa saja untuk kembali")
    clear_screen()
def keluar():
    print("--------------------------------")
    print("** LAKUKAN PEMBAYARAN ! **")
    print("--------------------------------")
    print("Terimakasih Telah Berkunjung :)")
def menu_awal():
    while(True):
        print(" Selamat Datang di Toko 73SpeedShop ")
        print("----------------------------------------------")
        print(" 1 Untuk melihat daftar baut ")
        print(" 2 Untuk melihat daftar perkakas ")
        print(" 3 untuk melihat daftar diskon ")
        print(" 4 Pembayaran ")
        print(" 5 Untuk keluar ")
        try:
            a=int(input("pilih menu 1-5: "))
            print()
            if(a==1):
                daftar_baju()
                kembali()
            elif(a==2):
                daftar_celana()
                kembali()
            elif(a==3):
                daftar_diskon()
                kembali()
            elif(a==4):
                akhir()
                break 
            elif(a==5):
                keluar()
                break
            else:
                print("Masukkan angka 1-5")
                kembali()
                continue
        except ValueError:
            print("masukkan sesuai yang ada di daftar menu !")
            kembali()
            continue
def daftar_baju():
    print(" No | daftar barang | Harga")
    print("--------------------------------------------")
    print(" 1 | baut titanium hijau | 55000")
    print(" 2 | baut titanium bunglon | 110000")
    print(" 3 | baut titanium kuning | 75000")
    print(" 4 | baut titanium gunmetal | 75000")
    print(" 5 | baut titanium blue | 90000")
    print(" 6 | baut titanium polos | 70000")
    print("--------------------------------------------")
    kode=int(input("Masukkan nomor barang : "))
    if(kode==1):
        jumlah1=int(input("Masukkan jumlah barang : "))
        total1=55000*jumlah1
        total.append(total1)
        tanya()
    elif(kode==2):
        jumlah2=int(input("Masukkan jumlah barang : "))
        total2=110000*jumlah2
        total.append(total2)
        tanya()
    elif(kode==3):
        jumlah3=int(input("Masukkan jumlah barang : "))
        total3=75000*jumlah3
        total.append(total3)
        tanya()
    elif(kode==4):
        jumlah4=int(input("Masukkan jumlah barang : "))
        total4=75000*jumlah4
        total.append(total4)
        tanya() (total4)
        tanya()
    elif(kode==5):
        jumlah5=int(input("Masukkan jumlah barang : "))
        total5=90000*jumlah5
        total.append(total5)
        tanya()
    elif(kode==6):
        jumlah6=int(input("Masukkan jumlah barang : "))
        total6=70000*jumlah6
        total.append(total6)
        tanya()
    return
def daftar_celana():
    print(" No | daftar barang | Harga")
    print("--------------------------------------------")
    print(" 1 | kunci T | 130000")
    print(" 2 | kunci inggris | 150000")
    print(" 3 | kunci shock | 120000")
    print(" 4 | kunci L | 100000")
    print(" 5 | kunci kit minni | 30000")
    print("--------------------------------------------")
    kode=int(input("Masukkan nomor barang : "))
    if(kode==1):
        jumlah1=int(input("Masukkan jumlah barang : "))
        total1=130000*jumlah1
        total.append(total1)
        tanya()
    elif(kode==2):
        jumlah2=int(input("Masukkan jumlah barang : "))
        total2=150000*jumlah2
        total.append(total2)
        tanya()
    elif(kode==3):
        jumlah3=int(input("Masukkan jumlah barang : "))
        total3=120000*jumlah3
        total.append(total3)
        tanya()
    elif(kode==4):
        jumlah4=int(input("Masukkan jumlah barang : "))
        total4=100000*jumlah4
        total.append(total4)
        tanya() (total4)
        tanya()
    elif(kode==5):
        jumlah5=int(input("Masukkan jumlah barang : "))
        total5=30000*jumlah5
        total.append(total5)
        tanya()
    return
def daftar_diskon():
    print(" No | jumlah belanja | jumlah diskon ")
    print("--------------------------------------------")
    print(" 1 | > Rp.300000,- | 2% ")
    print(" 2 | > Rp.500000,- | 5% ")
    print(" 3 | > Rp.750000,- | 8% ")
    print(" 4 | > Rp.1000000,- | 10% ")
    print("--------------------------------------------")
def tanya():
    print("\n-----------------------------------")
    tanya = input("Ingin tambah barang? [y/t] : ")
    print("-------------------------------------")
    if(tanya=="y"):
        menu_awal()
    elif(tanya=="t"):
        keluar()
    else:
        print("Pilihan yang anda masukan salah!")
def akhir():
    for harga in total:
        print("SubTotal : ", sum(total))
        diskon=0
        a=sum(total)
        if(a>1000000):
            diskon=a*10/100
        elif(a>750000):
            diskon=a*8/100
        elif(a>500000):
            diskon=a*5/100
        elif(a>300000):
            diskon=a*2/100
        else:
            diskon=0
        print("Potongan Harga : ", diskon)
        totalakhir=a-diskon
        print("Total : ", totalakhir)
        print("-------------------------------")
        bayar=int(input("Jumlah Pembayaran : "))
        kembalian=bayar-totalakhir
        print("Kembalian : ", kembalian)
        print("-------------------------------")
        print(" Terima Kasih ")
        print("-------------------------------")
        break
menu_awal()
