#IMPORTAR CLASE PADRE
from MODELO import Log_persona

#CALSE HIJA
class cliente(Log_persona.persona):

    def __init__(self,nom1,eda1,NomEmpre,Tel):
        super().__init__(nom1,eda1)
        self.__NombreEmpresa=NomEmpre
        self.__telefono=Tel

    #metodos set y get
    
    def setNombreEmpresa(self,NomEmpre):
        self.__NombreEmpresa=NomEmpre

    def settelefono(self,tel):
        self.__telefono=tel
    
    def getNombreEmpresa(self):
        return self.__NombreEmpresa
    
    def gettelefono(self):
        return self.__telefono
    
    #metodos propios
    def MostrarCliente(self):
        self.MostrarPersona()
        print("Nombre de la empresa   : {}".format(self.getNombreEmpresa()))
        print("Telefono de contacto   : {}".format(self.gettelefono()))  
        
    def MostrarClienteCompleto(self,lista_clientes):
        print("{:^20} | {:^20} | {:^20} | {:^20}".format("NOMBRE","EDAD","EMPRESA","TELEFONO CONTAC."))
        print("-"*90)
        for cliente in lista_clientes:
            print("{:^20} | {:^20} | {:^20} | {:^20}".format(cliente["Nombre"],cliente["Edad"],cliente["Empresa"],cliente["Telefono"]))
