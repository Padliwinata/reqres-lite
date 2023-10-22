import requests
import json

# Note :
# Daftar/login menggunakan list email berikut atau register akan failed:
# george.bluth@reqres.in, janet.weaver@reqres.in, emma.wong@reqres.in, eve.holt@reqres.in, charles.morris@reqres.in
# tracey.ramos@reqres.in, michael.lawson@reqres.in, lindsay.ferguson@reqres.in, tobias.funke@reqres.in, byron.fields@reqres.in
# george.edwards@reqres.in, rachel.howell@reqres.in
# ----------------------------------
# GUNAKAN NIM ANDA SEBAGAI PASSWORD
# ----------------------------------

def display_user(): # (15)
    # I.S -
    # F.S Menampilkan seluruh data user dalam bentuk list yang diiterasi
    
def get_user(id): # (10)
    # I.S id user yang akan ditampilkan
    # F.S Menampilkan data satu user yang diminta, dan print "Data tidak ditemukan" apabila user tidak ditemukan

def register(email, password) -> int: # (15)
    # I.S email dan password yang akan diregister
    # F.S kode status response apabila user sukses diregister (200 / HTTP OK)

def login(email, password) -> int: # (15)
    # I.S email dan password yang akan login
    # F.S kode status response apabila user sukses login (200 / HTTP OK)
    
def edit_user(name): # (15)
    # I.S nama user baru untuk user yang login
    # F.S tampilkan "Sukses edit!" apabila edit nama berhasil (200 / HTTP OK), atau print error jika tidak
    
def delete_user(id): # (15)
    # I.S id user yang akan dihapus (1 - 12)
    # F.S tampilkan "Sukses terhapus!" apabila data sukses terhapus (204 / HTTP NO CONTENT), atau print error jika tidak
    if resp.status_code == 204:
        # Print sukses 

def show_menu(): # (5)
    # I.S -
    # F.S tampilkan menu sederhana untuk menampilkan pilihan yang bisa dilakukan user
    choose = 1
    while 1 <= choose <= 4: 
        print("Menu admin sederhana")
        print("---------------------------------------")
        print("1. Tampilkan Semua User")
        print("2. Tampilkan Satu User")
        print("3. Ubah Nama Anda")
        print("4. Hapus User")
        print("---------------------------------------")
        choose = int(input("Masukkan pilihan anda: "))
        if choose == 1:
            # Jalankan fungsi display user
        elif choose == 2:
            id_input = input("Masukkan id user yang ingin ditampilkan: ")
            # Jalankan fungsi get user
        elif choose == 3:
            new_name = input("Masukkan nama baru: ")
            # Jalankan fungsi edit user
        elif choose == 4:
            del_user = input("Masukkan id user yang akan dihapus: ")
            # Jalankan fungsi delete user
        else:
            print("Keluar dari aplikasi...")

def login_menu(): # (5)
    # I.S -
    # F.S tampilkan input sederhana untuk input email dan password untuk masuk kedalam aplikasi
    success = False
    while not success:
        print("Masuk ke reqres")
        print("---------------------------------------")
        email = input("Email : ")
        password = input("Password : ")
        # Jalankan fungsi login
        # if salah:
            print("Masukkan password dan gunakan email yang sudah terdaftar")
        # else:
            print("Login sukses!")
            success = True
            show_menu()

def register_menu(): #(5)
    # I.S -
    # F.S tampilkan input sederhana untuk input email dan password untuk register kedalam aplikasi
    success = False
    while not success:
        print("Daftar ke reqres")
        print("---------------------------------------")
        email = input("Email : ")
        password = input("Password : ")
        check = register(email, password)
        # Jalankan fungsi register
        # if salah:
            print("Masukkan password dan gunakan email yang sudah terdaftar")
        # else:
            print("Login sukses!")
            success = True
            show_menu()

def main_menu():
    print("Praktikum HTTP API")
    print("NAMA : -")
    print("NIM  : -")
    print("---------------------------------------")
    print("1. Login")
    print("2. Register")
    print("---------------------------------------")
    pilihan = int(input("Masukkan pilihan anda : "))
    if pilihan == 1:
        login_menu()
    else:
        register_menu()

main_menu()