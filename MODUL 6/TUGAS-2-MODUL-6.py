# ukm_melukis = {'mala','mili', 'mulu','mele','molo','lala'}
# ukm_menulis = {'dada','didi','dudu','dede','dodo','sasa'}
# ukm_membaca = {'nana','nini','nunu','nono','mala'}
# ukm_merangkai = {'lala','lili','nono'} 
# print(ukm_melukis,ukm_menulis,ukm_membaca,ukm_merangkai)

# mhsw_bnyk_ukm =() 
# ukm_list = [ukm_melukis,ukm_menulis,ukm_membaca,ukm_merangkai]

# #lebih dr 1 ukm
# gabungan=set()
# gabungan1=ukm_melukis&ukm_membaca
# gabungan.update(gabungan1)
# gabungan1=ukm_melukis&ukm_menulis
# gabungan.update(gabungan1)
# gabungan1=ukm_melukis&ukm_merangkai
# gabungan.update(gabungan1)
# gabungan1=ukm_membaca&ukm_menulis
# gabungan.update(gabungan1)
# gabungan1=ukm_membaca&ukm_merangkai
# gabungan.update(gabungan1)
# gabungan1=ukm_menulis&ukm_merangkai
# gabungan.update(gabungan1)
# print("Siswa yang ikut lebih dari satu UKM: ",gabungan)

# ukm_melukis.add('moci')
# ukm_melukis.update(ukm_melukis) 
# ukm_menulis.add('moci')
# ukm_menulis.update(ukm_menulis)

# #hapus mhssw
# ukm_melukis.remove('mala') 
# ukm_melukis.update(ukm_melukis)
# print(ukm_melukis)

# #ukm kurang dr 4 anggota
# ukm_kurang_dari_4_anggota = [ukm for ukm in [ukm_melukis,ukm_membaca,ukm_menulis,ukm_merangkai] if len(ukm) < 4]
# print("UKM dengan kurang dari 4 anggota:", ukm_kurang_dari_4_anggota)

# #mhssw yg tdk ad di ukm mnapun                      
# mhssw_tdk_ada_di_ukm = set() 
# for ukm in ukm_list:
#     mhssw_tdk_ada_di_ukm.update(ukm)
# print(mhssw_tdk_ada_di_ukm)

# ukm = {
#     'ukm_1': 'ana, ani, nia, nei, nana',

#     'ukm_2': 'lala, lili, lulu, koko, lolo',

#     'ukm_3': 'sai, sei, soi',

#     'ukm_4': 'kiki, kaka, koko, keke, nia'
# }

ukm = {
    "UKM 1": {"tingky","wingky","tamam","dipsi","faroid"},
    "UKM 2": {"upin","jarjit","akmal","tamam"},
    "UKM 3": {"meil","memei","susanti"},
    "UKM 4": {"febi","kukuh","vivi","marsya","azli"},
}

for key, value in ukm.items():
    print(key, value)

# Hitung mahasiswa yang bergabung dalam lebih dari satu UKM
mahasiswa_lebih_dari_satu_ukm = set()
macam_ukm = {}

for ukm_name, anggota in ukm.items():
    for mahasiswa in anggota:
        if mahasiswa in macam_ukm:
            mahasiswa_lebih_dari_satu_ukm.add(mahasiswa)
        else:
            macam_ukm[mahasiswa] = ukm_name

print("Mahasiswa yang bergabung dalam lebih dari satu UKM:", mahasiswa_lebih_dari_satu_ukm)

# # Tambahkan ke dlm ukm
ukm["UKM 1"].add('raka')
print(ukm["UKM 1"])
ukm["UKM 4"].add('raka')
print(ukm["UKM 4"])
# ukm_4.add('moci')
# ukm_2.add('moci')
# ukm_4.update(ukm)
# ukm_2.update(ukm)

# # Hapus nei dari ukm_1
# ukm ['ukm_1'].remove('nei')

# # Tampilkan UKM dengan kurang dari 4 anggota
# ukm_kurang_dari_4_anggota = [ukm for ukm in [ukm_1, ukm_2, ukm_3, ukm_4] if len(ukm) < 4]
# print("UKM dengan kurang dari 4 anggota:", ukm_kurang_dari_4_anggota)

# # Tampilkan mahasiswa yang tidak bergabung dalam UKM
# mahasiswa_tidak_bergabung = set([
#     'ana','ani','nia','nei','lala','lili','lulu','lolo','sai','sei','soi','jeqi','kiki','kaka','koko','keke'
# ]) - (
#     ukm_1 | ukm_2 | ukm_3 | ukm_4
# )
# print("Mahasiswa yang tidak bergabung dalam UKM:", mahasiswa_tidak_bergabung)