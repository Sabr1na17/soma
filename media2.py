# -*- coding: utf-8 -*-

a = float(input())
b = float(input())
c = float(input())
peso1 = 2
peso2 = 3
peso3 = 5
media_ponderada = (a*peso1+b*peso2+c*peso3)/(peso1+peso2+peso3)
saida = "MEDIA = {0:.1f}".format(media_ponderada)
print(saida)
