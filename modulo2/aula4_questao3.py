

input("Digite o nome do produto 1 ")
p1 = float(input("Digite o preço unitário do produto 1 "))
q1 = int(input("Digite a quantidade comprada do produto 1 "))

input("Digite o nome do produto 2 ")
p2 = float(input("Digite o preço unitário do produto 2 "))
q2 = int(input("Digite a quantidade comprada do produto 2 "))

input("Digite o nome do produto 3 ")
p3 = float(input("Digite o preço unitário do produto 3 "))
q3 = int(input("Digite a quantidade comprada do produto 3 "))

pt = float((p1*q1) + (p2*q2) + (p3*q3))
print(f"Total: R${pt:,.2f}")