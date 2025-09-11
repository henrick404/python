from InquirerPy import inquirer

choices = ["+", "-", "*", "/","="]

def menu():
    action = inquirer.select(
        message = "operação:",
        choices = choices,
        default = choices[0]
    ).execute()

    return action

def calculo():
    lista = []
    print(9*"*", "CALCULADORA", 9*"*")
    repetir = True
    vezesrepetidas = 0
    while repetir:
        #parte visível
        num1 = float(input("número:"))        
        lista.append(num1)
        operacao = menu()
        lista.append(operacao)

        #repetições para segundo numero
        if vezesrepetidas == 0:
            num2 = float(input("número:"))
            lista.append(num2)
            operacao = menu()
            lista.append(operacao)
        vezesrepetidas+=1

        #encerra o while
        if operacao== "=":
            repetir=False

    def operando(tipo):
        indice = 1
        resultado=lista[0]
        while lista[indice] != "=":
            numero1=lista[indice-1]
            numero2=lista[indice+1]
            if tipo =="*":   
                if lista[indice] == tipo:
                    resultado = numero1*numero2
                    del lista[indice+1]
                    del lista[indice]
                    lista[indice-1]=resultado
                
            if tipo =="/":   
                if lista[indice] == tipo:
                    resultado = numero1/numero2
                    del lista[indice+1]
                    del lista[indice]
                    lista[indice-1]=resultado

            if tipo =="+":   
                if lista[indice] == tipo:
                    resultado = numero1+numero2
                    del lista[indice+1]
                    del lista[indice]
                    lista[indice-1]=resultado

            if tipo =="-":   
                if lista[indice] == tipo:
                    resultado = numero1-numero2  
                    del lista[indice+1]
                    del lista[indice]
                    lista[indice-1]=resultado
            if lista[indice]!="=":
                 indice+=1                          
    operando("*")
    operando("/")
    operando("+")
    operando("-")
    print("Resultado é igual a:",lista[0])


calculo()
