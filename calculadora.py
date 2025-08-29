print("calculo")
num1=int(input("primeiro número:"))
num2=int(input("segundo número:"))
operacao=str(input("Qual operação você deseja fazer(+,-,*,/)"))


if operacao == "+":
    resultado=num1+num2
elif operacao == "-":
    resultado=num1-num2
elif operacao == "*":
    resultado=num1*num2
elif operacao == "/":
    resultado=num1/num2

print("o resultado é",resultado)