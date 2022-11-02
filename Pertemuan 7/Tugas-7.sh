#!/bin/bash

# mendeklarasikan fungsi
panjang() {
        echo "Masukan PAnjang :"
        read p

}
lebar() {
        echo "Masukan Lebar :"
        read l

}
luas() {
       echo "Menghitung Luas Bidang Persegi"
       panjang
       lebar
       let l=$p*$l
       echo "Luas Persegi :
$l"
}

# memanggil fungsi
luas

