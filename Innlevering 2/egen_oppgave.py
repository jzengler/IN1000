'''
Lag et program som spør brukeren om semesteravgiften er betalt og om brukeren har tilgang til de ulike ressursene for faget IN1000.

1. Hvis semesteravgiften ikke er betalt skriv ut informasjon om frist og en lenke til studentweb
2. Hvis brukeren ikke har laget et passord til uio-brukeren skriv ut en lenke til passordsiden.
	a. Hvis svaret er ja fortsett med å spørre om brukeren har meldt seg inn i en gruppe på piazza-forumet og har tilgang til devilry innleveringssiden.
	b. Vis lenke til den aktuelle ressursen og kort informasjon om hva det er hvis svaret er nei.
3. Skriv ut lenken til semestersiden uavhengig av hva svarene på tidligere spørsmål var.

Et lite script som spør om brukeren har registrert seg ved ulike uio ressurser.
'''

# lagre svar fra bruker
svar = input("Har du husket å betale semesteravgiften? ")

# sjekker om svaret er ja, alle andre tilfeller viser informasjon om frist og lenke til studentweb
if svar  == "ja":
	print("Bra!")
else:
	print("Husk at fristen for å betale er 1. september!")
	print("Gå til https://studentweb.uio.no/studentweb/login.jsf?inst=FSPROD for å se faktura")

# overskriver verdien i variabelen svar
svar = input("\nHar du laget et passord til uio-brukeren din? ")

# Fortsetter med spørsmål om piazza og devilry hvis ja. Viser lenke til passordsiden til uio hvis nei
if svar == "ja":
	print("Bra!")

	# overskriver variabelen svar
	svar = input("\nHar du meldt deg inn i en gruppe på forumet på piazza?")

	# ja er eneste gyldige svar
	if svar == "ja":
		print("Flott!")

	else:
		print("Det burde du gjøre! Der kan du stille spørsmål om python eller om faget IN1000.")
		print("https://piazza.com/")


	# overskriver variabelen svar igjen
	svar = input("\nHar tilgang til devilry innleveringssiden?")

	# eneste gyldige svar er ja
	if svar == "ja":
		print("Så bra!")

	else:
		print("Alle obligatoriske oppgaver skal leveres på devilry!")
		print("Denne tilgangen bør du ordne med en gang! https://devilry.ifi.uio.no/")


else:
	print("Passord til brukeren din kan du opprette her: https://passord.uio.no/")

# Viser lenke til semestersiden uansett hva brukeren har svart tidligere
print("\nGå til semestersidene for faget for å se informasjon, forelesninger og oppgaver. Lykke til!")
print("https://www.uio.no/studier/emner/matnat/ifi/IN1000/h19/")