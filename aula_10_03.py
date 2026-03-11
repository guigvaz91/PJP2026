# Objetivo: Calcular IMC e classificar de forma simples

nome = input("Digite seu nome: ")
peso = float(input("Digite seu Peso (Kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura**2)    #aritiméticos
print(f"IMC de {nome}: {imc:.2f}")

#comparação + lógicos (faixa simplificada)
baixo_peso = imc <18.5
normal = (imc >= 18.5) and (imc < 25)
sobrepeso = (imc >= 25) and (imc < 30)
obesidade = imc >= 30

print("Baixo peso?", baixo_peso)
print("Normal?", normal)
print("Sobre peso?", sobrepeso)
print("Obesidade?", obesidade)