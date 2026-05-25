#christian
import datetime
import crud

def subMenu():
    try:
        menu2 = int(input(
                    """
                    Selecciona una tabla:
                    ---------------------------- 
                   |    1.-Departamentos        |
                   |    2.-Empleados            |
                   |    3.-Proyectos            |
                   |    4.-Roles                |
                   |    5.-Detalle Proyectos    |
                   |                            |
                   |    0.-Salir                |
                    ---------------------------- 
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
           |     1.-LEER            | 
           |     2.-INSERTAR        | 
           |     3.-ACTUALIZAR      |
           |     4.-ELIMINAR        |   
           |     0.-Salir           |  
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
                        case 4:
                            tabla = "Roles"
                            print(f"Leyendo {tabla}")
                            crud.lectura(tabla)
                        case 5:
                            tabla = "DetalleProyectos"
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
                    
                    case 4:
                        print("Vas a insertar en Roles")    
                        nombre = input("Introduzca el nombre del Rol -> ")    
                        descrip = input("Y ahora introduce una descripción -> ")
                        crud.insertarRol(nombre,descrip)
                        
                    case 5: 
                        print("Vas a insertar en Detalle Proyectos")
                        
                        print("Tabla de Proyectos:")
                        crud.lectura("Proyectos")
                        codProye = input("Introduce el codigo de Proyecto -> ")
                        
                        print("Tabla de Empleados:")
                        crud.lectura("Empleados")
                        codEmp = input("Ahora introduzca el codigo del empleado -> ")
                        
                        print("Tabla de Roles:")
                        crud.lectura("Roles")
                        codRol = input("Introduce ahora el codigo de Rol -> ")
                        horas = input("Por ultimo intdroduce las horas asignadas que tendra este empleado -> ")
                        crud.insertaDetalle(codEmp,codProye,codRol,horas)
                    
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
                        
                    case 4:
                        print("Vas a actualizar en Roles")
                        crud.lectura("Roles")
                        codRol = int(input("Introduce el codigo a actualizar -> "))
                        crud.lecturaRol(codRol)
                        nombre = input("Introduce ahora el nuevo o actual nombre -> ")
                        descrip = input("Por último introduce la descripcion nueva o actual -> ")
                        
                        crud.actualizarRol(nombre,descrip,codRol)
                        
                    case 5:
                        print("Vas a actualizar en Detalle Proyectos")
                        crud.lectura("DetalleProyectos")
                        codEmple = input("Introduce el codigo de Empleado")
                        codProye = input("Ahora el codigo de Proyecto")
                        rol = input("Introduce el codigo de Rol")
                        crud.lecturaDetalle(codEmple,codProye,rol)
                        horas = input("Introduce las horas que quería cambiar -> ")
                        crud.actualizaDetalle(codEmple,codProye,rol,horas)
                        
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
                    case 4:
                        print("Vas a eliminar un Rol")
                        crud.lectura("Roles")
                        codigo = int(input("Introduce el codigo a eliminar -> "))
                        print("EXTERMINANDO ROL ->")
                        crud.lecturaRol(codigo)
                        crud.eliminarRol(codigo)
                    
                    case 5:
                        print("Vas a eliminar un Detalle Proyecto")
                        crud.lectura("DetalleProyectos")
                        codEmp = input("Introduce el codigo de empleado -> ")
                        codProye = input("Ahora introduce el de proyecto -> ")
                        rol = input("Y por último introduce el rol -> ")
                        crud.eliminarDetalle(codEmp,codProye,rol)
                        
                    case _:
                        print("Saliendo o no implementado")                       

            case _:
                print("Saliendo ...")
                
                salida = "si"

    except ValueError:
        print("Oops!  That was no valid number.  Try again idiot...")

crud.cursor.close()
print("Adiós, no vuelvas más!.")
