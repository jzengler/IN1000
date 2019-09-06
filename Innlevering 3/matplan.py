# Scriptet inneholder en prosdeyre som slår opp matplanen til en beboer fra en ordbok
# Svar på  deloppgave 3 er skrevet nederst i filen


# Oppretter ordboken for beboere og måltid
matplan = {"Ola Dunk":["Bacon", "Kneip med leverpostei", "Koteletter"],
"Kari Havrenakke":["Havrefras","Napoelonskake","Betasuppe"]}

# Prosedyre for å søke opp matplan for beboer
def vis_matplan():

    # Tar navn som input og gjør om navn til å begynne med versaler
    navn = input("Skriv inn navn på beboer for å vise matplan: ").title()

    # Hvis navn er en nøkkel i matplan
    if navn in matplan:

        #Skriv ut måltidene
        print("Matplan for " + navn)
        print("Frokost: " + matplan[navn][0])
        print("Lunsj: " + matplan[navn][1])
        print("Middag: " + matplan[navn][2])

    # Hvis beboer ikke finnes i ordboken
    else:
        print("Beboer ikke registrert med en matplan: " + navn)

# Kall prosedyren
vis_matplan()



# Svar på deloppgave 3
'''
3.  a.
Her ville jeg benyttet mengde fordi brukernavnene er unike og bør ikke listes opp flere ganger.
Ved å bruke mengde unngår man at det er flere studenter i faget enn det er unike navn.

Skal det derimot knyttes attributter til et brukernavn vil en ordbok være mer hensikstsmessig.
Dette vil fortsatt ivareta unikhet for brukernavn ettersom nøkler i ordboken kun kan forekomme en gang.

    b.
Her vil det være naturlig med en ordbok som knytter antall poeng til brukernavn.
Som forklart i oppgaven over kan dette være et eksempel på en attributt som knyttes til studenten

    c.
I dette tilfellet bør det brukes en liste hvis forutsetningen er at kun navn skal være med.
Fordi en person kan vinne i lotto flere ganger må det også være mulig å føre opp navnet flere ganger.

    d.
Her forutsetter jeg at det skal utarbeides en kollektiv oversikt over allergier for en gruppe mennesker.
Da kan det benyttes en mengde fordi det ikke er behov for å se hvilken enkelt gjest som har hvilke allergier.
'''
