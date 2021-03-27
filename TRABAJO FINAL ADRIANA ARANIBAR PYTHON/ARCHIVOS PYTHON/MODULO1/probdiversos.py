#1
while(True):
    try:
        capital = float(input("Ingresar cantidad a depositar: "))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        break
i = 0.04

for t in range(1,4):
    a1 = capital * ((1+ i)**t)
    print(f"La cantidad del {t} año es: {a1:.2f}")

#2
import math
def val_num(coef):
    while True :
        try:
            n = float(input(f"Ingrese el coeficiente {coef}: "))
            return n
        except:
            print("Hay un error, usted debe introducir bien el número")
a = val_num('a')
b = val_num('b')
c = val_num('c')
if a != 0:
    
    d = math.pow(b,2) - 4 * a * c
    
    if d >= 0:
        x1 = (-b + math.sqrt(d) ) / 2
        x2 = (-b - math.sqrt(d) ) / 2
        
        print(f'Soluciones x1: {x1}, x2: {x2}')
    else:
        print('Ecuación no presenta solución real')
else:
    print('No es una ecuación de 2do grado')