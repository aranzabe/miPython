import generico, neo, smith, random

class Matrix:
    
    def __init__(self, tam = 5):
        self._mat=[]
        for i in range(tam):
            fila = [0]*tam
            self._mat.append(fila)
            
    # def getMatrix(self):
    #     return self._mat;
    
    def __str__(self):
        cad = ""
        for i in range(len(self._mat)):
            for j in range(len(self._mat[0])):
                if (self._mat[i][j]!=0):
                    cad += str(self._mat[i][j].resumen()) + "\t\t"
                else:
                    cad += "vacio" + "\t\t"
            cad += "\n"
        return cad
    
    def getFils(self):
        return len(self._mat)
    
    def getCols(self):
        return len(self._mat[0])
    
    def add(self, f, c, p):
        self._mat[f][c] = p
        
    def get(self, f, c):
        return self._mat[f][c]
    
  