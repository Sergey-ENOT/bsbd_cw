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
            # db_cursor = self.connection_db.cursor()
            # #db_cursor.execute("call proc_start_reception('2024/01/07', '23:00:00');")
            # db_cursor.execute("select * from pg_roles;")
            # #print("cursor:", db_cursor.description)    # todo check fetch cursor for 'None' or no
            # print("Roles: ", db_cursor.fetchall(), "\n")
            # db_cursor.close()
        except (Exception, Error) as ex:
            print("Connection refused...")
            print("Error(connection):", ex)
            raise Exception

    def check_patient_data(self, arg_policy, arg_date):
        self.cursor_db = self.connection_db.cursor()
        self.cursor_db.execute(f"select check_patient_data('{arg_policy}', '{arg_date}');")
        res_query_f = self.cursor_db.fetchone()
        self.cursor_db.close()
        self.cursor_db = None
        return res_query_f[0]

    def func_select_patient_data(self, id_p):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_select_patient_data({id_p})")
            received_data = self.cursor_db.fetchone()
            self.cursor_db.close()
            return received_data
        except (Exception, Error) as err:
            print(err)

    def view_get_streets_title(self):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from view_title_streets")
            received_data = self.cursor_db.fetchall()
            self.cursor_db.close()
            return received_data
        except (Exception, Error) as err:
            print(err)

    def close_connection(self):
        try:
            self.connection_db.close()
            self.connection_db = None
        except (Exception, Error) as ex:
            print(ex)


if __name__ == "__main__":
    try:
        db_con = ConnectorDB("127.0.0.1", "patient_public", "12345678")
        db_con.create_connection()
        res_query = db_con.check_patient_data("1263000000000001", "1977-12-12")
        db_con.close_connection()
        print(res_query)

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
