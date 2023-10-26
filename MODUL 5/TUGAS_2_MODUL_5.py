#Buatlah program yang 
#dapat menginputkan data mahasiswa fakultas teknik 
#(berisikan NIM, Nama, Alamat dan Prodi) 
#dengan menggunakan List dan Tuple. 
#Program dapat mencari data mahasiswa sesuai dengan Data Prodi. 
#Minimal data adalah 5

def data_mahasiswa():
    NIM = int(input("Masukkan NIM: "))
    Nama = input("Masukkan Nama: ")
    Alamat = input("Masukkan Alamat: ")
    Prodi = input("Masukkan Prodi: ")
    return(NIM, Nama, Alamat, Prodi)
def cari_data_mahasiswa(Mahasiswa, dari_prodi):
    Mahasiswa_prodi = []
    for data in Mahasiswa:
        if data[3] == dari_prodi:
            Mahasiswa_prodi.append(data)
    return Mahasiswa_prodi

Data_mahsiswa = []
jumlah_data = 5
for i in range(jumlah_data):
    print(f"Masukkan data mahasiswa {i+1}")
    Data_mahsiswa.append(data_mahasiswa())

print("\nData Mahasiswa:")
for data in Data_mahsiswa:
    print(f"\nNIM: {data[0]} \nNama: {data[1]} \nAlamat: {data[2]} \nProdi: {data[3]}")

dari_prodi = input("\nData Mahasiswa dari Prodi:")
hasil_pencarian = cari_data_mahasiswa(Data_mahsiswa, dari_prodi)

print(f"\nHasil_pencarian {dari_prodi}:")
if len(hasil_pencarian) > 0:
    for data in hasil_pencarian:
        print(f"\nNIM: {data[0]} \nNama: {data[1]} \nAlamat: {data[2]} \nProdi: {data[3]}")
else:
    print("Tidak ada data mahasiswa dlm prodi ini!")