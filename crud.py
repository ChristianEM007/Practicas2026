import pyodbc

try:
    conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "DATABASE=DBPracticas;"  
    "UID=soporte;"
    "TrustServerCertificate=yes;"
    )
    if conn:
        print("Conectado correctamente")
except: pass
    
cursor = conn.cursor()

#------------------------------------------------------------------- Lecturas -------------------------------------------------------------------
def lectura(tabla):
    query = f"SELECT * FROM {tabla}"
    cursor.execute(query)
    filas = cursor.fetchall()
    return filas
    
    
def lecturaDepto(codigo):
    print("...")
    cursor.execute(f"SELECT * FROM Departamentos Where codDepto = {codigo}")
    for row in cursor.fetchall():
        print(" ",row)
    print("...")

def lecturaEmple(codigo):
    print("...")
    cursor.execute(f"SELECT * FROM Empleados Where codEmpleado = {codigo}")
    for row in cursor.fetchall():
        print(" ",row)
    print("...")
    
def lecturaProye(codigo):
    print("...")
    cursor.execute(f"SELECT * FROM Proyectos Where codProyecto = {codigo}")
    for row in cursor.fetchall():
        print(" ",row)
    print("...")
    
def lecturaRol(codigo):
    print("...")
    cursor.execute(f"SELECT * FROM Roles Where codRol = {codigo}")
    for row in cursor.fetchall():
        print(" ",row)
    print("...")
    
def lecturaDetalle(codigoE,codigoP,rol):
    print("...")
    cursor.execute(f"SELECT * FROM DealleProyectos Where codEmple = {codigoE} and codProye = {codigoP} and rol = {rol}")
    for row in cursor.fetchall():
        print(" ",row)
    print("...")
    
#------------------------------------------------------------------- Inserciones -------------------------------------------------------------------
def insertarDepto(nombre,ubicacion):
    try:
        cursor.execute("INSERT INTO Departamentos(nomDepto,ubicacion) values(?,?)",
                (nombre,ubicacion,)
                )
        conn.commit()
        print("Insertado perfectamente")
    except pyodbc.Error as e:
        print(f"Ooops FATAL ERROR -> {e}")
    
def insertarEmple(depto,nombre,ape1,ape2,fecIni,edad):
    try:
        cursor.execute("INSERT INTO Empleados(codDepto,nomEmpleado,ape1Empleado,ape2Empleado,fecIniEmp,edad) values(?,?,?,?,?,?)",
                (depto,nombre,ape1,ape2,fecIni,edad,)
                    )
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error as e:
        print(f"Ooops los campos fecha o edad estan mal -> {e}")

def insertarProye(nombre,fecIni):
    try:
        cursor.execute("INSERT INTO Proyectos(nomProyecto,fechaInicio) values(?,?)",
                       (nombre,fecIni))
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error:
        print("Ooops el campo fecha puede estar FATAL")
    
def insertarRol(nombre,descrip):
    try:
        cursor.execute("INSERT INTO Roles(nomRol,descripcion) values(?,?)",
                       (nombre,descrip))
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error as e:
        print(f"Ooops FATAL ERROR -> {e}")

def insertaDetalle(codEmple,codProye,rol,horas):
    try:
        cursor.execute("INSERT INTO DetalleProyectos(codEmple,codProye,rol,horasAsignadas) values(?,?,?,?)",
                    (codEmple,codProye,rol,horas) 
                    )
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error as e:
        print(f"Ooops FATAL ERROR -> {e}")
        
#------------------------------------------------------------------- Actualizaciones -------------------------------------------------------------------
def actualizarDepto(nombre,ubicacion,codigo):
    cursor.execute("UPDATE Departamentos SET nomDepto = ?, ubicacion = ? WHERE codDepto = ?",
               (nombre,ubicacion,codigo,)
              )
    conn.commit()
    print("Actualizado satisfactoriamente")
    
def actualizarEmple(codigoDepto,nombre,ape1,ape2,inicio,fecFin,edad,codEmp):
    cursor.execute("UPDATE Empleados SET codDepto = ?, nomEmpleado = ?, ape1Empleado = ?, ape2Empleado = ?, fecIniEmp = ?, fecIniEmp = ?, edad = ?  WHERE codEmpleado = ?",
               (codigoDepto,nombre,ape1,ape2,inicio,fecFin,edad,codEmp,)
              )
    conn.commit()
    print("Actualizado satisfactoriamente")

def actualizarProye(codProye,nombre,fechaFin):
    cursor.execute("UPDATE Proyectos SET nomProyecto = ?, fechaFin = ? WHERE codProyecto = ?",
                   (nombre,fechaFin,codProye)
                   )
    conn.commit()
    print("Actualizado satisfactoriamente")
    
def actualizarRol(nombre,descripcion,codigo):
    cursor.execute("UPDATE Roles SET nomRol = ?, descripcion = ? WHERE codRol = ?",
                   (nombre,descripcion,codigo)
                   )
    conn.commit()
    print("Actualizado satisfactoriamente")
    
def actualizaDetalle(codEmple,codProye,rol,horas):
    cursor.execute("UPDATE DetalleProyectos SET horasAsignadas = ?, WHERE codEmple = ? and codProye = ? and rol = ?",
                   (horas,codEmple,codProye,rol))
    conn.commit()
    print("Actualizado satisfactoriamente")
    
#------------------------------------------------------------------- Eliminaciones -------------------------------------------------------------------
def eliminarDepto(codigo):
    try:
        cursor.execute("DELETE FROM Departamentos WHERE codDepto = ?",
                    (codigo,)
                )
        conn.commit()
        print(f"{codigo} Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy En el Departamento {codigo} tienes por lo menos a 1 empleado")
    
def eliminarEmple(codigo):
    try:
        cursor.execute("DELETE FROM Empleados WHERE codEmpleado = ?",
                    (codigo,)
                )
        conn.commit()
        print(f"{codigo} Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy Tienes al Empleado {codigo} añadido a uno o varios DetalleProyectos")
    
def eliminarProyec(codigo):
    try:
        cursor.execute("DELETE FROM Proyectos WHERE codProyecto = ?",
                    (codigo,)
                    )
        conn.commit()
        print(f"{codigo} Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy Tienes el Proyecto {codigo} añadido a DetalleProyectos")
        
def eliminarRol(codigo):
    try:
        cursor.execute("DELETE FROM Roles WHERE codRol = ?",
                    (codigo,)
                    )
        conn.commit()
        print(f"{codigo} Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy Tienes el rol {codigo} añadido a DetalleProyectos")

def eliminarDetalle(codEmple,codProye,rol):
    try:
        cursor.execute("DELETE FROM DetalleProyectos WHERE codEmple = ? and codProye = ? and rol = ?",
                        (codEmple,codProye,rol))
        conn.commit()
        print("Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy FATAL ERROR in DetalleProyectos -> {e}")

