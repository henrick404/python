palavra = list("ABC")
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(palavra)):
    letra = palavra[i]
    indice = alfabeto.index(letra)
    nova_letra = alfabeto[indice+1]
    palavra[i]=nova_letra
print(palavra)