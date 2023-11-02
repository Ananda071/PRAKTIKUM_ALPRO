# Seorang mahasiswi mengisi data diri sebagai berikut :
# Nama : Susanti
# Alamat : Surakarta
# Prodi : Sistem informasi
# Semester : 5
# Angkatan : 2015
# Pada tahun 2018 susanti pindah tempat tinggal ke madura
# dan pada saat bersamaan susanti beralih jenjang ke prodi teknik informatika. 
# Namun pada tahun 2019 susanti memutuskan untuk berhenti menjadi mahasiswi. 
# Buatlah program dari alur cerita diatas!

# mhs = {
#     'nama': 'susanti',
#     'almt':'surakarta',
#     'prodi':'sistem informasi',
#     'smstr':'5',
#     'angkatan':'2015',
#     'status':'mahasiswa'
#     }

# mhs['nama'] = input("nama:")
# mhs['almt'] = input("almt:")
# mhs['prodi'] = input("prodi:")
# mhs['smstr'] = int(input("smstr:"))
# mhs['angkatan'] = int(input("angkatan:"))
# mhs['status'] = input("mahasiswa:")

# print(mhs)

#2018
# mhs = {
#     'nama': 'susanti',
#     'almt':'surakarta',
#     'prodi':'sistem informasi',
#     'smstr':'5',
#     'angkatan':'2015',
#     'status':'mahasiswa'
#     }

# del mhs ['almt']
# del mhs ['prodi']

# mhs['almt'] = 'madura',
# mhs['prodi'] = 'teknik informatika',
# print (mhs)

#2019
# mhs = {
#     'nama': 'susanti',
#     'almt':'surakarta',
#     'prodi':'sistem informasi',
#     'smstr':'5',
#     'angkatan':'2015',
#     'status':'mahasiswa'
#     }

# del mhs ['nama']
# del mhs ['almt']
# del mhs ['prodi']
# del mhs ['smstr']
# del mhs ['angkatan']
# del mhs ['status']

# mhs['status'] = 'data mahasiswa ini tidak ada,karena sudah keluar.'
# print(mhs)

# key = "mahasiswa"
# status = key in mhs
# print(f"apakah {key} ada di mhs")

mhs = {
    'nama': 'susanti',
    'almt':'surakarta',
    'prodi':'sistem informasi',
    'smstr':'5',
    'angkatan':'2015',
    'status':'mahasiswa'
    }

mhs['nama'] = input("nama:")
mhs['almt'] = input("almt:")
mhs['prodi'] = input("prodi:")
mhs['smstr'] = int(input("smstr:"))
mhs['angkatan'] = int(input("angkatan:"))
mhs['tahun pindah'] = int(input("masukkan tahun pindah :"))
mhs['tahun keluar'] = int(input("masukkan tahun keluar :"))

del mhs ['almt']
del mhs ['prodi']

mhs['almt'] = 'madura',
mhs['prodi'] = 'teknik informatika',
print(mhs,"\npada tahun", mhs['tahun pindah'],
      mhs['nama'], "pindah tempat ke", mhs['almt'], 
      "\ndan pada saat itu juga", mhs['nama'],
      "\npindah prodi", mhs['prodi'], 
      "\nNamun pada tahun", mhs['tahun keluar'], 
      mhs['nama'], "memutusakan untuk berhenti menjadi mahasiswa")

# Pada tahun 2018 susanti pindah tempat tinggal ke madura
# dan pada saat bersamaan susanti beralih jenjang ke prodi teknik informatika. 
# Namun pada tahun 2019 susanti memutuskan untuk berhenti menjadi mahasiswi. 
