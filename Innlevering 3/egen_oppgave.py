'''
Lag et quiz-program som tar for seg hvilke land ulike bilmerker kommer fra.
Løs oppgaven ved å bruke ordboker.
'''


# Oppretter orbok for bilmerker
land_bilmerker = {"Volvo":"Sverige",
"Toyota":"Japan",
"Lada":"Russland",
"Seat":"Spania"}

#Poeng-variabel, første element er antall rette svar, andre element er antall spørsmål stilt
poeng = [0,0]

# For hvert merke i ordboken spør bruker og ta input
for merke in land_bilmerker:

    # inkrementer antall spørsmål stilt
    poeng[1] += 1
    # Still spørsmål og lagre svar som egennavn. Eks sverige -> Sverige
    svar = input("I hvilket land produseres " + merke +"? ").title()

    # Hvis svaret er rett
    if svar in land_bilmerker[merke]:
        # inkrementer antall rette svar
        poeng[0] += 1
        #Gi bruker tilbakemelding på at svaret var rett
        print("Riktig!\n")

    # Ellers hvis det er feil
    else:
        # Gi bruker tilbakemelding på at svaret var feil og hva som er det riktige svaret
        print("Feil! " + merke + " produseres i " + land_bilmerker[merke]+ "\n")

# Avslutt med å skriv ut [antall rette/antall spørsmål]
print(  "Du fikk " + str(poeng[0]) + "/" + str(poeng[1]) + " riktig!" )
