

v = int(input("Insira um valor: "))

c = v//100
v -= (c*100)
print(c, "nota(s) de R$100,00")

b = v//50
v -= (b*50)
print(b, "nota(s) de R$50,00")

n = v//20
v -= (n*20)
print(n, "nota(s) de R$20,00")

r = v//5
v -= (r*5)
print(r, "nota(s) de R$10,00")

a = v//10
v -= (a*10)
print(a, "nota(s) de R$5,00")

s = v//2
v -= (s*2)
print(s, "nota(s) de R$2,00")

f = v//1
v -= (f*1)
print(f, "nota(s) de R$1,00")