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
    try:
        query = f"SELECT * FROM {tabla}"
        cursor.execute(query)
        filas = cursor.fetchall()
        return filas
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
        
def lecturaGeneral(tabla):
    try:
        cursor.execute(f"SELECT * FROM {tabla}")
        for row in cursor.fetchall():
            print(" ",row)
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
        
def lecturaDepto(codigo):
    try:    
        print("...")
        cursor.execute(f"SELECT * FROM Departamentos WHERE codDepto = {codigo}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")

def lecturaEmple(codigo):
    try:
        print("...")
        cursor.execute(f"SELECT * FROM Empleados WHERE codEmpleado = {codigo}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def lecturaProye(codigo):
    try:
        print("...")
        cursor.execute(f"SELECT * FROM Proyectos WHERE codProyecto = {codigo}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def lecturaRol(codigo):
    try:
        print("...")
        cursor.execute(f"SELECT * FROM Roles WHERE codRol = {codigo}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
        
def lecturaDetalle(codigoE,codigoP,rol):
    try:
        print("...")
        cursor.execute(f"SELECT * FROM DealleProyectos WHERE codEmple = {codigoE} and codProye = {codigoP} and rol = {rol}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def lecturaHistorial(codigo):
    try:
        print("...")
        cursor.execute(f"SELECT * FROM HistorialAccesos WHERE codAcceso = {codigo}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")

def lecturaSeguridad(codigo):
    try:
        print("...")
        cursor.execute(f"SELECT * FROM Seguridad WHERE codSeguridad = {codigo}")
        for row in cursor.fetchall():
            print(" ",row)
        print("...")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
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
        
def insertaHistorial(fecha,tipo,emple,detalle):
    try:
        cursor.execute("INSERT INTO HistorialAccesos(fechaAcceso,tipoAcceso,codEmpleado,detalle) values(?,?,?,?)",
                    (fecha,tipo,emple,detalle) 
                    )
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error as e:
        print(f"Ooops FATAL ERROR -> {e}")

def insertaSeguridad(codEmple,fecha):
    try:
        cursor.execute("INSERT INTO Seguridad(codEmple,fecIniSeg) values(?,?)",
                    (codEmple,fecha) 
                    )
        conn.commit()
        print("Insertado Perfectamente")
    except pyodbc.Error as e:
        print(f"Ooops FATAL ERROR -> {e}")


#------------------------------------------------------------------- Actualizaciones -------------------------------------------------------------------
def actualizarDepto(nombre,ubicacion,codigo):
    try:
        cursor.execute("UPDATE Departamentos SET nomDepto = ?, ubicacion = ? WHERE codDepto = ?",
                (nombre,ubicacion,codigo,)
                )
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def actualizarEmple(codigoDepto,nombre,ape1,ape2,inicio,fecFin,edad,codEmp):
    try:
        cursor.execute("UPDATE Empleados SET codDepto = ?, nomEmpleado = ?, ape1Empleado = ?, ape2Empleado = ?, fecIniEmp = ?, fecIniEmp = ?, edad = ?  WHERE codEmpleado = ?",
                (codigoDepto,nombre,ape1,ape2,inicio,fecFin,edad,codEmp,)
                )
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
        
def actualizarProye(codProye,nombre,fechaFin):
    try:
        cursor.execute("UPDATE Proyectos SET nomProyecto = ?, fechaFin = ? WHERE codProyecto = ?",
                    (nombre,fechaFin,codProye)
                    )
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def actualizarRol(nombre,descripcion,codigo):
    try:
        cursor.execute("UPDATE Roles SET nomRol = ?, descripcion = ? WHERE codRol = ?",
                    (nombre,descripcion,codigo)
                    )
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def actualizaDetalle(codEmple,codProye,rol,horas):
    try:
        cursor.execute("UPDATE DetalleProyectos SET horasAsignadas = ? WHERE codEmple = ? and codProye = ? and rol = ?",
                    (horas,codEmple,codProye,rol))
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
def actualizaAcceso(emple,detalle,codAcceso):
    try:
        cursor.execute("UPDATE HistorialAccesos SET codEmpleado = ?, detalle = ? WHERE codAcceso = ?",
                    (emple,detalle,codAcceso))
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")

def actualizaSeguridad(codEmp,fecha,codigo):
    try:
        cursor.execute("UPDATE Seguridad SET codEmple = ?, fecIniSeg = ? WHERE codSeguridad = ?",
                    (codEmp,fecha,codigo))
        conn.commit()
        print("Actualizado correctamente")
    except pyodbc.Error as e:
        print(f"OOUPSY error -> {e}")
    
    
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

def eliminarHistorial(codigo):
    try:
        cursor.execute("DELETE FROM HistorialAccesos WHERE codAcceso = ?",
                        (codigo,))
        conn.commit()
        print("Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy FATAL ERROR in Historial Accesos -> {e}")

def eliminarSegurata(codigo):
    try:
        cursor.execute("DELETE FROM Seguridad WHERE codSeguridad = ?",
                        (codigo,))
        conn.commit()
        print("Eliminado satisfactoriamente")
    except pyodbc.Error as e:
        print(f"Ooooupssssy FATAL ERROR in Historial Accesos -> {e}")
    