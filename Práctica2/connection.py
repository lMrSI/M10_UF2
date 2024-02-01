import psycopg2

class DataBaseConnection:
    def __init__(self, database, user, password, host, port):
        self.connection = psycopg2.connect(
            database = database,
            user = user,
            password = password,
            host = host,
            port = port
        )
        self.cursor = self.connection.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def get_connection():
        return DataBaseConnection(
            database="postgres",
            user='user_postgres',
            password='pass_postgres',
            host='localhost',
            port='5432'
        )


