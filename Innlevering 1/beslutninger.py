'''
Scriptet tar for seg if beslutninger
'''

# Spør bruker om hen har lyst på brus
svar = input("Har du lyst på en brus?")


# If-sjekk om svaret er ja
if svar == "ja":
	print("Her har du en brus!")

# elif-sjekk om svaret er nei
elif svar == "nei":
	print("Den er grei.")

# else hvis brukeren har svart noe annet enn ja eller nei
else:
	print("Det forstod jeg ikke helt.")
