#IMPORTAR LAS CALSES A USAR
from MODELO import Log_empleado,Log_cliente,Log_directivo,Log_empresa

#IMPORTAR LIBRERIA
import os


# INICIALIZAR VARIABLES
bandera=True
opc=1


#CREAR FUNCIONES

#validar opc
def validaciones_opc(opc,valor_min,valor_max):
    while opc<valor_min or opc>valor_max:
        print("Opcion no valida")
        opc=int(input("Selecciones nuevamente una opcion que este dentro del menu :"))
    return opc


#FUNCIONES PARA EPMPLEADOS
#pedir datos empleado
def datos_empleado():
    #crar diccionario
    dicci_empleado={}
    
    nom=input("-Ingrese el nombre del empleado : ").upper()
    dicci_empleado["Nombre"]=nom
    
    edad=int(input("\n-Ingrese la edad del empleado : "))
    while edad<=0:
        print("\n*La edad no pude ser negativa ni igual a 0")
        edad=int(input(" Ingrese nuevamente la edad:"))
    dicci_empleado["Edad"]=edad
    
    sueldo_bruto=float(input("\n-Ingrese el sueldo bruto (COP) : "))
    while sueldo_bruto<=0:
        print(" \n*El sueldo no puede ser negativo o igual a 0.")
        sueldo_bruto = float(input(" Ingrese nuevamente el sueldo : "))  
    dicci_empleado["SueldoBruto"]=sueldo_bruto
    
    return dicci_empleado,nom,edad,sueldo_bruto

#busqueda empleado
def buscar_empleado():
    nombre=input("Ingrese el nombre del empleado a buscar :").upper()
                                    
    encontradoE=None
    for dicci_buscar in lista_empleado:
        if dicci_buscar["Nombre"]==nombre:
            encontradoE=dicci_buscar
            break
    if encontradoE:
        print("")
        print("\t\tEMPLEADO ENCONTRADO\n")
        print("NOMBRE       : {}".format(encontradoE["Nombre"]))
        print("EDAD         : {}".format(encontradoE["Edad"]))
        print("SUELDO BRUTO :${}".format(encontradoE["SueldoBruto"]))
    else:
        print("")
        print("\t\tEL EMPLEADO NO EXISTE EN LA LISTA\n")
        os.system("pause")
        encontradoE=False
    
    return encontradoE
        
    

#FUNCIONES PARA DIRECTIVOS
#pedir datos directivo  
def datos_directivo():
    #crear diccionario
    dicci_directivos={}
    
    nom=input("-Ingrese el nombre del directivo :").upper()
    dicci_directivos["Nombre"]=nom
    
    edad=int(input("\n-Ingrese la edad del directivo :"))
    while edad<=0:
        print("\n*La edad no puede ser negativa ni igual a 0")
        edad=int(input(" Ingrese nuevamente la edad : "))   
    dicci_directivos["Edad"]=edad
    
    sueldo_bruto=float(input("\n-Ingrese el sueldo bruto (COP) : "))
    while sueldo_bruto<=0:
        print(" \n*El sueldo no puede ser negativo o igual a 0.")
        sueldo_bruto = float(input(" Ingrese nuevamente el sueldo : "))
    dicci_directivos["SueldoBruto"]=sueldo_bruto
    
    print("\n-Indique la categoria del directivo")
    print("\t1.Alto")
    print("\t2.Medio")
    print("\t3.Bajo\n")
    categoria=int(input("Selecione una de las opciones :"))
    while categoria<=0 or categoria>=4:
        print("\n*Opcion no valida")
        categoria=int(input(" Selecione nuevamente una de las 3 alternativas :"))
    
    if categoria==1:
        nivel="ALTO"
        dicci_directivos["NivelCategoria"]=nivel
    elif categoria==2:
        nivel="MEDIO"
        dicci_directivos["NivelCategoria"]=nivel
    elif categoria==3:
        nivel="BAJO"
        dicci_directivos["NivelCategoria"]=nivel
    
    return dicci_directivos,nom,edad,sueldo_bruto,nivel

