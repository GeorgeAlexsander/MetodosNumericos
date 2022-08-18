# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 20:53:36 2022

@author: george
"""

from math import exp, log
import math 

def seleciona_funcao_desejada():
   return int(input('Digite 1 para utilizar os dados da Tarefa semanal, exercicio 3 \nDigite 2, caso queira valores personalizados \nValor escolhido: '))
    
def seta_dados_da_integral(seta_f):
    if seta_f == 1: return exp(1), exp(1)+1, 30
    elif seta_f == 2:
        return eval(input('Digite o limitante inferior: ')), eval(input('Digite o limitante superior: ')), int(input('Digite o valor de n (norma de partição do intervalo): '))

def seta_integral_utilizada(seta_f):
    if seta_f == 1: return '1/(x*log(x))'
    elif seta_f == 2: 
        return str(input('Digite a função que deseja utilizar: '))

def seta_metodo():
    return int(input('Digite 1 para Met.dos Trapézios \nDigite 2 para Met. de Simpson \nDigite sua escolha: '))
               
def calcula_valor_de_f(x, f):
    return eval(f)

def retorna_maior_valor_de_f(a,b,h,f_de_teste):
    x=a
    max_value_f=0.0  
    while(x<b):
        teste_de_max_f=eval(f_de_teste) 
        if abs(teste_de_max_f) > abs(max_value_f):
            max_value_f = abs(teste_de_max_f)
            x_com_maior_valor_de_f = x
        x+=h        
    return x_com_maior_valor_de_f
   

def lim_do_erro_Trapezios(a,b,n):
    h= (b-a)/n
    f_duas_linhas='(2*log(x)**2+3*log(x)+2)/(x**3*log(x)**3)'
    #f_duas_linhas='-2*exp(-x)*math.cos(x)' #versao do exemplo da apostila
    x = retorna_maior_valor_de_f(a,b,h,f_duas_linhas)
    limitante_do_erro = abs((((b-a)*(h**2.0))/12.0)*eval(f_duas_linhas))
    return limitante_do_erro

def lim_do_erro_Homer_Simpson(a,b,n):
    h = (b-a)/n
    
    f_quatro_linhas='2*(12*log(x)**4+25*log(x)**3+35*log(x)**2+30*log(x)+12)/(x**5*log(x)**5)'
    x = retorna_maior_valor_de_f(a,b,h,f_quatro_linhas)
    limitante_do_erro= -(n*h**5/180)*eval(f_quatro_linhas)
    return limitante_do_erro

def metodos_dos_Trapezios(a,b,f, n, seta_f):
    integral = 0
    h= (b-a)/n
    
    for k in range (1, n):
        integral += calcula_valor_de_f(a + k*h, f)
        
    integral *= 2
    integral += (calcula_valor_de_f(a, f)+calcula_valor_de_f(b, f))
    integral *= (h/2)
    
    return integral

def metodo_de_Homer_Simpson(a,b,f,n):
    h= (b-a)/n
    soma_odd, soma_even = 0,0
    
    for k in range(1,n,2):
        soma_odd += calcula_valor_de_f(a + k*h, f)
    for k in range(2,n,2):
        soma_even += calcula_valor_de_f(a + k*h, f)
        
    return (h/3) * (calcula_valor_de_f(a, f) + 4*soma_odd + 2*soma_even + calcula_valor_de_f(b, f))
        
seta_f = seleciona_funcao_desejada()
a, b, n = seta_dados_da_integral(seta_f)
f = seta_integral_utilizada(seta_f)
metodo = seta_metodo()

if(metodo == 1):
    resultado = metodos_dos_Trapezios(a,b,f, n, seta_f)
elif(metodo == 2):
    resultado = metodo_de_Homer_Simpson(a,b,f, n)

print('O valor aproximado da integral é: ', resultado)

if(seta_f == 1):
    if(metodo == 1):
        lim_do_erro = lim_do_erro_Trapezios(a,b,n)
              
    elif(metodo == 2):
        lim_do_erro = lim_do_erro_Homer_Simpson(a,b,n)
    print('O valor do limitante do erro é: ', lim_do_erro)
    print('O valor verdadeiro da integral é: ', log((log(exp(1)+1))))
    print('O erro verdadeiro é: ', abs(log(log(exp(1)+1))-(resultado)))