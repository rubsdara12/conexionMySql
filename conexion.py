# comando para descargar el conector a mysql   pip install mysql-connector-python
import mysql.connector
class CConexion:

    def ConexionBaseDeDatos():
        try:
            conexion = mysql.connector.connect(user='root', password='2215', 
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3306')
            print("Conexion Correcta")

            return conexion
        

        except mysql.connector.Error as error:
            print("Error al conectarte a la base de Datos {}" ,format(error))

            return conexion
        
    ConexionBaseDeDatos()





























# import mysql.connector  conexion de manera sencilla

# conexion = mysql.connector.connect(user='root', password='2215', host='localhost', database='world', port='3306')

# print(conexion)

# cursor= conexion.cursor()
# cursor.execute("SELECT database")
# registro=cursor.fetchone()
# print("conectado a la BD: ", registro )