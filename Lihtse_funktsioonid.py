from math import * # * kõik funktionid moodulist
#import math math.funktsion()

print()
print("Võrdse pindalaga ristkülik ja ring")
a= float(input("anna laius: "))
b= float(input("anna kõrgus: "))
S=a*b # -,+,**,/,//,%
P = 2*a+2*b
d = round (sqrt (a**2+b**2), 2) #ümardamine 2 numbrid koma pärast
print (f"pindala = {5}\nLäbimõõt = {P}\nDiagonaal = {d}")
print ("Ringi raadius")
r = round (sqrt (S/pi), 2)
print (f"Ringi raadius: = {r}")



#print("tere tulemast") #выводит инфо на экран, väljundlause
#nimi = input("Mis on sinu nimi?") #Sisendlause lugemine jaoks input()->str
#print() #tühi rida
#print (f"{nimi}, sul on väga ilus nimi!")
#print (nimi,", sul on väga ilus nimi!") # ->tühik
#print (nimi+", sul on väga ilus nimi!") #str+str
#vanus = int (input("Kui vana sa oled?")) # int(str)
#print (nimi, "sa oled",vanus,"aastat vana")
#vanus+=10
#print (nimi+", 10 aasta pärastsa sa oled "+str(vanus)+" aastat vana")