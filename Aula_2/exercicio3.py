# Exercício 3
peso = input("Digite seu peso (em kg): ")
altura = input("Digite sua altura (em metros): ")

peso = float(peso)
altura = float(altura)

imc = peso / (altura * altura)
imc = round(imc,2)

print("Seu IMC é",imc,".")