

#definição de variáveis
l, a, m2, pm2, tpm2 = 0, 0, 0, float(0), 0

#solicitação de dados
l = int(input("Digite a largura do terreno "))
a = int(input("Digite a altura do terreno "))
pm2 = int(input("Qual o preço do metro quadrado? (m2) "))

#calculo com os dados obtidos
m2 = int(a*l)
tpm2 = float(m2*pm2)

#demonstração do resultado
print("O valor será avaliado em", tpm2, "reais")