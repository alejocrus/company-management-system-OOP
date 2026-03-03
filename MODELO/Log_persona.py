#CLASE PADRE

class persona:
    def __init__(self,nom,eda):
        self.__nombre=nom
        self.__edad=eda
        
    #Metodos get y set
    
    def setnombre(self,nombre):
        self.__nombre=nombre
    
    def setedad(self,edad):
        self.__edad=edad
    
    def getnombre(self):
        return self.__nombre
    
    def getedad(self):
        return self.__edad
    
    
    #metodos propios
    
    def MostrarPersona(self):
        print("Nombre                 : {}".format(self.getnombre()))
        print("Edad                   : {}".format(self.getedad()))
        