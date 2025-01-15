import time
from datetime import datetime

def sent_function(name: str)->None:
    now_time = datetime.now()
    great_time = now_time.strftime("%Y-%m-%d  %H:%M:%S")
    with open("shopping_list.txt", "a") as file:
        
        file.write(f"{great_time} da yaratildi:\n{name}\n")

print("Bozordan oladigan maxsulotlaringizni yozing:")
print("Agar yana ma`lumotlarni qo`shmoqchi bo`lsangiz 1 aks holda 0 raqamini yuboring")
while True:
    name = input("Maxsulot nomini kiriting:")
    
    test = input("Yana ma`lumot qo`shasizmi?:")
    if test != '0':
        sent_function(name)
    else:
        sent_function(name)
        break

print("\nMarhamat shopping_list.txt fayliga saqlangan ma`lumotlar:\n")
with open("shopping_list.txt", "r") as file:
    print(file.read())
