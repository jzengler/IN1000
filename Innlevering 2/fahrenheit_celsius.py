#Tar temperatur i fahrenheit som input og konverterer til celsius

#temperatur i fahrenheit av typen desimaltall
fahrenheit = float(input("Skriv inn temperatur i fahrenheit: "))

#omregning til celsius
celsius = (fahrenheit - 32) * 5 / 9

#skriver ut temperatur i celsius. Runder av til to desimaler og gjør om til streng
print("Temperatur i celsius: " + str(round(celsius, 2)))
