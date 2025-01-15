import time
from datetime import datetime

def sent_function(name: str, phon: str)->None:
    now_time = datetime.now()
    great_time = now_time.strftime("%Y-%m-%d  %H:%M:%S")
    with open("contacts.txt", "a") as file:
        
        file.write(f"{great_time} da yaratildi:\n{name}: +998{phon}\n\n")

print("Ismingiz: Ali, tel raqmingiz: 339969633 kurinishida kiriting")
print("Agar yana ma`lumotlarni qo`shmoqchi bo`lsangiz 1 aks holda 0 raqamini yuboring")
while True:
    name = input("Ismingizni kiriting:")
    phoneNumber = input("Tel nommiringizni kiriting: ")

    test = input("Yana ma`lumot qo`shasizmi?:")
    if test != '0':
        sent_function(name, phoneNumber)
    else:
        sent_function(name, phoneNumber)
        break

print("\nMarhamat contacts.txt fayliga saqlangan ma`lumotlar:\n")
with open("contacts.txt", "r") as file:
    print(file.read())
    