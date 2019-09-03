#Scriptet demonstrerer bruk av lister i python3

# liste med tre elementer av typen heltall
tall_liste = [3, 6, 9]

# skriver ut første og tredje element i listen ved å slice. starter på siste element og dekrementer med 2; tilbake til index 0
#print(tall_liste[::-2])
print(tall_liste[::len(tall_liste)-1])

# Oppretter tom liste til navn
navn_liste = []

# for hvert element i rekken 0 til 4 legg til en ny brukerinput
# konverterer til minuskler for å forenkle hvis-spørring med navn
for i in range(0,4):
    navn_liste.append(input("Skriv inn navn: ").lower())

# sjekker om listen inneholder navnet mitt
if "zengler" in navn_liste:
    print("Du husket meg!")
else:
    print("Glemte du meg?")


# lagrer summen tall_liste i element 1 og verdien 1 i element 2 til multiplisering under
sum_produkt = [sum(tall_liste),1]

# itererer over tall_liste og multipliserer med produktet av foregående.
for element in tall_liste:
    sum_produkt[1] = sum_produkt[1] * element

# sammenslåing av tall_liste med sum_produkt
sammen = sum_produkt + tall_liste

print(sammen)

# fjerner de to siste elementene
sammen = sammen[0:len(sammen)-2]

print(sammen)
