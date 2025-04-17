# Data film
film_list = [
    {"nama": "Spider-Man", "harga": 45000},
    {"nama": "Avengers", "harga": 50000},
    {"nama": "Toy Story", "harga": 40000}
]

# Fungsi menampilkan menu
def tampilkan_menu():
    print("\n=== Menu Bioskop ===")
    for i in range(len(film_list)):
        print(str(i+1) + ". " + film_list[i]["nama"])
    print("4. Selesai")

# Program utama
while True:
    tampilkan_menu()
    pilihan = input("Pilih film (1-4): ")

    if pilihan == "1" or pilihan == "2" or pilihan == "3":
        index = int(pilihan) - 1
        print("Nama film: " + film_list[index]["nama"])
        print("Harga tiket: Rp" + str(film_list[index]["harga"]))
    elif pilihan == "4":
        print("Program selesai. Terima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
