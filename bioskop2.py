# Data film dan harga
film_list = [
    {"nama": "Spider-Man", "harga": 45000},
    {"nama": "Avengers", "harga": 50000},
    {"nama": "Toy Story", "harga": 40000}
]

# Program utama
while True:
    print("\n=== Menu Bioskop ===")
    print("1. " + film_list[0]["nama"])
    print("2. " + film_list[1]["nama"])
    print("3. " + film_list[2]["nama"])
    print("4. Selesai")

    pilihan = input("Pilih nomor film (1-4): ")

    if pilihan == "1" or pilihan == "2" or pilihan == "3":
        index = int(pilihan) - 1
        print("Film yang dipilih: " + film_list[index]["nama"])
        print("Harga tiket: Rp" + str(film_list[index]["harga"]))
    elif pilihan == "4":
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia. Coba lagi.")
