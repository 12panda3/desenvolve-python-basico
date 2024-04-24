


n1 = int(input("Digite dois números: "))
n2 = int(input())

n3 = int(n1 + n2)

n3 = n3 % 2

if n3 != 0:
    print("O resultado é impar")

else:
    print("O resultado é par")