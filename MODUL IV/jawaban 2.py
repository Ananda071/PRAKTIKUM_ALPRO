def faktorial(n):#<--untuk mendeklasarikan fungsi bernama"faktorial"
    if n == 0:
        return 1 #mengembalikan nilai
    else:
        return n * faktorial(n - 1)#rumus faktorial
bilangan = int(input("masukkan bilangan postif:"))
if bilangan < 0:
    #Ini adalah kondisi untuk memeriksa
    #apakah bilangan yang dimasukkan oleh pengguna negatif.
    #Jika negaif, maka pesan "bilangan faktorial hanya untuk bilangan positif" akan dicetak
    print("bilangan faktorial hanya untuk bilangan poositif.")
else:
    faktor = faktorial(bilangan)
    print(f"Faktorial dari {bilangan} adalah {faktor}")
    #Jika bilangan positif
    # maka faktorial akan dipanggil dengan kata "bilangan".
    #  dan hasilnya akan disimpan dalam variabel faktor.

    #faktorial itu bilangan bulat yg di kalikan bilangan sebelumnya
    #rekursif adlh fugsi yg memanggil dirinya  sendiri/ fungsi itu sendiri
    #parameter itu menampung nilai yg di proses dlm fungsi.