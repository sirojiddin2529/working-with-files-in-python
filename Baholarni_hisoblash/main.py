import time
from datetime import datetime

def sent_function(name: str, age: int)->None:
    now_time = datetime.now()
    great_time = now_time.strftime("%Y-%m-%d  %H:%M:%S")
    with open("grades.txt", "a") as file:
        
        file.write(f"{great_time} da yaratildi:\n{name}: {age}\n")

print("Ismingiz: Ali, Yoshingiz: 25 kurinishida kiriting")
print("Agar yana ma`lumotlarni qo`shmoqchi bo`lsangiz 1 aks holda 0 raqamini yuboring")
s = 0
count = 0
summ = '('
while True:
    name = input("Ismingizni kiriting:")
    age = int(input("Yoshingiz kiriting: "))

    s += age
    count += 1
    summ += str(age)
    test = input("Yana ma`lumot qo`shasizmi?:")
    if test != '0':
        summ += '+'
        sent_function(name, age)
    else:
        s = s / count
        summ += f') / {count} = {s} '
        print(f"Result:\n{summ}")
        sent_function(name, age)
        break