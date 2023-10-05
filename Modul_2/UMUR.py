print("umur saya")
umur = int(input("masukkan umur:"))
if umur > 50 :
    print(umur, "tua")
elif umur > 25:
    print(umur,"dewasa" )
elif umur > 17:
    print(umur,"muda" )
elif umur > 7:
    print(umur, "anak anak")
elif umur > 3:
    print(umur, "balita")
else:
    print("umur tidak valid")