import connection as conn

#Hacer la consulta SQL para crear una tabla llamada PELICULAS
def create():
    sql = '''CREATE TABLE PELICULAS(
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    año INT NOT NULL,
                    director VARCHAR(255) NOT NULL,
                    pais VARCHAR(255) NOT NULL,
                    puntuacion FLOAT NOT NULL
    )'''
    #Ejecutar la consulta create utilizando el cursor de la conexión
    conn.cursor.execute(sql)
    #commit para guardar los cambios en la base de datos
    conn.conn.commit()
