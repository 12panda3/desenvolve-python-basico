


n1 = int(input())
n2 = int(input())
n3 = int(input())

m = int((n1 + n2 + n3) / 3)

if m >= 60:
    print("Aprovado")

else:
    if m >= 40: 
        print("Rexuperação")

    else:
        print("Reprovado")

print("Fim")