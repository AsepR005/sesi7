# 1. Menerima input dari pengguna
angka = int(input("Masukkan bilangan bulat positif: "))

# 2. Menghitung jumlah dari digit-digit bilangan
jumlah_digit = sum(int(digit) for digit in str(angka))

# 3. Menentukan apakah habis dibagi jumlah digit
if angka % jumlah_digit == 0:
    print("Bilangan ini spesial.")
else:
    print("Bilangan ini tidak spesial.")
