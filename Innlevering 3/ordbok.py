



# ordbok for matvarer og pris
matvarer = {"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}
print(matvarer)

# itererer to ganger der bruker oppgir varenavn og pris som legges til ordboken matvarer
for i in range(0,2):
    # mellomlagre brukerinput
    varenavn = input("Skriv inn varenavn: ")
    pris = float(input("skriv inn pris[kr.øre]: "))

    #legger til i ordboken
    matvarer[varenavn] = pris

    # gjør jobben, men er ikke spesielt pen å se på...
    #matvarer[input("Skriv inn varenavn: ")] = float(input("skriv inn pris[kr.øre]: "))

print(matvarer)
