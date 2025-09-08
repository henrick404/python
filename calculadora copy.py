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
    resultado=0
    def operando(tipo):
        indice = 1
        resultado=0
        while lista[indice] != "=":
            numero1=lista[indice-1]
            numero2=lista[indice+1]
            if tipo =="*":   
                if lista[indice] == tipo:
                    resultado = numero1*numero2
                    lista[indice-1]=resultado
                    del lista[indice+1]
                    del lista[indice]
            if tipo =="/":   
                if lista[indice] == tipo:
                    resultado = numero1/numero2
                    lista[indice-1]=resultado
                    del lista[indice+1]
                    del lista[indice]
            if tipo =="+":   
                if lista[indice] == tipo:
                    resultado = numero1+numero2
                    lista[indice-1]=resultado
                    del lista[indice+1]
                    del lista[indice]
            if tipo =="-":   
                if lista[indice] == tipo:
                    resultado = numero1-numero2  
                    lista[indice-1]=resultado
                    del lista[indice+1]
                    del lista[indice]                            
    operando("*")
    operando("/")
    operando("+")
    operando("-")
    print(lista)

calculo()
