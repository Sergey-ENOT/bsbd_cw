import psycopg2
from psycopg2 import Error


class ConnectorDB:
    def __init__(self, host, role, password):
        self.host = host
        self.user = role
        self.port = "5432"
        self.password = password
        self.db_name = "registratura"
        self.connection_db = None
        self.cursor_db = None

    def create_connection(self):
        try:
            self.connection_db = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.db_name,
            )
            db_cursor = self.connection_db.cursor()
            #db_cursor.execute("call proc_start_reception('2024/01/07', '23:00:00');")
            db_cursor.execute("select * from pg_roles;")
            #print("cursor:", db_cursor.description)    # todo check fetch cursor for 'None' or no
            print("Roles: ", db_cursor.fetchall(), "\n")
            db_cursor.close()
        except (Exception, Error) as ex:
            print("Connection refused...")
            print("Error(connection):", ex)
            raise Exception

    def close_connection(self):
        try:
            self.connection_db.close()
            self.connection_db = None
        except (Exception, Error) as ex:
            print(ex)


if __name__ == "__main__":
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                      # пароль, который указали при установке PostgreSQL
                                      password="admin123",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="registratura")

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")
