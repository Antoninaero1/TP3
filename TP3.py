# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:44:59 2021

@author: antoc
"""
from math import sin
from math import log #sur python log=ln
from math import exp
from math import cos
from math import tan

def f1(x):
    return x**4+3*x-9
def f1der(x):
    return 4*x**3+3
def f2(x):
    return 3*cos(x)-2-x
def f2der(x):
    return -3*sin(x)-1
def f3(x):
    return x*exp(x)-7
def f3der(x):
    return exp(x)+x*exp(x)
def f4(x):
    return exp(x)-x-10
def f4der(x):
    return exp(x)-1
def f5(x):
    return 2*tan(x)-x-5
def f5der(x):
    return ((2)/(cos(x)*cos(x)))-1
def f6(x):
    return 3-exp(x)+x**2
def f6der(x):
    return 2*x-exp(x)
def f7(x):
    return 3*x+4*log(x)-7
def f7der(x):
    return 3+(4/x)
def f8(x):
    return x**4-2*x**2+4*x-17
def f8der(x):
    return 4*x**3-4*x+4
def f9(x):
    return exp(x)-2*sin(x)-7
def f9der(x):
    return exp(x)-2*cos(x)
def f10(x):
    return log(x**2+4)*exp(x)-10
def f10der(x):
    return exp(x)*(log(x**2+4)+((2*x)/(x**2+4)))

def Newton (f,fder,X0,epsilon,Nitermax):
    """ Programme de la méthode de Newton qui compare l'ecart entre [xold] et g(xn) [xnew] 
    Avec g(xn)=xold-(f(xold))/(f'(xold))
    cet écart est comparé à epsilon qui nous permet de définir la précision 
    de la solution alpha tel que f(alpha)=0
    on inplémente aussi un compteur d'itération pour sorir de la boucle si il n'y a pas de solution trouvé au bout de Niermax essai
    cela nous permet aussi de savoir à quelle vitesse la méthode de newton trouve alpha 
    """
    n=0
    xold=X0
    xnew=1
    erreur=-(f(xold)/fder(xold))
    while abs(erreur)>epsilon and n<Nitermax:
        xnew=xold-(f(xold)/fder(xold))
        n+=1
        erreur=xnew-xold
        xold=xnew
        print(n)
    return xnew
    
print(Newton(f1,f1der,1,1e-10,5e4),'1')   # affiche alpha1 et le nombre d'itération pour la 1)

print(Newton(f1,f1der,-1.9,1e-10,5e4),'1') # affiche alpha2 et le nombre d'itération pour la 1)

print(Newton(f2,f2der,0.54,1e-10,5e4),'2')   # affiche alpha1 et le nombre d'itération pour la 2)

print(Newton(f2,f2der,-4,1e-10,5e4),'2') # affiche alpha2 et le nombre d'itération pour la 2)

print(Newton(f2,f2der,-2,1e-10,5e4),'2') # affiche alpha3 et le nombre d'itération pour la 2)

print(Newton(f3,f3der,1.5,1e-10,5e4),'3')   # affiche alpha et le nombre d'itération pour la 3)

print(Newton(f4,f4der,2.5,1e-10,5e4),'4')   # affiche alpha1 et le nombre d'itération pour la 4)

print(Newton(f4,f4der,-10,1e-10,5e4),'4') # affiche alpha2 et le nombre d'itération pour la 4)

print(Newton(f5,f5der,1.25,1e-10,5e4),'5')   # affiche alpha et le nombre d'itération pour la 5)

print(Newton(f6,f6der,1.9,1e-10,5e4),'6')   # affiche alpha et le nombre d'itération pour la 6)

print(Newton(f7,f7der,1.5,1e-10,5e4),'7')   # affiche alpha et le nombre d'itération pour la 7)

print(Newton(f8,f8der,2,1e-10,5e4),'8')   # affiche alpha1 et le nombre d'itération pour la 8)

print(Newton(f8,f8der,-2,1e-10,5e4),'8') # affiche alpha2 et le nombre d'itération pour la 8)

print(Newton(f9,f9der,1.8,1e-10,5e4),'9')   # affiche alpha et le nombre d'itération pour la 9)

print(Newton(f10,f10der,2,1e-10,5e4),'10')   # affiche alpha et le nombre d'itération pour la 10)

