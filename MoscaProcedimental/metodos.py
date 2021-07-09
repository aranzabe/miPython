import random   

def iniciar(tablero, tam = 10):
    """Por defecto iniciaría un tablero con 10 posiciones a False. 
       Si queremos cambiar esto bastaría con llamar a la función indicando en el segundo argumento de cuanto quiero el tablero."""
    for i in range(tam):
        tablero[i] = False

def iniciar2(tam = 10):
    tablero = []
    for i in range(tam):
        tablero += [False]
    return tablero

def colocarMosca(tablero):
    #print(len(tablero))
    lt = len(tablero)
    pos = random.randint(0, lt - 1)
    # pos = random.randint(0, len(tablero) - 1)
    tablero[pos]=True

def manotazo(tablero, pos):
    qhp = 2
    if (tablero[pos] == True):
        qhp = 0
    else:
        #Miramos si está a la izquierda o a la derecha
        if (pos > 0):
            if (tablero[pos - 1] == True):
                qhp = 1
        if (pos < len(tablero) - 1):
            if (tablero[pos + 1] == True):
                qhp = 1
    return qhp

def revolotear(tablero):
    #Aquí da un error si llamamos a la función iniciar tablero. Ya que declara otra variable y la desvincula de la principal. tablero = iniciar2(len(tablero))
    #Sin embargo, de la siguiente manera sí funciona ok porque no defino otra variable con t = []
    iniciar(tablero,len(tablero))

    #Una tercera forma sería:
    # for i in range(0, len(tablero)-1):
    #     tablero[i] = False
    colocarMosca(tablero)
    # return tablero