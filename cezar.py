for n in range(1,28):   
    palavra = list("ABC")
    alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(len(palavra)):
        letra = palavra[i]
        indice = alfabeto.index(letra)
        nova_letra = alfabeto[indice+n]
        palavra[i]=nova_letra
    print(palavra)