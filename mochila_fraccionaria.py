import time #libreria para el tiempo
import matplotlib.pyplot as plt


def mochila_fraccionaria(capacidad,objetos):
    objetos.sort(key=lambda x: x[0]/x[1], reverse=True)  #ordenar por valor/peso
    total_objetos=0.0
    mochila=[]
    for valor,peso in objetos:
        if capacidad >= peso:   #si el oobejtos se puede guardar completamente
            mochila.append((valor,peso))
            total_objetos += valor
            capacidad -=peso  
            #el objeto pesa mas de la capacidad de la mochila
        else:
            fracc= capacidad/peso
            mochila.append((valor*fracc, peso*fracc))
            total_objetos += valor*fracc
            break

    return total_objetos, mochila
    
def experimento1():
    inicio= time.time()
    objetos=[(5,10), (1,15), (1,8), (3,15)]
    capacidad=35
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento2():
    inicio= time.time()
    objetos=[(1,2), (3,4), (4,3), (3,2)]
    capacidad=50
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento3():
    inicio= time.time()
    objetos=[(5,6), (6,7), (7,8), (8,9)]
    capacidad=35
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento4():
    inicio= time.time()
    objetos=[(1,10), (2,8), (3,7), (4,6)]
    capacidad=50
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento5():
    inicio= time.time()
    objetos=[(1,1), (2,2), (3,3), (4,4)]
    capacidad=35
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento6():
    inicio= time.time()
    objetos=[(6,1), (2,9), (7,1), (9,9)]
    capacidad=100
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento7():
    inicio= time.time()
    objetos=[(1,8), (8,7), (9,5), (1,3)]
    capacidad=35
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento8():
    inicio= time.time()
    objetos=[(5,8), (8,2), (5,3), (7,2)]
    capacidad=70
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento9():
    inicio= time.time()
    objetos=[(8,9), (1,5), (2,9), (4,9)]
    capacidad=100
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def experimento10():
    inicio= time.time()
    objetos=[(9,7), (6,2), (1,2), (5,7)]
    capacidad=35
    total_objetos, mochila = mochila_fraccionaria(capacidad, objetos)
    print("el total de objetos es ",total_objetos," y la mochila quedo ",mochila)
    fin= time.time()
    tiempo_ejecutado = fin - inicio
    print("tiempo de ejecucion: ",tiempo_ejecutado)
    grafica(capacidad)

def grafica(capacidad):
    plt.title(f'Mochila con capacidad {capacidad}')
    plt.xlabel('Valor')
    plt.ylabel('Peso')
    plt.legend()
    plt.show()

    
if __name__=='__main__':

    experimento1()
    
   