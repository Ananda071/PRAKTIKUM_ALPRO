#Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = int(input("Masukkan nilai tugas: "))
nilai_uts = int(input("Masukkan nilai UTS: "))
nilai_uas = int(input("Masukkan nilai UAS: "))
nilai_tugas_akhir = int(input("Masukkan nilai tugas akhir: "))

# Menghitung rata-rata nilai
rata_rata_nilai = (nilai_tugas + nilai_uts + nilai_uas + nilai_tugas_akhir) / 4

# Menentukan nilai berdasarkan ketentuan
if 80 <= rata_rata_nilai <= 100:
    nilai = "A"
elif 70 <= rata_rata_nilai < 80:
    nilai = "B"
elif 60 <= rata_rata_nilai < 70:
    nilai = "C"
elif 40 <= rata_rata_nilai < 60:
    nilai = "D"
elif 0 <= rata_rata_nilai < 40:
    nilai = "E"
else:
    nilai = ("nilai tidak valid")

# Menampilkan hasil
print(f"Nama mahasiswa: {nama}")
print(f"Rata-rata nilai: {rata_rata_nilai}")
print(f"Nilai akhir: {nilai}")