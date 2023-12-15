import random
import matplotlib.pyplot as plt

#Generar una tirada aleatoria
def girar():
    resultado=random.randint(0,36)
    return resultado


#Casillas
#        0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6   
tablero=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0]

#Color
rojo=0
negro=0

#Par o Impar
par=0
impar=0

#Tercios
tercio1=0
tercio2=0
tercio3=0

#Mitades
mitad1=0
mitad2=0

#Filas
fila1=0
fila2=0
fila3=0

#Numero de tiradas simuladas
tiradasInicio=10000
#Saldo total
saldoInicio=50

#Partidas
partidas=5

#Lista para almacenar los saldos al final de cada tirada
saldoTiradas = []

#Costo total de cada tirada
costo=sum(tablero)+rojo+negro+par+impar+tercio1+tercio2+tercio3+mitad1+mitad2+fila1+fila2+fila3


while partidas!=0:
    tiradas=tiradasInicio
    saldo=saldoInicio
    saldoTiradas.append(saldo)

    while tiradas!=0 or saldo<=0:
        #Comprobar si hay saldo para hacer la apuesta
        if saldo<costo:
            saldo=0
            saldoTiradas.append(saldo)
            break
        
        #Actualizar saldo, tiradas y ganado despues de la apuesta
        saldo=saldo-costo
        tiradas=tiradas-1
        ganado=0

        #Simular giro ruleta
        resultado=girar()

        #Casilla
        ganado=ganado+tablero[resultado]*36

        #0
        if resultado==0:
            saldo=saldo+ganado
            saldoTiradas.append(saldo)
            continue

        #Color
        if resultado==1 or resultado==3 or resultado==5 or resultado==7 or resultado==9 or resultado==12 or resultado==14 or resultado==16 or resultado==18 or resultado==19 or resultado==21 or resultado==23 or resultado==25 or resultado==27 or resultado==30 or resultado==32 or resultado==34 or resultado==36:
            ganado=ganado+rojo*2
        else:
            ganado=ganado+negro*2

        #Par o Impar
        if resultado%2==0:
            ganado=ganado+par*2
        else:
            ganado=ganado+impar*2

        #Tercios
        if resultado < 13:
            ganado=ganado+tercio1*3
        elif resultado < 25:
            ganado=ganado+tercio2*3
        else:
            ganado=ganado+tercio3*3

        #Mitades
        if resultado < 19:
            ganado=ganado+mitad1*2
        else:
            ganado=ganado+mitad2*2

        #Filas
        if resultado%3==0:
            ganado=ganado+fila3*3
        elif resultado%3==2:
            ganado=ganado+fila2*3
        else:
            ganado=ganado+fila1*3
            
        #Actualizar saldo en funcion de lo ganado y añadirlo a la lista del progreso
        saldo=saldo+ganado
        saldoTiradas.append(saldo)

    #Grafica con el progreso del saldo
    plt.plot(range(1, len(saldoTiradas) + 1), saldoTiradas, label=f'Partida {partidas}')

    #Reiniciar la lista para almacenar los saldos al final de cada tirada
    saldoTiradas.clear()
    partidas=partidas-1

#Grafica
plt.title('Evolución del Saldo')
plt.xlabel('Tiradas')
plt.ylabel('Saldo')
plt.legend()
plt.show()