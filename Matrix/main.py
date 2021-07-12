import persona, neo, smith, generico
import random, matrix, time

def factoriaLocalizacion():
    longitud = random.randint(0, 100)
    latitud = random.randint(0,100)
    alea = random.randint(1,4)
    ciudad = ""
    if (alea == 1):
        ciudad = "Madrid"
    elif (alea == 2):
        ciudad = "Barcelona"
    elif (alea == 3):
        ciudad = "NY"
    else: 
        ciudad = "Retuerta del Bullaque"
    
    localizacion =persona.Localizacion(longitud, latitud, ciudad)
    return localizacion

def factoriaPersonaGenerica():
    edad = random.randint(1,100)
    nombre = ""
    alea = random.randint(1,4)
    if (alea == 1):
        nombre = "Inma"
    elif (alea == 2):
        nombre = "Jose"
    elif (alea == 3):
        nombre = "Diego"
    else: 
        nombre = "Jaime"
    localizacion = factoriaLocalizacion()
    porMorir = random.randint(1,100)
    pers = generico.Generico(nombre, localizacion, edad, porMorir)
    return pers

def factoriaNeo():
    localizacion = factoriaLocalizacion()
    edad = random.randint(1,100)
    loCreo = random.randint(1,2)
    seLoCree = False
    if (loCreo == 1):
        seLoCree = True
    n = neo.Neo(localizacion, edad, seLoCree)
    return n

def factoriaSmith():
    localizacion = factoriaLocalizacion()
    edad = random.randint(1,100)
    porInf = random.randint(1,100)
    s = smith.Smith(localizacion,edad,porInf)
    return s

def factoriaRepositorio(tam = 200):
    repo = []
    for i in range(tam):
        repo += [factoriaPersonaGenerica()]
    return repo

def factoriaMatrix(repo):
    m = matrix.Matrix()
    filaAleatoria = random.randint(0, m.getFils() - 1)
    colAleatoria = random.randint(0, m.getCols() - 1)
    m.add(filaAleatoria, colAleatoria, factoriaNeo())
    salir = False
    while(not salir):
        filaAleatoria = random.randint(0, m.getFils() - 1)
        colAleatoria = random.randint(0, m.getCols() - 1)
        if (m.get(filaAleatoria, colAleatoria)==0):
            salir = True
            m.add(filaAleatoria, colAleatoria, factoriaSmith())
    for i in range(m.getFils()):
        for j in range(m.getCols()):
            if (m.get(i, j) == 0):
                m.add(i, j, repo.pop())
    return m

##################################################################################################
###################################### Programa principal ########################################
##################################################################################################
# Para probar la generación de objetos básicos
# l = [];
# p = factoriaPersonaGenerica()
# p2 = factoriaPersonaGenerica()
# p3 = factoriaPersonaGenerica()
# print(p)
# print(p2)
# print(p3)
# l += [p]
# l += [p2]
# l += [p3]

# n = factoriaNeo()
# print(n)
# l += [n]

# s = factoriaSmith()
# print(s)
# l += [s]


# for elemento in l:
#     print(elemento.resumen())
# print(persona.Persona.cuantasPersonasDefinidas())

#Para probar Matrix
# m = matrix.Matrix(4)
# m.add(0,2,factoriaNeo())
# m.add(1,1,factoriaSmith())
# m.add(2,2,factoriaPersonaGenerica())
# m.add(2,0,factoriaPersonaGenerica())
# m.add(3,0,factoriaPersonaGenerica())
# # print(m.getMatrix())
# print(m)
# print("Filas: ", str(m.getFils()))
# print("Columnas: ", str(m.getCols()))


#Para probar el repositorio
# repositorio = factoriaRepositorio(9)
# repositorio = factoriaRepositorio()
# for elemento in repositorio:
#     print(elemento)

##---------------------- Simulación --------------------------##
# Iniciamos el repositorio y Matrix
repositorio = factoriaRepositorio()
m = factoriaMatrix(repositorio)
print(m) 
# print(len(repositorio))

tiempo = 1
while(tiempo <= 300):  #cinco minutos de simulación
    # print("Cada segundo")
    for i in range(m.getFils()):
        for j in range(m.getCols()):
            if (isinstance(m.get(i,j), generico.Generico)): #Solo evaluaremos los personajes genéricos.
                if (m.get(i,j).getPorcentaje() < 30):
                    print("El personaje que había en " + str(i) + ", " + str(j) + " ha muerto de viejo.")
                    if (len(repositorio)==0): #Si el repositorio se vacía lo rellenamos de nuevo
                        repositorio = factoriaRepositorio()
                    m.add(i,j,repositorio.pop())
                else:
                    pers = m.get(i,j)
                    pers.setPorcentaje(int(pers.getPorcentaje() * 0.9))
                    m.add(i, j, pers)
    
    if (tiempo % 2 == 0): #cada 2 segundos
        # print("Cada 2 segundos")
        print("Actúa Smith")
        for f in range(m.getFils()):
            for c in range(m.getCols()):
                if (isinstance(m.get(f,c),smith.Smith)):
                    smithActual = m.get(f, c)
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if (f + i >= 0 and f + i < m.getFils() and c + j >= 0 and c + j < m.getCols()): #estamos dentro de los límites de Matrix
                                if (isinstance(m.get(f+i,c+j),generico.Generico)):
                                    aleatorio = random.randint(1, 100)
                                    if (aleatorio <= smithActual.getPorcentaje()):
                                        m.add(f + i, c + j, factoriaSmith())
                                    
                                    
    
    if (tiempo % 5 == 0): #cada 5 segundos
        print("Actúa Neo")
        for f in range(m.getFils()):
            for c in range(m.getCols()):
                if (isinstance(m.get(f,c),neo.Neo)):
                    neoActuando = m.get(f, c)
                    for i in [-1, 0, 1]:
                        for j in [-1, 0, 1]:
                            if (f + i >= 0 and f + i < m.getFils() and c + j >= 0 and c + j < m.getCols()): #estamos dentro de los límites de Matrix
                                if (isinstance(m.get(f+i,c+j),smith.Smith)):
                                    if (neoActuando.getMeLoCreo()):
                                        if (len(repositorio)==0): #Si el repositorio se vacía lo rellenamos de nuevo
                                            repositorio = factoriaRepositorio()
                                        m.add(f + i, c + j, repositorio.pop())
    
    print(m)
    time.sleep(1)
    tiempo += 1
    
