#christian
import datetime
import crud

def subMenu():
    try:
        menu2 = int(input(
                    """
                    Selecciona una tabla:
                    ------------------------
                   |    1.-Departamentos    |
                   |    2.-Empleados        |
                   |    3.-Proyectos        |
                   |                        | 
                   |    0.-Salir            |
                    ------------------------
                    -> """))
        return menu2
    except ValueError:
        print("Oops!  That was no valid number.  Try again idiot")          


salida = "no"
while(salida != "si"):
    try:
        menu = int(input("""
            ¿Que desea hacer?
            ------------------------
           |     1.-Leer            | 
           |     2.-Insertar        | 
           |     3.-Actualizar      |
           |     4.-Eliminar        |   
           |     5.-Salir           |  
            ------------------------
            -> """
            )) 
        
        match (menu):
        
            case 1:
                menu2 = subMenu()
                    
                match(menu2):
                        case 1:
                            tabla = "Departamentos"
                            print(f"Leyendo {tabla}")
                            crud.lectura(tabla)
                        case 2:
                            tabla = "Empleados"
                            print(f"Leyendo {tabla}")
                            crud.lectura(tabla)
                        case 3:
                            tabla = "Proyectos"
                            print(f"Leyendo {tabla}")
                            crud.lectura(tabla)
                        case _:
                            print("Saliendo de aqui")
                       
            case 2:
                menu3 = subMenu()
                
                match(menu3):
                    case 1:
                        nombre = input("Introduzca el nombre del Departamento -> ")
                        ubicacion = input("Ahora introduce la ubicacion -> ")
                        crud.insertarDepto(nombre,ubicacion)
                    case 2:
                        print("Vas a insertar en Empleados") 
                        #depto = int(input("Introduce el codigo de depto -> "))
                        nombre = input("Introduzca el nombre del Empleado -> ")
                        ape1 = input("Ahora introduce el primer apellido -> ")
                        ape2 = input("Ahora introduce el segundo apellido -> ")
                        inicio = datetime.datetime.strptime(input("Ahora introduce cuando entrará a trabajar (yyyy-mm-dd) -> "),"%Y-%m-%d").date()
                        edad = int(input("Por último introduce la edad -> "))
                        crud.insertarEmple(nombre,ape1,ape2,inicio,edad)
                        
                    case 3:
                        print("Vas a insertar en Proyectos")
                        nombre = input("Introduzca el nombre del Proyecto -> ")
                        fecIni = datetime.datetime.strptime(input("Ahora introduce la fecha de inicio (yyyy-mm-dd) -> "),"%Y-%m-%d").date()
                        crud.insertarProye(nombre,fecIni)
                        
                    case _:
                        print("Saliendo o no implementado")
                
            case 3:
                menu4 = subMenu()
                
                match (menu4):
                    case 1:
                        print("Vas a actualizar Departamentos")
                        crud.lectura("Departamentos")
                        codigo = int(input("Introduce el Codigo del Departamento a actualizar -> "))
                        crud.lectura(codigo)
                        nombre = input("Ahora introduce el nuevo nombre del Departamento -> ")
                        ubicacion = input("Por último introduce la nueva Ubicacion -> ")
                        crud.actualizarDepto(nombre,ubicacion,codigo)
                    case 2:
                        print("Vas a actualizar Empleados")
                        crud.lectura("Empleados")
                        codEmp = int(input("Cual es el codigo del Empleado a actualizar? -> "))
                        crud.lecturaEmple(codEmp)
                        codigoDepto = input("Escriba el nuevo o el actual Departamento -> ")
                        nombre = input("Escribe el nuevo o actual nombre -> ")
                        ape1 = input("Introduce el nuevo o actual apellido -> ")
                        ape2 = input("Introduce el nuevo o actual segundo apellido -> ")
                        fecFin = datetime.datetime.strptime(input("Introduce o no la fecha de finalizacion en la empresa (yyyy-mm-dd) -> "),"%Y-%m-%d").date()
                        edad = input("Introduce por ultimo la edad nueva o actual -> ")
                        crud.actualizarEmple(codigoDepto,nombre,ape1,ape2,fecFin,edad,codEmp)
                        
                    case 3:
                        print("Vas a actualizar en Proyectos")
                        crud.lectura("Proyectos")
                        codProye = int(input("Cual es el codigo del Proyecto a actualizar? -> "))
                        crud.lecturaProye(codProye)
                        nombre = input("Introduce el nuevo o actual nombre del Proyecto -> ")
                        fechaFin = input("Ahora introduce o no la fecha de Fin de Proyecto (yyyy-mm-dd) -> ")
                        if(fechaFin != ""):
                            datetime.datetime.strptime(fechaFin,"%Y-%m-%d").date()
                        else:
                            fechaFin = None
                            
                        crud.actualizarProye(codProye,nombre,fechaFin)
                        
                    case _:
                        print("Saliendo o no implementado")
            case 4:
                menu5 = subMenu()
                
                match (menu5):
                    case 1:
                        print("Vas a eliminar un Departamento")
                        crud.lectura("Departamentos")
                        codigo = int(input("Introduce el Codigo a Eliminar -> "))
                        print("ELIMINANDO DEPARTAMENTO -> ")
                        crud.lecturaDepto(codigo)
                        crud.eliminarDepto(codigo)
                    case 2:
                        print("Vas a eliminar un Empleado")
                        crud.lectura("Empleados")
                        codigo = int(input("Introduce el Codigo a Eliminar -> "))
                        print("ELIMINANDO EMPLEADO -> ")
                        crud.lecturaEmple(codigo)
                        crud.eliminarEmple(codigo)
                    case 3:
                        print("Vas a eliminar un Proyecto")
                        crud.lectura("Proyectos")
                        codigo = int(input("Introduce el codigo a eliminar -> "))
                        print("EXTERMINANDO PROYECTO ->")
                        crud.lecturaProye(codigo)
                        crud.eliminarProyec(codigo)
                        
                    case _:
                        print("Saliendo o no implementado")                       

            case _:
                print("Saliendo ...")
                
                salida = "si"

    except ValueError:
        print("Oops!  That was no valid number.  Try again idiot...")

crud.cursor.close()
print("Adiós, no vuelvas más!.")
