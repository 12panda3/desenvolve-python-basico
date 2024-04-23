


c = str(input("Escolha a classe (guerreiro, mago ou arqueiro): "))
f = int(input("Digite os pontos de força (de 1 a 20): "))
m = int(input("Digite os pontos de magia (de 1 a 20): "))

if c == "guerreiro":
    if f >= 15 and m <= 10:
        r = True

    else:
        r = False    

if c == "mago":
    if m >= 15 and f <= 10:
        r = True

    else:
        r = False    


if c == "arqueiro":
    if f >= 5 and f < 15 and m >= 5 and m < 15:
        r = True

    else:
        r = False    



print("Pontos de atributo consistentes com a classe escolhida:", r)
