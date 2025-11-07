def hitung():
    try:
        angka = int(input("Masukkan Angka: "))
        hasil = 10 / angka
        print("Hasil: ", hasil)
        return hasil
    except ValueError:
        print("inputan bukan angka")
        return 1
    except ZeroDivisionError:
        print("tidak bisa dibagi dengan nol")
        return 0
    finally:
        print("Program jalan")
hitung()
