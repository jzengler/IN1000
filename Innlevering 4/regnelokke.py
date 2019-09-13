'''
Scriptet demonstrerer bruk av while og for løkker
1,2 while-løkke som legger flyttall til liste så lenge bruker ikke oppgir tallet 0
3 for-løkke som skriver ut hvert element brukeren la til listen
4 for-løkke som finner summen av tallene
5 for-løkke som finner minste tall i listen
  for-løkke som finner største tall i listen
'''


#INIT
# initaliser med en slik at while-løkken kan kjøre første gang
tall = 1
# initialiserer en tom liste
minListe = []
# initialiser variabelen minSum
minSum = 0

# 1,2
# så lenge burkerinput ikke er null fortsett å ta nye tall
while tall != 0:
    # ta flyttall som brukerinput
    tall = float(input("Skriv inn et tall: "))

    # lagrer tallet i listen hvis det ikke er 0
    if tall != 0:
        minListe.append(tall)

# 3
# skriver ut hvert element i listen
for element in minListe:
    print("Du skrev inn:", element)

# 4
# legger til hvert element i listen til minSum
for element in minListe:
    minSum += element

# skriv ut summen av alle tallene i listen
print("\nSummen av tallene er:", minSum)

# 5
# Finner minste element i listen og skriver ut
minste = minListe[0]
for element in minListe:
    if element < minste:
        minste = element

print("\nDet minste tallet i listen er:", minste)

#finner største element i listen og skriver ut
storste = minListe[0]
for element in minListe:
    if element > storste:
        storste = element

print("\nDet stoorste tallet i listen er:", storste)
