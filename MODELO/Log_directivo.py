#IMPORTAR CLASE PADRE
from MODELO import Log_empleado
#CLASE HIJA
class directivo(Log_empleado.empleado):

    def __init__(self,nom2,eda2,sueldo2,catego):
        super().__init__(nom2,eda2,sueldo2)
        self.__categoria=catego

    #metodos set y get
    def setcategoria(self,categoria):
        self.__categoria=categoria

    def getcategoria(self):
        return self.__categoria
    
    #metodos propios
    def MostrarDirectivo(self):
        self.MostrarEmpleado()
        print("Categoria del directivo: {} ".format(self.getcategoria()))
        
    def MostrarDirectivoCompleto(self,lista_directivos):
        print("{:^20} | {:^20} | {:^20} | {:^20} | {:^20}".format("NOMBRE","EDAD","SUELDO BRUTO","SUELDO NETO","CATEGORIA"))
        print("-"*110)
        for directivo in lista_directivos:
            print("{:^20} | {:^20} | {:^20} | {:^20} | {:^20}".format(directivo["Nombre"],directivo["Edad"],directivo["SueldoBruto"],directivo["SalarioNeto"],directivo["NivelCategoria"]))
            
    
        

