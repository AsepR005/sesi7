def menu_utama():
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Daftar Film")
        print("2. Pembelian Tiket")
        print("3. Quit")
        pilih = input("Pilih menu: ")

        if pilih == '1':
            daftar_film()
        elif pilih == '2':
            pembelian_tiket()
        elif pilih == '3':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

def daftar_film():
    print("\n=== DAFTAR FILM ===")
    print("1. Avengers")
    print("2. Fast and Furious")
    print("3. Transformers")
    input("Tekan Enter untuk kembali...")

def pembelian_tiket():
    print("\n=== PEMBELIAN TIKET ===")
    nama = input("Nama Anda: ")
    print("Pilih film:")
    print("1. Avengers")
    print("2. Fast and Furious")
    print("3. Transformers")
    film = input("Pilihan (1-3): ")

    if film == '1':
        film_nama = "Avengers"
    elif film == '2':
        film_nama = "Fast and Furious"
    elif film == '3':
        film_nama = "Transformers"
    else:
        print("Pilihan film tidak valid.")
        return

    jumlah = input("Jumlah tiket: ")
    if not jumlah.isdigit():
        print("Jumlah tiket harus angka.")
        return

    jumlah = int(jumlah)
    total = jumlah * 25000

    print("\nNama:", nama)
    print("Film:", film_nama)
    print("Jumlah tiket:", jumlah)
    print("Total harga: Rp" + str(total).replace(",", "."))

menu_utama()