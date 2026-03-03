#IMPORTAR CLASES CONTENIDAS
from MODELO import Log_empleado,Log_cliente

#CLASE CONTENEDORA

class Empresa:
    def __init__(self,nombreEmppresaEmple,nombreEmpresaCli):
        
        self.NombreE=Log_cliente.cliente(nombreEmppresaEmple)
        self.NombreC=Log_empleado.empleado(nombreEmpresaCli)
        