#busqueda directivo
def buscar_directivo():
    nombre=input("Ingrese el nombre del directivo a buscar :").upper()
                                    
    encontradoD=None
    for dicci_buscar in lista_directivos:
        if dicci_buscar["Nombre"]==nombre:
            encontradoD=dicci_buscar
            break
    if encontradoD:
        print("")
        print("\t\tDIRECTIVO ENCONTRADO\n")
        print("NOMBRE       : {}".format(encontradoD["Nombre"]))
        print("EDAD         : {}".format(encontradoD["Edad"]))
        print("SUELDO BRUTO :${}".format(encontradoD["SueldoBruto"]))
        print("CATEGORIA    : {}".format(encontradoD["NivelCategoria"]))
    else:
        print("")
        print("\t\tEL EMPLEADO NO EXISTE EN LA LISTA\n")
        os.system("pause")
        encontradoD=False
        
    return encontradoD

#FUNCIONES PARA CLIENTES
#registarar cliente
def registrocliente():
    #crear diccionario
    dicci_clientes={}
    
    nom=input("-Ingrese el nombre del cliente :").upper()
    dicci_clientes["Nombre"]=nom
    
    edad=int(input("\n-Ingrese la edad del cliente :"))
    while edad<=0:
        print("\n*La edad no puede ser negativa ni igual a 0")
        edad=int(input(" Ingrese nuevamente la edad : "))   
    dicci_clientes["Edad"]=edad
    
    empresa=input("\n-Escriba el nombre de la empresa a la que se comunico :").upper()
    dicci_clientes["Empresa"]=empresa
    
    tel=int(input("\n-Registre el numero de contacto del cliente :"))
    while tel<0:
        print("\n*El numero de contacto no puede ser negativo")
        tel=int(input(" Ingrese nuevamente el numero de telefofno :"))
    dicci_clientes["Telefono"]=tel
    
    return dicci_clientes,nom,edad,empresa,tel

def buscar_cliente():
    nombre=input("Ingrese el nombre del cliente a buscar :").upper()
                                    
    encontradoC=None
    for dicci_buscar in lista_clientes:
        if dicci_buscar["Nombre"]==nombre:
            encontradoC=dicci_buscar
            break
    if encontradoC:
        print("")
        print("\t\CLIENTE ENCONTRADO\n")
        print("NOMBRE       : {}".format(encontradoC["Nombre"]))
        print("EDAD         : {}".format(encontradoC["Edad"]))
        print("EMPRESA      : {}".format(encontradoC["Empresa"]))
        print("TELEFONO     : {}".format(encontradoC["Telefono"]))
    else:
        print("")
        print("\t\tEL CLIENTE NO EXISTE EN LA LISTA\n")
        os.system("pause")
        encontradoC=False
        
    return encontradoC
    
    
    
#CREAR DICCIONARIOS
lista_empleado=[]
lista_directivos=[]
lista_clientes=[]

#INICIO CODIGO PRINCIPAL

