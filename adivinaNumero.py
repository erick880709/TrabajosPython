import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int (input('Ingrese un numero de 1 a 100'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido<numero_aleatorio:
            print('Elige un numero mas grande')
        else:
            print ('Elige un numero mas pequeñ')
        numero_elegido = int (input('Ingrese un numero de 1 a 100'))    

    print ('ganaste')



if __name__ == '__main__':
    run()