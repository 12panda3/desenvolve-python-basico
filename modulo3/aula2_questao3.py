


i = int(input("Qual a sua idade? "))
p = input("Você já jogou PELO MENOS 3 jogos? (True ou False) ")
v = int(input("Quantos você venceu? "))
r = bool

if (i > 15 and i < 19) and (p == "True") and (v >= 1):
    r = True
    print("Apto para ingressar no clube de jogos de tabuleiro:", r)

else:
    r = False
    print("Apto para ingressar no clube de jogos de tabuleiro:", r)
