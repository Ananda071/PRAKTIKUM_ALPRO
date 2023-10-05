print("PERMAINANAN batu, gunting, kertas")
user_1 = input("silahkan pilih:")
user_2 = input("silahkan pilih:")
if user_1 == "batu" and user_2 == "kertas":
    print(f"{user_1} vs {user_2} = {user_2} WIN!!!")
elif user_1 == "batu" and user_2 == "gunting":
     print(f"{user_1} vs {user_2} = {user_1} WIN!!!")
elif user_1 == "kertas" and user_2 == "batu":
     print(f"{user_1} vs {user_2} = {user_1} WIN!!!")
elif user_1 == "gunting" and user_2 == "batu":
     print(f"{user_1} vs {user_2} = {user_2} WIN!!!")
elif user_1 == "gunting" and user_2 == "kertas":
     print(f"{user_1} vs {user_2} = {user_1} WIN!!!")
elif user_1 == "kertas" and user_2 == "gunting":
     print(f"{user_1} vs {user_2} = {user_2} WIN!!!")
else:
     print("HASILNYA TIDAK VALID, SILAHKAN ULANGI SEKALI LAGI!")