'''
1. Nei, konkatenering av heltall og streng i printfunksjonen vil ikke fungere.

2. Det er ingen feilhåndtering hvis input er noe annet enn et heltall.
   Det medfører at programmet feiler ved typeendring av verdien i a.
'''

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
	print(b + "Hei!")