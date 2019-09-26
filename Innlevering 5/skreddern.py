'''
Skriv et beregningsprogram for skreddere med en funksjon som leser
inn en fil (som du lager selv og leverer sammen med de andrefilene)
der hver linje beskriver et navn på et mål og selve målet i tommer.
Formatet vil se slik ut:
Skulderbredde 4
Halsvidde 3.2
Livvidde 10

La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboken.
Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av
​tommerTilCm​ som du skrev tidligere for å skrive ut målene i centimeter
'''




# prosedyre som tar en liste av mål og konverterer til cm
def konverterMaal(maal):
    for i in maal:
        print( tommerTilCm(float(i)), "cm" )

# funksjon som konverterer tommer til cm
def tommerTilCm(tommer):
    assert tommer > 0, "parameter maa være storre enn 0"
    return tommer * 2.54

def hovedprogram():
    #opprett tom ordbok
    lagretMaal = {}

    # åpne filen maal.txt med lesetilgang
    with open("maal.txt", "r") as maal:
        # fjern new line og split hver linje på mellomrom
        for linje in maal:
            l = linje.rstrip("\n").split(" ")

            # bruk første element som nøkkel og andre som verdi
            lagretMaal[l[0]] = l[1]

    # konverter målene fra filen til cm
    konverterMaal(lagretMaal.values())

hovedprogram()
