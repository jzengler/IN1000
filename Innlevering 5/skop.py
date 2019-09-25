def minFunksjon():
    for x in range(2):
        c = 2
        print(c)
        c += 1
        b =10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b = 0
    print(b)
    b = a
    a = minFunksjon()
    print(b)
    print(a)

hovedprogram()


'''
Først defineres funksjonen "minFunksjon" som ikke tar parameter.
Deretter defineres prosedyren "hovedprogram" som ikke tar parameter.
Så kalles "hovedprogram".
I "hovedprogram" opprettes variablene "a" og "b" med verdiene 42 og 0.
Variabelen "b" skrives så ut ved bruk av print før "b" settes lik "a".
Deretter kalles "minFunksjon".
"minFunksjon" starter med en for-løkke som vil eksekvere for hver "x" i rekken 0-1, altså 2 ganger.
Inne i løkken defineres variabelen "c" med verdien 2 og skrives deretter ut ved bruk av print.
Videre inkrementeres "c" med 1 og variabelen "b" defineres med verdien 10.
"b" førsøkes inkrementert med "a" som kun er definert i "hovedprogram". Dette vil generere en kjøretidsfeil.
'''
