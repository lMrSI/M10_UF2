import psycopg2

#Establecer la conexión con PostgreSQL
conn = psycopg2.connect(
    database="postgres",
    user='user_postgres',
    password='pass_postgres',
    host='localhost',
    port='5432'
)

#Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

#print(connection)



