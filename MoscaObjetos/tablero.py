import random   

class Tablero:
    #Como Python solo permite un constructor, usamos un argumento opcional: si se pone será el que sea y si no valdrá 10.
    def __init__(self, tam=10):
        """Por defecto crea un tablero de 10 posiciones."""
        self.__tablero = []
        for i in range(tam):
            self.__tablero += [False]
        
    
    def __iniciar(self, tam = 10):
        """Por defecto iniciaría un tablero con 10 posiciones a False. 
        Si queremos cambiar esto bastaría con llamar a la función indicando en el segundo argumento de cuanto quiero el tablero."""
        for i in range(tam):
            self.__tablero[i] = False


    def colocarMosca(self):
        #print(len(tablero))
        lt = len(self.__tablero)
        pos = random.randint(0, lt - 1)
        # pos = random.randint(0, len(tablero) - 1)
        self.__tablero[pos]=True

    def manotazo(self, pos):
        qhp = 2
        if (self.__tablero[pos] == True):
            qhp = 0
        else:
            #Miramos si está a la izquierda o a la derecha
            if (pos > 0):
                if (self.__tablero[pos - 1] == True):
                    qhp = 1
            if (pos < len(self.__tablero) - 1):
                if (self.__tablero[pos + 1] == True):
                    qhp = 1
        return qhp

    def revolotear(self):
        #Aquí da un error si llamamos a la función iniciar tablero. Ya que declara otra variable y la desvincula de la principal. tablero = iniciar2(len(tablero))
        #Sin embargo, de la siguiente manera sí funciona ok porque no defino otra variable con t = []
        self.__iniciar(len(self.__tablero))

        #Una tercera forma sería:
        # for i in range(0, len(tablero)-1):
        #     tablero[i] = False
        self.colocarMosca()
        # return tablero
        
    def __str__(self):
        return str(self.__tablero)