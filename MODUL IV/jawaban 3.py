# def pangkat_dua(n):
#     if n == 0:
#         return 1
#     else:
#         return 2 * bilangan
# bilangan = int(input("Masukkan bilangan positif: "))
# if bilangan < 0:
#     print("eror!, masukkan bilangan positif.")
# else:
#     hasil = pangkat_dua(bilangan)
#     print(f"{bilangan} pangkat dua adalah {hasil}")

#di jadikan (-)
bilangan = int(input("Masukkan bilangan: "))
def pangkat_dua(bilangan):
    if bilangan == 0:
        return 1
    else:
        return  bilangan * bilangan 
hasil=pangkat_dua(bilangan)
print(bilangan,"pangkat dua adalah",hasil)