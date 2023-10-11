while True: #variabel yang program nya berulang terus jika nilai benar
    lama_peminjaman = int(input("Masukkan lama peminjaman buku (dalam hari): "))
    denda_harian = 2000
    denda_mingguan = 5000
    maksimum_peminjaman = 7 # 7 hari

    if lama_peminjaman <= maksimum_peminjaman:
        denda = 0
    else:
        denda_harian_total = denda_harian * (lama_peminjaman - maksimum_peminjaman)
        denda_mingguan_total = denda_mingguan * ((lama_peminjaman - maksimum_peminjaman) // 7)#bemagian bulat 7 untuk mengetahui mingguan  yang terlewat
        denda = denda_harian_total + denda_mingguan_total

    print(f"anda meminjam buku lebih dari {lama_peminjaman} hari, denda yang harus dibayar: Rp{denda}")
    
    ulangi = input("Apakah ingin menghitung lagi? (ya/tidak): ")
    if ulangi!= "ya":
        break