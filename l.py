def ganti_huruf(kalimat):
    hasil = ""
    for huruf in kalimat:
        if huruf in "Aa":
            hasil += "4"
        elif huruf in "Ee":
            hasil += "3"
        elif huruf in "Uu":
            hasil += "7"
        elif huruf in "Ss":
            hasil += "5"
        else:
            hasil += huruf
    return hasil

# Contoh penggunaan:
input1 = "BELAJAR Pemrograman Python Sangat Mudah sekali"
input2 = "Looping For digunakan ketika sudah diketahui batas Awal dan Batas Akhir"

print("Output 1:", ganti_huruf(input1))
print("Output 2:", ganti_huruf(input2))
