from random import randint
computer=randint(0,2)

if computer ==0:
    computer="kéo"
if computer == 1:
    computer= "búa"
if computer ==2:
    computer="bao"

while True:
    player=input("Vui Lòng Chọn Kéo Búa Bao:")
    if (player =="kéo") or (player =="bao") or (player =="búa"):
        break
print("sự lựa chọn của máy là: "+computer)
if player == computer:
    print("Hòa")
elif player == "kéo":
    if computer == "búa":
        print("thua")
    else:
        print("thắng")   
elif player =="búa":
    if computer =="kéo":
        print("Thắng")
    else:
        print("Thua")
else:
    if computer =="kéo":
        print("thua")
    else:
        print("Thắng")
