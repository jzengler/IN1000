'''
Scriptet tar for seg variabler, input og utskrift
Tar ett navn og skriver ut en konkatenert streng
Regner differanse mellom to tall og skriver ut
Tar ett annet navn og konkatenerer med det første
'''

# Lagrer input fra bruker i variabelen navn
navn = input("Skriv inn navnet ditt: ")

# Skriver ut Hei <innholdet i variabelen navn>!
print("Hei " + navn + "!")


# Tall og differanse
# Intialiserer to heltallsvariabler
tall_a = 8
tall_b = 15

# Skriver ut tallene som streng på hver sin linje
print(str(tall_a) + "\n" + str(tall_b))

# Lagrer differansen av tallene a og b i variabelen differanse
differanse = tall_a - tall_b

# Skriver ut Differanse etterfulgt av differansen som streng
print("Differanse: " + str(differanse))


# Mer bruker input
# Tar et nytt navn som input og konkatenerer begge navnene i var. sammen
annet_navn = input("Skriv inn ett navn til: ")
sammen = navn + annet_navn

# skriver ut sammen
print(sammen)

# Endrer verdien av sammen til å innholde og mellom variablene navn og annet_navn
sammen = navn + " og " + annet_navn

# skriver ut sammen igjen
print(sammen)


