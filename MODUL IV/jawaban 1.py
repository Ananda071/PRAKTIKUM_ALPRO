#bangun ruang
def luas_permukaan_kerucut(r, s):
    rumus=  22/7 * r * (r + s)
    return rumus
def luas_permukaan_limas(s, a, t):
    rumus = (1.72 * s * s) + 5 * (0.5 * a * t)
    return rumus
def luas_permukaan_persegi_lima(luas_alas, keliling_alas, tinggi_prisma):
    return 2 * luas_alas * keliling_alas * tinggi_prisma
print("menghitung luas permukaan bangun ruang")
pilih_bangun_ruang= int(input("masukan bangun ruang yang akan anda hitung (1/2/3):"))

if pilih_bangun_ruang == 1:#kerucut
    r =float(input("jari-jari kerucut:"))#float tuh bisa 2 bilangan, desimal / bulat
    s = float(input("selimut: "))
    hasil = luas_permukaan_kerucut(r, s)
    print("Luas permukaan kerucut adalah:", hasil)

elif pilih_bangun_ruang == 2:#limas segitiga
    s = float(input("Panjang sisi alas: "))
    a = float(input("Panjang sisi miring alas: "))
    t = float(input("Tinggi limas: "))
    hasil = luas_permukaan_limas(s, a, t)
    print("Luas permukaan limas adalah:", hasil)

elif pilih_bangun_ruang == 3:#prisma segitiga
    luas_alas = float(input("Masukkan luas alas segi lima : "))
    keliling_alas = float(input("Masukkan keliling alas segi lima: "))
    tinggi_prisma = float(input("Masukkan tinggi prisma segi lima: "))
    hasil = luas_permukaan_persegi_lima(luas_alas, keliling_alas, tinggi_prisma)
    print("Luas permukaan segi lima beraturan adalah:", hasil)


else:
    print("Pilihan tidak valid. Silakan pilih 1 untuk menghitung luas permukaan kerucut, 2 untuk menghitung luas permukaan limas, atau 3 untuk menghitung luas permukaan segi lima.")