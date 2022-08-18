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
    #exp(4*x)*sin(6*x)/(1+x**2)
def quadratura_gaussiana_2p(a,b, f):
    x1 = -0.8611363116
    x2 = 0.8611363116
    x3 = -0.3399810436
    x4 = 0.3399810436
    if a==-1 and b==1:
        integral= calcula_valor_de_f(x1, f) + calcula_valor_de_f(x2, f)
    else:
        #troca de variaveis p/ demais casos
        t1 = 0.5*((b-a)*x1 + a + b) 
        t2 = 0.5*((b-a)*x2 + a + b)
        t3 = 0.5*((b-a)*x3 + a + b)
        t4 = 0.5*((b-a)*x4 + a + b)
        const1= 0.3478548451
        const2= 0.6521451549
        dt = (b-a)/2.0
        integral = ((const1)*calcula_valor_de_f(t1, f)+(const1)*calcula_valor_de_f(t2, f)+(const2)*calcula_valor_de_f(t3, f)+(const2)*calcula_valor_de_f(t4, f))*dt
        print((const1)*calcula_valor_de_f(t1, f))
        print((const1)*calcula_valor_de_f(t2, f))
        print((const2)*calcula_valor_de_f(t3, f))
        print((const2)*calcula_valor_de_f(t4, f))
   
    return integral


seta_f = seleciona_funcao_desejada()
a, b = seta_dados_da_integral(seta_f)
f = seta_integral_utilizada(seta_f)
    
resultado_da_integral=quadratura_gaussiana_2p(a,b,f)
print ('o resultado da integral é %f' %resultado_da_integral)

#print('O erro verdadeiro é: ', abs((3*exp(3*pi/4)+2)/13-(resultado_da_integral)))