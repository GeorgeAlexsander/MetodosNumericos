# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:04:33 2022

@author: george
"""
from math import sqrt, exp, sin, pi
import math

def seleciona_funcao_desejada():
   return int(input('Digite 1 para utilizar os dados da Tarefa semanal, exercicio 4 \nDigite 2, caso queira valores personalizados \nValor escolhido: '))
    
def seta_dados_da_integral(seta_f):
    if seta_f == 1: return 0.0, pi/4.0
    elif seta_f == 2:
        return eval(input('Digite o limitante inferior: ')), eval(input('Digite o limitante superior: '))

def seta_integral_utilizada(seta_f):
    if seta_f == 1: return 'exp(3.0*x)*sin(2.0*x)'
    elif seta_f == 2: 
        return str(input('Digite a função que deseja utilizar: '))
        
def calcula_valor_de_f(x, f):
    return eval(f)

def quadratura_gaussiana_2p(a,b, f):
    x1 = -sqrt(3.0/5.0)+1
    x2 = 0
    x3 = sqrt(3.0/5.0)+1
    if a==-1 and b==1:
        integral= calcula_valor_de_f(x1, f) + calcula_valor_de_f(x2, f)
    else:
        #troca de variaveis p/ demais casos
        t1 = 0.5*((b-a)*x1 + a + b) 
        t2 = 0.5*((b-a)*x2 + a + b)
        t3 = 0.5*((b-a)*x3 + a + b)
        dt = (b-a)/2.0
        integral = ((5/9)*calcula_valor_de_f(t1, f)+(8/9)*calcula_valor_de_f(t2, f)+(5/9)*calcula_valor_de_f(t3, f))*dt
        print((5/9)*calcula_valor_de_f(t1, f))
        print((8/9)*calcula_valor_de_f(t2, f))
        print((5/9)*calcula_valor_de_f(t3, f))
   
    return integral


seta_f = seleciona_funcao_desejada()
a, b = seta_dados_da_integral(seta_f)
f = seta_integral_utilizada(seta_f)
    
resultado_da_integral=quadratura_gaussiana_2p(a,b,f)
print ('o resultado da integral é %f' %resultado_da_integral)

print('O erro verdadeiro é: ', abs((3*exp(3*pi/4)+2)/13-(resultado_da_integral)))