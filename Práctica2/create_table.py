import connection as conn

def create():
    sql = '''CREATE TABLE PELICULAS(
                    id SERIAL PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    año INT NOT NULL,
                    director VARCHAR(255) NOT NULL,
                    pais VARCHAR(255) NOT NULL,
                    puntuacion FLOAT NOT NULL
    )'''
    conn.cursor.execute(sql)
    conn.conn.commit()
