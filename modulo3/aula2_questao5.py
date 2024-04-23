


s = input("Digite seu gênero (M ou F) ")
i = int(input("Digite sua idade: "))
t = int(input("Digite seu tempo de contribuição: "))
r = bool(False)

if s == "m":
    if (i >= 65) or (t >= 30) or (i >= 60 and t >= 25):
        r = True
        print(r)

    else:
        r = False
        print(r)



if s == "f":
    if (i >= 60) or (t >= 30) or (i >= 60 and t >= 25):
        r = True
        print(r)

    else:
        r = False
        print(r)

     