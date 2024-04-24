


a = int(input("Digite um ano e descubra se ele é bissexto! "))

if (((a % 4) == 0) and ((a % 100) != 0)) or ((a%400) == 0):
    print("Bissexto!")

else:
    print("Não Bissexto!")