while opc!=3:
    os.system("cls")
    print("\t\t\t***************************")
    print("\t\t\t*   ORGANISACION ALECRU   *")
    print("\t\t\t***************************\n")
    print("\t-Bienvenido a la seccion general")
    print("\t ¿A que area desea entrar?\n")
    print("1. Administrativa")
    print("2. Cliente")
    print("3. Cerrar por completo el programa\n")
    opc=int(input("Seleccione una opcion :"))
    opc=validaciones_opc(opc,1,3)
    
    #ADMINISTRADOR
    if opc==1:
        os.system("cls")
        contraseña=int(123)
        print("\t\t\t*****************************")
        print("\t\t\t*     ZONA DE VALIDACION    *")
        print("\t\t\t*****************************\n")
        print("\t-Antes de darle acceso al area administrativa")
        print("\t Usted debe ingresar la contraseña, tendra solo 3 intentos")
        print("\t La contraseña es 123\n")
        usu=int(input("Este es su primer intento, ingrese la contraseña : "))
        if usu!=contraseña:
            os.system("cls")
            print("\nCONTRASEÑA INCORRECTA")
            usu=int(input("Este es su segundo intento, ingrese nuevamente la contraseña :"))
            
            if usu!=contraseña:
                os.system("cls")
                print("\nCONTRASEÑA INCORRECTA")
                usu=int(input("Este es su ULTIMO intento, ingrese nuevamente la contraseña :"))
                if usu!=contraseña:
                    os.system("cls")
                    print("")
                    print("\t\t\tACCESO DENEGADO")
                    os.system("pause")

                       
        if usu==contraseña:
            os.system("cls")
            while opc!=6:
                print("\t\t\t***************************")
                print("\t\t\t*   AREA ADMINISTRATIVA   *")
                print("\t\t\t***************************\n")
                print("\t-Le damos la bienvenida al area administrativa")
                print("\t En esta area puede hacer lo siguiente para empleados y directivos")
                print("\t ¿Que desea realizar?\n")
                print("1. Agregar")
                print("2. Ver lista ")
                print("3. Buscar")
                print("4. Modificar ")
                print("5. Eliminar ")
                print("6. Volver al menu anterior para: \n")
                print("\t-Ingresar al area de clientes ")
                print("\t-Salir del programa\n")
                opc=int(input("Selecciones una opcion :"))
                opc=validaciones_opc(opc,1,6)
                os.system("cls")
                #///////////////////////////////////////////////////////////////////// INICIO AREA ADMINISTRATIVA ////////////////////////////////////////////////////////////////////////
                if opc==1:
                    os.system("cls")
                    while opc!=3:
                        print("\t\t\t**************************")
                        print("\t\t\t*   ZONA DE AGREGACION   *")
                        print("\t\t\t**************************\n")
                        print("\t-Seleccione a quien vamos a agregar :\n")
                        print("1. Empleado")
                        print("2. Directivo")
                        print("3. Volver al menu anterior para:\n")
                        print("\t-Ver listas")
                        print("\t-Buscar")
                        print("\t-Modificar ")
                        print("\t-Eliminar ")
                        print("\t-Volver al menu de entrada: \n")
                        opc=int(input("Selecciones una opcion :"))
                        opc=validaciones_opc(opc,1,3)
                        os.system("cls")
                        #///////////////////////////////////////////// INICIO DE ZONA AGRAGACION///////////////////////////////////
                        
                        #AGREGAR EMPLEADO
                        if opc==1:
                            while bandera==True:
                                os.system("cls")
                                print("\t\t\t**************************")
                                print("\t\t\t*    AGREGAR EMPLEADO    *")
                                print("\t\t\t**************************\n")
                                
                                #funcion parametrizada
                                print("Ingrese Los siguientes datos para registrar el empleado :\n")
                                dicci_empleado,nom,eda,sueldo_bruto=datos_empleado()
                                
                                #guardar diccionario en lista
                                lista_empleado.append(dicci_empleado)
                                
                                #instanciar
                                empleado=Log_empleado.empleado(dicci_empleado["Nombre"],dicci_empleado["Edad"],dicci_empleado["SueldoBruto"])
                                empleado.CalcularSalarioNeto(dicci_empleado)
                                print("-"*50)
                                os.system("pause")
                                os.system("cls")
                                print("\tDATOS REGISTRADOS DEL EMPLEADO\n")
                                empleado.MostrarEmpleado()
                                
                                bandera=input("\n¿Desea ingresar otro Empleado? (SI/NO):").upper()in["SI","S"]
                                os.system("cls")
                            bandera=True
                            
                            
                        #AGREGAR DIRECTIVO
                        if opc==2:
                            while bandera==True:
                                print("\t\t\t***************************")
                                print("\t\t\t*    AGREGAR DIRECTIVO    *")
                                print("\t\t\t***************************\n")
                                print("Ingrese Los siguientes datos para registrar el directivo :\n")
                                #funcion parametrizada
                                dicci_directivos,nom,eda,sueldo_bruto,categoria=datos_directivo()
                                
                                #guardar diccionario en lista
                                lista_directivos.append(dicci_directivos)
                                
                                #instanciar
                                directivo=Log_directivo.directivo(dicci_directivos["Nombre"],dicci_directivos["Edad"],dicci_directivos["SueldoBruto"],dicci_directivos["NivelCategoria"])
                                directivo.CalcularSalarioNeto(dicci_directivos)
                                print("-"*50)
                                os.system("pause")
                                os.system("cls")
                                print("\tDATOS REGISTRADOS DEL DIRECTIVO\n")
                                directivo.MostrarDirectivo()
                                
                                bandera=input("\n¿Desea ingresar otro directivo? (SI/NO):").upper()in["SI","S"]
                                os.system("cls")
                            bandera=True
                                
                        if opc==3:
                            opc=1
                            break
                        
                    
                    #///////////////////////////////////////////// FIN DE ZONA AGRAGACION///////////////////////////////////
                    
                
                
                if opc==2:
                    while opc!=3 :
                        os.system("cls")
                        print("\t\t\t**************************")
                        print("\t\t\t*     ZONA DE LISTAS     *")
                        print("\t\t\t**************************\n")
                        print("\t-¿Que listas desea ver?\n")
                        print("1. Empleado")
                        print("2. Directivo")
                        print("3. Volver al menu anterior para:\n")
                        print("\t-Agregar")
                        print("\t-Buscar")
                        print("\t-Modificar ")
                        print("\t-Eliminar ")
                        print("\t-Volver al menu de entrada: \n")
                        opc=int(input("Selecciones una opcion :"))
                        opc=validaciones_opc(opc,1,3)
                        os.system("cls")
                        #/////////////////////////////// INICIO ZONA DE LISTAS /////////////////////////////////////////////// 
                        
                        #LISTAS DE EMPLEADOS
                        if opc==1:
                            if lista_empleado==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO EMPLEADOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                print("\t\t\t***************************")
                                print("\t\t\t*      LISTA EMPLEADOS     *")
                                print("\t\t\t***************************\n")
                                empleado.MostrarEmpleadocompleto(lista_empleado)
                                print("")
                                os.system("pause")
                                os.system("cls")
                                
                        #LISTAS DIRECTIVOS
                        if opc==2:
                            if lista_directivos==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO DIRECTIVOS\n")
                                os.system("pause")
                            else:
                                print("\t\t\t*****************************")
                                print("\t\t\t*      LISTA DIRECTIVOS     *")
                                print("\t\t\t*****************************\n")
                                directivo.MostrarDirectivoCompleto(lista_directivos)
                                print("")
                                os.system("pause")
                                
                        if opc==3:
                            opc=1
                            break
                             
                        #/////////////////////////////// FIN ZONA DE LISTAS ///////////////////////////////////////////////
                
                if opc==3:
                    opc=1
                    while opc!=3:
                        os.system("cls")
                        print("\t\t\t****************************")
                        print("\t\t\t*     ZONA DE BUSQUEDA     *")
                        print("\t\t\t****************************\n")
                        print("\t -¿A quienes desea buscar?\n")
                        print("1. Empleado")
                        print("2. Directivo")
                        print("3. Volver al menu anterior para:\n")
                        print("\t-Agregar")
                        print("\t-Ver Listas")
                        print("\t-Modificar ")
                        print("\t-Eliminar ")
                        print("\t-Volver al menu de entrada: \n")
                        opc=int(input("Selecciones una opcion :"))
                        opc=validaciones_opc(opc,1,3)
                        os.system("cls")
                        #/////////////////////////////// INICIO ZONA DE BUSQUEDA ///////////////////////////////////////////////
                        #BUSCAR EMPLEADO
                        if opc==1:
                            if lista_empleado==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO EMPLEADOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                while bandera==True:
                                    print("\t\t\t*********************************")
                                    print("\t\t\t*     BUSQUEDA DE EMPLEADOS     *")
                                    print("\t\t\t*********************************\n")
                                    #funcion de retorno
                                    encontradoE=buscar_empleado()  
                                    bandera=input("\n¿Desea buscar otro empleado? (SI/NO):").upper()in["SI","S"]
                                    os.system("cls")
                                bandera=True
                                
                        #BUSCAR DIRECTIVO       
                        if opc==2:
                            if lista_directivos==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO DIRECTIVOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                while bandera==True:
                                    print("\t\t\t*********************************")
                                    print("\t\t\t*     BUSQUEDA DE EMPLEADOS     *")
                                    print("\t\t\t*********************************\n")
                                    #funcion de retorno
                                    encontradoD=buscar_directivo()    
                                    bandera=input("\n¿Desea buscar otro directivo? (SI/NO):").upper()in["SI","S"]
                                    os.system("cls")
                                bandera=True
                        
                        if opc==3:
                            opc=1
                            break
                                      
                            
                        #/////////////////////////////// FIN ZONA DE BUSQUEDA ///////////////////////////////////////////////
                
                if opc==4:
                    while opc!=3:
                        os.system("cls")
                        print("\t\t\t********************************")
                        print("\t\t\t*     ZONA DE MODIFICACION     *")
                        print("\t\t\t********************************\n")
                        print("\t -¿A quienes desea modificar?\n")
                        print("1. Empleado")
                        print("2. Directivo")
                        print("3. Volver al menu anterior para:\n")
                        print("\t-Agregar")
                        print("\t-Ver Listas")
                        print("\t-Buscar ")
                        print("\t-Eliminar ")
                        print("\t-Volver al menu de entrada: \n")
                        opc=int(input("Selecciones una opcion :"))
                        opc=validaciones_opc(opc,1,3)
                        os.system("cls")
                        #/////////////////////////////// INICIO ZONA DE MODIFICACION ///////////////////////////////////////////////
                        #MODIFICAR EMPLEADO
                        if opc==1:
                            if lista_empleado==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO EMPLEADOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                while bandera==True:
                                    
                                    print("\t\t\t*********************************")
                                    print("\t\t\t*     MODIFICACION EMPLEADO     *")
                                    print("\t\t\t*********************************\n")
                                    #funcion de retorno
                                    encontradoE=buscar_empleado()
                                    if encontradoE==False:
                                        break
                                    else:
                                        print("\nIngrese los nuevos datos del empleado:\n")
                                        dicci_empleado,nom,eda,sueldo_bruto=datos_empleado()
                                        
                                        #actualizar lista
                                        encontradoE["Nombre"]=nom
                                        encontradoE["Edad"]=eda
                                        encontradoE["SueldoBruto"]=sueldo_bruto
                                        print("\nEL EMPLEADO FUE ACTUALIZADO EN LA LISTA !!!")
                                    
                                    bandera=input("\n¿Desea modificar otro empleado? (SI/NO):").upper()in["SI","S"]
                                    os.system("cls")
                                bandera=True
                        
                        #MODIFICAR DIRECTIVO
                        if opc==2:
                            if lista_directivos==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO DIRECTIVOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                while bandera==True:
                                    print("\t\t\t**********************************")
                                    print("\t\t\t*     MODIFICACION DIRECTIVO     *")
                                    print("\t\t\t**********************************\n")
                                    #funcion retorno
                                    encontradoD=buscar_directivo()
                                    if encontradoD==False:
                                        break
                                    else:
                                        print("\nIngrese los nuevos datos del directivo:\n")
                                        dicci_directivos,nom,eda,sueldo_bruto,nivel=datos_directivo()
                                    
                                        #actualizar lista
                                        encontradoD["Nombre"]=nom
                                        encontradoD["Edad"]=eda
                                        encontradoD["SueldoBruto"]=sueldo_bruto
                                        encontradoD["NivelCategoria"]=nivel
                                            
                                        print("\nDIRECTIVO ACTUALIZADO CON EXITO !!!")

                                    bandera=input("\n¿Desea modificar otro directivo? (SI/NO):").upper()in["SI","S"]
                                    os.system("cls")
                                bandera=True
                            
                        if opc==3:
                            opc=1
                            break   
                        #/////////////////////////////// FIN ZONA DE MODIFICACION ///////////////////////////////////////////////
                        
                
                if opc==5:
                    while opc!=3:
                        os.system("cls")
                        print("\t\t\t*******************************")
                        print("\t\t\t*     ZONA DE ELIMINACION     *")
                        print("\t\t\t*******************************\n")
                        print("\t -¿A quienes desea eliminar?\n")
                        print("1. Empleado")
                        print("2. Directivo")
                        print("3. Volver al menu anterior para:\n")
                        print("\t-Agregar")
                        print("\t-Ver Listas")
                        print("\t-Buscar")
                        print("\t-Modificar ")
                        print("\t-Volver al menu de entrada: \n")
                        opc=int(input("Selecciones una opcion :"))
                        opc=validaciones_opc(opc,1,3)
                        os.system("cls")
                        #/////////////////////////////// INICIO ZONA DE ELIMINACION ///////////////////////////////////////////////
                        #ELIMINAR EMPLEADOS
                        if opc==1:
                            if lista_empleado==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO EMPLEADOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                while bandera==True:
                                    print("\t\t\t************************************")
                                    print("\t\t\t*     ELIMINACION DE EMPLEADOS     *")
                                    print("\t\t\t************************************\n")
                                    #funcion retorno
                                    encontradoE=buscar_empleado()
                                    if encontradoE==False:
                                        break
                                    else:
                                        lista_empleado.remove(encontradoE)
                                        print("\nEL EMPLEADO SE ELIMINO EXITOSAMENTE !!!")
                                    
                                    
                                    bandera=input("\n¿Desea eliminar otro empleado? (SI/NO):").upper()in["SI","S"]
                                    os.system("cls")
                                bandera=True
                                
                        #ELIMINAR DIRECTIVOS        
                        if opc==2:
                            if lista_directivos==[]:
                                print("")
                                print("\t\tNO SE HAN REGISTRADO DIRECTIVOS\n")
                                os.system("pause")
                                os.system("cls")
                            else:
                                while bandera==True:
                                    print("\t\t\t************************************")
                                    print("\t\t\t*     ELIMINACION DE DIRECTIVOS     *")
                                    print("\t\t\t************************************\n")
                                    #funcion de retorno
                                    encontradoD=buscar_directivo()
                                    if encontradoD==False:
                                        break
                                    else:
                                        lista_directivos.remove(encontradoD)
                                        print("\nEL DIRECTIVO SE ELIMINO CORRECTAMENTE !!!")
                                    
                                    bandera=input("\n¿Desea eliminar otro directivo? (SI/NO):").upper()in["SI","S"]
                                    os.system("cls")
                                bandera=True
                                
                        if opc==3:
                            opc==1
                            break
                            
                        #/////////////////////////////// FIN ZONA DE ELIMINACION ///////////////////////////////////////////////
                
                if opc==6:
                    opc=1
                    break
                    
                    
                    
                    
            
            
        
        #///////////////////////////////////////////////////////////////////// FIN AREA ADMINISTRATIVA ////////////////////////////////////////////////////////////////////////////
    
    #CLIENTES    
    if opc==2:
        os.system("cls")
        while opc!=5:
            print("\t\t\t***************************")
            print("\t\t\t*     AREA DE CLIENTES    *")
            print("\t\t\t***************************\n")
            print("\t-Bienvenido al area de clientes")
            print("\t ¿Que desea realizar con los clientes?\n")
            print("1. Registrar")
            print("2. Ver lista")
            print("3. Modificar")
            print("4. Eliminar")
            print("5. Volver al menu anterior para:\n")
            print("\t-Entrar al area administrativa")
            print("\t-Cerrar por completo el programa\n")
            opc=int(input("Selecciones una opcion :"))
            opc=validaciones_opc(opc,1,5)
            os.system("cls")
            #///////////////////////////////////////////////////////////////////// INICIO AREA CLIENTES ////////////////////////////////////////////////////////////////////////////
            #AGREGAR
            if opc==1:
                os.system("cls")
                while bandera==True:
                    print("\t\t\t*******************************")
                    print("\t\t\t*     REGISTRAR UN CLIENTE     *")
                    print("\t\t\t*******************************\n")
                    print("Ingrese los siguientes datos para registrar al cliente\n")
                    #funcion de retorno
                    dicci_clientes,nom,edad,empresa,tel=registrocliente()
                    
                    #guardar en lista
                    lista_clientes.append(dicci_clientes)
                    
                    #instanciar
                    cliente=Log_cliente.cliente(dicci_clientes["Nombre"],dicci_clientes["Edad"],dicci_clientes["Empresa"],dicci_clientes["Telefono"])
                    os.system("cls")
                    print("\tDATOS REGISTRADOS DEL EMPLEADO\n")
                    cliente.MostrarCliente()
                    
                    
                    bandera=input("\n¿Desea registrar otro cliente? (SI/NO):").upper()in["SI","S"]
                    os.system("cls")
                bandera=True
            
            #VER LISTA
            if opc==2:
                if lista_clientes==[]:
                    print("")
                    print("\t\tNO SE HAN REGISTRADO CLIENTES\n")
                    os.system("pause")
                    os.system("cls")
                else:
                    print("\t\t\t**********************************")
                    print("\t\t\t*         LISTADO CLIENTES       *")
                    print("\t\t\t**********************************\n")
                    cliente.MostrarClienteCompleto(lista_clientes)
                    print("")
                    os.system("pause")
                    os.system("cls")
                    
                
            #MODIFICAR
            if opc==3:
                if lista_clientes==[]:
                    print("")
                    print("\t\tNO SE HAN REGISTRADO CLIENTES\n")
                    os.system("pause")
                    os.system("cls")
                else:
                    while bandera==True:
                        print("\t\t\t**********************************")
                        print("\t\t\t*     MODIFICAR DATOS CLIENTE    *")
                        print("\t\t\t**********************************\n")
                        #funcion de retorno
                        encontradoC=buscar_cliente()
                        if encontradoC==False:
                            os.system("cls")
                            break
                        else:
                            print("\nIngrese los nuevos datos del cliente:\n")
                            dicci_clientes,nom,edad,empresa,tel=registrocliente()
                            
                            #actualizar lista
                            encontradoC["Nombre"]=nom
                            encontradoC["Edad"]=edad
                            encontradoC["Empresa"]=empresa
                            encontradoC["Telefono"]=tel
                            print("\nEL CLIENTE FUE ACTUALIZADO EN LA LISTA !!!")

                        bandera=input("\n¿Desea modificar otro cliente? (SI/NO):").upper()in["SI","S"]
                        os.system("cls")
                    bandera=True
                
            #ELIMINAR
            if opc==4:
                if lista_clientes==[]:
                    print("")
                    print("\t\tNO SE HAN REGISTRADO CLIENTES\n")
                    os.system("pause")
                    os.system("cls")
                else:
                    while bandera==True:
                        print("\t\t\t**********************************")
                        print("\t\t\t*     ELIMINACION DE CLIENTE     *")
                        print("\t\t\t**********************************\n")
                        #funcion de retorno
                        encontradoC=buscar_cliente()
                        if encontradoC==False:
                            os.system("cls")
                            break
                        else:
                            lista_clientes.remove(encontradoC)
                            print("\nEL CLIENTE SE ELIMINO CORRECTAMENTE !!!")

                        bandera=input("\n¿Desea eliminar otro cliente? (SI/NO):").upper()in["SI","S"]
                        os.system("cls")
                    bandera=True
                
            if opc==5:
                opc=1
                break
            
            #///////////////////////////////////////////////////////////////////// FIN AREA CLIENTES ////////////////////////////////////////////////////////////////////////////

        
    if opc==3:
        os.system("cls")
        print("Gracias por usar nuestro programa")
        print("Cerrando programa..........\n")
        break



