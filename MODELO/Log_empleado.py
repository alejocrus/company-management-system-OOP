#IMPORTAR CLASE PADRE
from MODELO import Log_persona

#CLASE HIJA

class empleado(Log_persona.persona):
    def __init__(self,nom1,eda1,sueldo_bruto1):
        super().__init__(nom1,eda1)
        self.__SueldoBruto=sueldo_bruto1
        
    #metodos set y get
    
    def setsueldo(self,sueldo):
        self.__SueldoBruto=sueldo
        
    def getsueldo(self):
        return self.__SueldoBruto
    
    #metodos propios
        
    def CalcularSalarioNeto(self,dicci_empleado):
        salud=0
        pension=0
        self.SalarioNeto=float(0)
        
        print(" -Se descontara 4% para su salud")
        print(" -Se descontara 4% para su pension")
        
        salud=(self.__SueldoBruto*4)/100
        pension=(self.__SueldoBruto*4)/100
        self.SalarioNeto=self.__SueldoBruto-salud-pension
        self.__SueldoBruto= "{:,.0f}".format(self.__SueldoBruto).replace(",",".")
        self.SalarioNeto= "{:,.0f}".format(self.SalarioNeto).replace(",",".")
        dicci_empleado["SueldoBruto"]=self.__SueldoBruto
        dicci_empleado["SalarioNeto"]=self.SalarioNeto
        
        
    def MostrarEmpleado(self):
        self.MostrarPersona()  
        print("Sueldo bruto (mensual) : ${}".format(self.getsueldo()))
        print("Su salario neto es de  : ${}".format(self.SalarioNeto))
        
    def MostrarEmpleadocompleto(self,lista_empleados):
        print("{:^20} | {:^20} | {:^20} | {:^20}".format("NOMBRE","EDAD","SUELDO BRUTO","SUELDO NETO"))
        print("-"*90)
        for empleado in lista_empleados:
            print("{:^20} | {:^20} | {:^20} | {:^20}".format(empleado["Nombre"],empleado["Edad"],empleado["SueldoBruto"],empleado["SalarioNeto"]))
            
        
        
        
        