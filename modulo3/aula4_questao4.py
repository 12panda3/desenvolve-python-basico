

kg = int(input("Digite o peso do pacote: "))
km = int(input("Digite a distância em km's: "))
p = float(0)

if kg > 10:
    p = float(10)

if km < 100:
    p += float(kg)

if km > 100 and km < 300:
    p += float(kg * 1.50) 

if km > 300:
    p += float(kg * 2)

print("O preço será de R$", p)