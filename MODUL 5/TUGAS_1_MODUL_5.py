#Buatlah program menggunakan List. 
#Program berisi data makanan dan harga secara dinamis (minimal 5 data). 
#Lalu cetak program dengan menampilkan data makanan dan harga yang telah diinput tadi.

#prepend(item) menambahkan item dari depan
#APPEND(item) menambahkan item dari belakang.
#INSERT(index, item) menambahkan item dari indeks tertentu

data_makanan = []
data_harga = []
for i in range(5):
    nama_makanan = input(f"nama makanan ke-{i+1}:")
    data_makanan.append(nama_makanan)
    harga_makanan = float(input(f"harga {nama_makanan}:"))
    data_harga.append(harga_makanan)

print("\nData Makanan:")
for i in range(5):
    print(f"{i+1}.{data_makanan[i]}")
    print(f"= Rp-{data_harga[i]:,.2f}")