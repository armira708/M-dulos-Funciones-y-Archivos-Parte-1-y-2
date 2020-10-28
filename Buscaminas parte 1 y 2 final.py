#Universidad Del Valle de Guatemala
#Andrés Armira 201183
#Módulos, funciones y Archivos parte 1 y 2
#Algoritmos y programación básica sección 50

import random
import os


def tablero1(f, c, v): #Se crea una matriz con filas y columnas agregado al valor que le ponemos
    tabla = []
    for i in range(f):
        tabla.append([])
        for j in range(c):
            tabla[i].append(v)
    return tabla

def tablero(tablero1):#Se muestran las filas y columnas con la matriz

    print("* * * * * * * * * * * * * * * * *")
    for f in tablero1:
        print("*", end=" ")
        for elem in f:
            print(elem, end= " ")
        print("*")
    print("* * * * * * * * * * * * * * * * * *")


def minas(tablero, minas, f, c):#Coloca en el tablero el número de minas
    minas_ocultas = []
    n = 0
    while n < minas:
        y = random.randint(0,f-1)
        x = random.randint(0,c-1)
        if tablero[y][x] != 9:
            tablero[y][x] = 9
            n += 1
            minas_ocultas.append((y,x))
    return tablero, minas_ocultas

def relleno(nver, ver, y, x, f, c, v):#Recorre las casillas cercanas, comprueba si son ceros y de ser así las descubre, recorre las cercanas a estas hasta encontrar pistas que también las descubre.
    
    ceros = [(y,x)]
    while len(ceros) > 0:
        y, x = ceros.pop()
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0 <= y+i <= f-1 and 0 <= x+j <= c-1:
                    if ver[y+i][x+j] == v and nver[y+i][x+j] == 0:
                        ver[y+i][x+j] = 0
                        if (y+i, x+j) not in ceros:
                            ceros.append((y+i, x+j))
                    else:
                        visible[y+i][x+j] = oculto[y+i][x+j]
    return ver
    

def pistas(tablero, f, c):#Recorre todos los valores posibles que corresponden adyacentes a la "y" y "x" y si no son minas se aumenta una unidad
    
    for y in range(f):
        for x in range(c):
            if tablero[y][x] == 9:
                for i in [-1, 0, 1]:
                    for j in [-1, 0, 1]:
                        if 0 <= y+i <= f-1 and 0 <= x+j <= c-1:
                            if tablero[y+i][x+j] !=9:
                                tablero[y+i][x+j] += 1
    return tablero
               
                        
def full_t(tablero, f, c, v):#Comprueba si el tablero no contiene una casilla con el valor visible inicial
    
    for y in range(f):
        for x in range(c):
            if tablero[y][x] == v:
                return False
    return True
                        

def presentacion():#Pantalla
    
    os.system("cls")
    
    print("***********************************************")
    print("*                                             *")
    print("*                 BUSCAMINAS                  *")
    print("*                                             *")
    print("*      W/A/S/D - controles para moverse       *")
    print("*                                             *")
    print("*                 R - revelar                 *")
    print("*                                             *")
    print("*           B/V - marcar/desmarcar            *")
    print("*                                             *")
    print("*                                             *")
    print("***********************************************")
    print("******INGRESE LAS OPCIONES EN MAYÚSCULA********")
    
def menu():#mueve o selecciona la opción del usuario
    
    print()
    opcion = input("¿W/S/A/D - M - B/V?")
    return opcion

def reemplazo(tablero):#Recorre todas las casillas del tablero y si una casilla es "0" cambia el valor por un espacio vacío 
    for i in range(12):
        for j in range(16):
            if tablero[i][j] == 0:
                tablero[i][j] = " "
    return tablero

c = 16
f = 12

ver = tablero1(f, c, "-")
nver = tablero1(f, c, 0)

nver, minas_ocultas = minas(nver, 15, f, c)

nver = pistas(nver, f, c)


presentacion()#Ficha inicial con tablero

y = random.randint(2, f-3)
x = random.randint(2, c-3)

real = ver[y][x]
ver[y][x] = "o"

os.system("cls")

tablero(ver)#Primer bucle

minas_marcadas = []

juego = True

while juego:
    move = menu()
    if move == "W":
        if y == 0:
            y = 0
        else:
            ver[y][x] = real
            y -= 1
            real = ver[y][x]
            ver[y][x] = "o"
            
    elif move == "S":
        if y == f-1:
            y = f-1
        else:
            ver[y][x] = real
            y += 1
            real = ver[y][x]
            ver[y][x] = "o"
            
    elif move == "A":
        if x == 0:
            x = 0
        else:
            ver[y][x] = real
            x -= 1
            real = ver[y][x]
            ver[y][x] = "o"
            
    elif move == "D":
        if x == c-1:
            x = c-1
        else:
            ver[y][x] = real
            x += 1
            real = ver[y][x]
            ver[y][x] = "o"
    
    elif move == "B":
        if real == "-":
            ver[y][x] = "$"
            real = ver[y][x]
            if (y,x) not in minas_marcadas:
                minas_marcadas.append((y,x))
                
    elif move == "V":
        if real == "$":
           ver[y][x] = "-"
           real = ver[y][x]
           if (y,x) in minas_marcadas:
               minas_marcadas.remove((y,x))
               
    elif move == "R":
        if nver[y][x] == 9:
            ver[y][x] = "M"
            juego = False
            
        elif nver[y][x] !=0:
            ver[y][x] = nver[y][x]
            real = ver[y][x]
            
        elif nver[y][x] == 0:
            ver[y][x] = 0
            ver = relleno(nver, ver, y, x, f, c, "-")
            ver = reemplazo(ver) 
            real = ver[y][x]
                   
    os.system("cls")
    
    tablero(ver)
    
    gana = False
    
    if full_t(ver, f, c, "-") and \
       sorted(minas_ocultas) == sorted(minas_marcadas) and \
       real != "-":
       gana = True
       juego = False
       
if not gana:
    print("**************************")
    print("********¡PERDISTE!********")
    print("**************************")
    
else:
    print("**************************")
    print("********¡GANASTE!*********")
    print("**************************")
    
    
        
    
            
        
    


