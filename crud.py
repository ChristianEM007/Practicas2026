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
finally:
    conn.close
    
cursor = conn.cursor()

# Lecturas -------------------------------------------------------------------
def lectura(tabla):
    print("Buscando ...")
    cursor.execute(f"SELECT * FROM {tabla}")
    for row in cursor.fetchall():
        print(" ",row)
    print("Listo")
    
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

# Inserciones -------------------------------------------------------------------
def insertarDepto(nombre,ubicacion):
    cursor.execute("INSERT INTO Departamentos(nomDepto,ubicacion) values(?,?)",
               (nombre,ubicacion,)
               )
    conn.commit()
    print("Insertado perfectamente")
    
def insertarEmple(nombre,ape1,ape2,fecIni,edad):
    try:
        cursor.execute("INSERT INTO Empleados(nomEmpleado,ape1Empleado,ape2Empleado,fecIniEmp,edad) values(?,?,?,?,?)",
                (nombre,ape1,ape2,fecIni,edad,)
                    )
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error:
        print("Ooops los campos fecha o edad estan mal")

def insertarProye(nombre,fecIni):
    try:
        cursor.execute("INSERT INTO Proyectos(nomProyecto,fechaInicio) values(?,?)",
                       (nombre,fecIni))
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error:
        print("Ooops el campo fecha puede estar FATAL")
    
        
# Actualizaciones -------------------------------------------------------------------
def actualizarDepto(nombre,ubicacion,codigo):
    cursor.execute("UPDATE Departamentos SET nomDepto = ?, ubicacion = ? WHERE codDepto = ?",
               (nombre,ubicacion,codigo,)
              )
    conn.commit()
    print("Actualizado satisfactoriamente")
    
def actualizarEmple(codigoDepto,nombre,ape1,ape2,fecFin,edad,codEmp):
    cursor.execute("UPDATE Empleados SET codDepto = ?, nomEmpleado = ?, ape1Empleado = ?, ape2Empleado = ?, fecIniEmp = ?, edad = ?  WHERE codEmpleado = ?",
               (codigoDepto,nombre,ape1,ape2,fecFin,edad,codEmp,)
              )
    conn.commit()
    print("Actualizado satisfactoriamente")

def actualizarProye(codProye,nombre,fechaFin):
    cursor.execute("UPDATE Proyectos SET nomProyecto = ?, fechaFin = ? WHERE codProyecto = ?",
                   (nombre,fechaFin,codProye)
                   )
    conn.commit()
    print("Actualizado satisfactoriamente")

# Eliminaciones -------------------------------------------------------------------
def eliminarDepto(codigo):
    cursor.execute("DELETE FROM Departamentos WHERE codDepto = ?",
                (codigo,)
            )
    conn.commit()
    print(f"{codigo} Eliminado satisfactoriamente")
    
def eliminarEmple(codigo):
    cursor.execute("DELETE FROM Empleados WHERE codEmpleado = ?",
                (codigo,)
            )
    conn.commit()
    print(f"{codigo} Eliminado satisfactoriamente")
    
def eliminarProyec(codigo):
    cursor.execute("DELETE FROM Proyectos WHERE codProyecto = ?",
                   (codigo,)
                   )
    conn.commit()
    print(f"{codigo} Eliminado satisfactoriamente")

