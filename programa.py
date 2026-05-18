#christian
import pyodbc
import datetime

try:
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=***************;"
    "DATABASE=DBPracticas;"  
    "UID=soporte;"
    "PWD=************;"
    "TrustServerCertificate=yes;"
    )
    if conn:
        print("Conectado correctamente")
except: pass
finally:
    conn.close
    
cursor = conn.cursor()
def lectura(tabla):
    print("Buscando ...")
    cursor.execute(f"SELECT * FROM {tabla}")
    for row in cursor.fetchall():
        print(" ",row)
    print("Listo")
    
def insertarDepto(nombre,ubicacion):
    cursor.execute("INSERT INTO Departamentos(nomDepto,ubicacion) values(?,?)",
               (nombre,ubicacion)
               )
    conn.commit()
    print("Insertado perfectamente")
    
def insertarEmple(nombre,ape1,ape2,fecIni,edad):
    try:
        cursor.execute("INSERT INTO Empleados(nomEmpleado,ape1Empleado,ape2Empleado,fecIniEmp,edad) values(?,?,?,?,?)",
                (nombre,ape1,ape2,fecIni,edad)
                    )
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error:
        print("Ooops los campos fecha o edad estan mal")
    
def actualizarDepto(nombre,ubicacion,codigo):
    cursor.execute("UPDATE Departamentos SET nomDepto = ?, ubicacion = ? WHERE codDepto = ?",
               (nombre,ubicacion,codigo)
              )
    conn.commit()
    print("Actualizado satisfactoriamente")
    
def actualizarEmple(nombre):
    cursor.execute("UPDATE Departamentos SET  WHERE codEmpleado = ?",
               (nombre)
              )
    conn.commit()
    print("Actualizado satisfactoriamente")

def eliminar(codigo):
    cursor.execute("DELETE FROM Departamentos WHERE codDepto = ?",
                (codigo,)
            )
    conn.commit()
    print(f"{codigo} eliminado satisfactoriamente")


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
                            lectura(tabla)
                        case 2:
                            tabla = "Empleados"
                            print(f"Leyendo {tabla}")
                            lectura(tabla)
                        case 3:
                            tabla = "Proyectos"
                            print(f"Leyendo {tabla}")
                            lectura(tabla)
                        case _:
                            print("Saliendo de aqui")
                       
            case 2:
                menu3 = subMenu()
                
                match(menu3):
                    case 1:
                        nombre = input("Introduzca el nombre del Departamento -> ")
                        ubicacion = input("Ahora introduce la ubicacion -> ")
                        insertarDepto(nombre,ubicacion)
                    case 2:
                        print("Vas a insertar en Empleados") 
                        #depto = int(input("Introduce el codigo de depto -> "))
                        nombre = input("Introduzca el nombre del Empleado -> ")
                        ape1 = input("Ahora introduce el primer apellido -> ")
                        ape2 = input("Ahora introduce el segundo apellido -> ")
                        inicio = datetime.datetime.strptime(input("Ahora introduce cuando entrará a trabajar (yyyy-mm-dd) -> "),"%Y-%m-%d").date()
                        edad = int(input("Por último introduce la edad -> "))
                        insertarEmple(nombre,ape1,ape2,inicio,edad)
                                                
                    case _:
                        print("Saliendo o no implementado")
                
            case 3:
                menu4 = subMenu()
                
                match (menu4):
                    case 1:
                        print("Vas a actualizar Departamentos")
                        codigo = int(input("Introduce el Codigo del Departamento a actualizar -> "))
                        nombre = input("Ahora introduce el nuevo nombre del Departamento -> ")
                        ubicacion = input("Por último introduce la nueva Ubicacion -> ")
                        actualizarDepto(nombre,ubicacion,codigo)
                    case 2:
                        print("Vas a actualizar Empleados")
                        
                    case _:
                        print("Saliendo o no implementado")
            case 4:
                menu5 = subMenu()
                
                match (menu5):
                    case 1:
                        print("Vas a eliminar un Departamento")
                        codigo = int(input("Introduce el Codigo a Eliminar -> "))
                        eliminar(codigo)
                    case _:
                        print("Saliendo o no implementado")
                        

            case _:
                print("Saliendo")
                
                salida = "si"

    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    
cursor.close()

print("Adiós")
