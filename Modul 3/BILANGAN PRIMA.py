atas =int(input("masukan batas atas: "))#batas awal
bawah =int(input("masukan batas bawah: ")) #batas akhir

print('bilangan prima antara {atas} dan {bawah} adalah: ')
for i in range(atas, bawah+1):#range u/ menghasilkan deret angka 
    if i > 1:
        for n in range (2, i):
            if (i % n) == 0:#% modulus itu habis di bagi
                break
        else:
            print(i)
