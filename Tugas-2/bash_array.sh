#!/bin/bash

# deklarasi array
distroLinux=("MInt" "Ubuntu" "Kali" "Arch" "Debian")

# random distro
let pilih=$RANDOM%5

# ekspetasi
echo "saya Memilih Distro $pilih, ${distroLinux[$pilih]} !"
