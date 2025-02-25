'''
Scriptet sjekker om to datoer er oppgitt i kronologisk rekkefølge
'''

# Ta start- og sluttdato som input. Splitter på .
# bruker map for å lagre dag og måned som separate variabeler av typen int.
d_1, m_1 = map(int, input("Skriv inn startdato på formatet [dd.MM]: ").split('.'))
d_2, m_2 = map(int, input("Skriv inn sluttdato på formatet [dd.MM]: ").split('.'))


# Hvis startmåned er mindre enn sluttmåned
# Eller samme måned men startdag er lavere enn sluttdag
if m_1 < m_2 or ( m_1 == m_2 and d_1 < d_2 ):
	print("Riktig rekkefølge!")

# Måned og dag er like
elif m_1 == m_2 and	d_1 == d_2:
	print("Samme dato!")

# Datoene er ikke oppgitt i kronologisk rekkefølge
else:
	print("Feil rekkefølge!")
