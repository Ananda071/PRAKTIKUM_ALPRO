size = int(input("masukkan size:"))
#perulangan i jika if
for i in range(size):#range u/ meenghasilkan deret angka
  if i == 0 or i == size-1: #i
    print("o"*size)
  else:
    print("o" + " "*(size-2) + "o")
print() #spasi

for i in range(size):
  if i == 0  :
    print("o"*size)#menampilkan ke 
  elif i > size//2: #// untuk pembagian bilangan bulat
    print(" "*(size-1) + "o")
  else:
    print(" "*(size-1) + "o")
print()

for i in range(size):
  if i == size:
    print(" "*(size-1) +"o")
  else:
    print(" "*(size-4) +"o")
print()
