'''print("kérem a nevedet:",end=" ")
nev = input()
print("szia " + nev)'''

'''nev = input("kérem a nevedet:")
print("szia " + nev)'''

'''szam = int(input("kérek egy számotr 1 és 10 között: "))
print(type(szam),szam)
print(szam*2)'''

'''szam = float(input("kérek egy számotr 1 és 10 között: "))
print(type(szam),szam)
print(szam*2)'''

'''szam = (input("kérek egy számotr 1 és 10 között: "))
egesz = int(szam)
print(egesz*2)'''

'''beolvasott = input("kérek valamit: ")
print(beolvasott)
print(type(beolvasott))
print(list(beolvasott))
print(set(beolvasott))
print(tuple(beolvasott))'''

'''szam = (input("kérek egy számotr 1 és 10 között: ")) 
egesz = int(szam)
if egesz < 1:
    print("a szám az túl kicsi")
else:
    if egesz > 10:
        print("szam túl nagy")
print("-"*10)'''

'''szam = (input("kérek egy számotr 1 és 10 között: ")) #számot csak 1-10 ig tudsz bele írni ha túl kicsi a szám mondja hogy túl kicsi ha túlnagy szól hogy túl nagy
egesz = int(szam)
if egesz < 1:
    print("a szám az túl kicsi")
elif egesz > 10:
        print("szam túl nagy")
print("-"*10)'''

'''x = int(input("kérek egy számot : ")) #megmondja hogy a szám páros e vagy páratlan 
y = x % 2
if y == 1:
    print("páratlan")
else:
    print("páros")'''

'''x = int(input("adj meg egy egész számot: ")) # a program megmondja hogy a szám pozitív negatív vagy 0
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
elif x == 0:
    print(0)'''

'''x = int(input("adj meg egy egész számot: ")) #program megmondja hogy a szám osztható e 3-mal
if x%3 == 0:
    print("osztható 3-mal")
else:
    print("nem osztható 3-mal")'''
