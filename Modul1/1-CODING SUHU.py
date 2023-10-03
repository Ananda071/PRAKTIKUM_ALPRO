#input suhu dalam celcius dari pengguna
celcius = "c"
farenheit = "f"
reamur = "r"
kelvin = "k"

celcius = float(input("masukkan suhu dalam ceelcius"))

#konversi celcius ke farenheit
farenheit =(celcius * 9/5 ) + 32
print(f"suhu dalam farenheit: {farenheit}derajat farenheit")

#konversi cecius ke reamur
reamur =celcius * 4/5
print(f"suhu dalam reamur: {reamur}derajat reamur")

#konversi celcius ke kelvin
kelvin =celcius + 273.15
print(f"suhu dalam kelvin: {kelvin}derajat kelvin")
