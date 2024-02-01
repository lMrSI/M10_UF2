import psycopg2
import connection

def create():
    sql = '''CREATE TABLE SERIES(
                    id SERIAL PRIMARY KEY,
                    nombre VARCHAR(255) NOT NULL,
                    temporadas INT NOT NULL,
                    capitulos INT NOT NULL,
                    puntuacion FLOAT NOT NULL
    )'''
    print(sql)
