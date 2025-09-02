from InquirerPy import inquirer

choices = ["+", "-", "*", "/","="]

def menu():
    action = inquirer.select(
        message = "operação:",
        choices = choices,
        default=choices[0]
    ).execute()

    return action

def calculo():
    lista=[]
    print(9*"*", "CALCULADORA", 9*"*")
    repetir=True
    vezesrepetidas=0
    while repetir:
        #parte visível
        num1=int(input("número:"))        
        lista.append(num1)
        operacao=menu()
        lista.append(operacao)

        #repetições para segundo numero
        if vezesrepetidas==0:
            num2=int(input("número:"))
            lista.append(num2)
            operacao=menu()
        lista.append(operacao)
        vezesrepetidas+=1

        #encerra o while
        if operacao== "=":
            repetir=False
    indice = 0
    par = 0
    impar = 1

    while lista[indice] != "=":
        if indice == 0:
            numero1=lista[par]
        operar = lista[impar]
        if par != len(lista) - 2:
            par = par+2
            numero2 = lista[par]

        if operar == "+":
            numero1 = numero1+numero2
        if operar == "-":
            numero1 = numero1-numero2
        if operar == "/":
            numero1 = numero1/numero2
        if operar == "*":
            numero1 = numero1*numero2
        indice+=1
        if impar != len(lista) - 1:
            impar+=2
    print ("o resultado é: ", numero1)


calculo()

