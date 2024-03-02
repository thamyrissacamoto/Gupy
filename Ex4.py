def inverterString(s):
    caracteres = list(s)
    inicio = 0
    fim = len(caracteres) - 1
    while inicio < fim:
        caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
        inicio += 1
        fim -= 1
    return ''.join(caracteres)

stringOriginal = "Hello world!"
stringInvertida = inverterString(stringOriginal)
print("String original:", stringOriginal)
print("String invertida:", stringInvertida)
