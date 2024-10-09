#coding: utf-8
#leitura em linha de valores
a,b,c = input().split()

a = int(a)
b = int(b)
c = int(c)

maiorAB = (a+b+abs(a-b))/2
maiorABC = int((maiorAB+c+abs(maiorAB-c))/2)
#print(maiorAB)
print(f"{maiorABC} eh o maior")