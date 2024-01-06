altura = float(input("Qual a sua altura em cm? "))
peso = float(input("Qual seu peso em kg? "))

imc = peso / (altura/100)**2

if imc < 18.5:
    print("Magreza")

elif imc in range(18.5, 24.9):
    print("Peso ok") 

elif imc in range(25.0, 29.9):
    print("Sobrepeso")

elif imc in range(30.0, 39.9):
    print("Obesidade")

else:
    print("Obesidade preocupante")

