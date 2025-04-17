while True:
    print("\nPilih operasi:")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")
    
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")
    
    if pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator.")
        break
    
    if pilihan not in ['1', '2', '3', '4']:
        print("Pilihan tidak valid, silakan coba lagi.")
        continue
    
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        
        if pilihan == '1':
            hasil = angka1 + angka2
            operasi = "+"
        elif pilihan == '2':
            hasil = angka1 - angka2
            operasi = "-"
        elif pilihan == '3':
            hasil = angka1 * angka2
            operasi = "x"
        elif pilihan == '4':
            hasil = angka1 / angka2
            operasi = "/"
        
        print("Hasil: ", angka1, operasi, angka2, "=", hasil)