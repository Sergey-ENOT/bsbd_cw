from PyQt5.QtWidgets import QMessageBox
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
        except (Exception, Error) as ex:
            print("Connection refused...")
            print("Error(connection):", ex)
            raise Exception("Ошибка при подключении. Проверьте данные")

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
            return received_data
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def func_select_doctor_data(self, log_d):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_select_doctor_data('{log_d}')")
            received_data = self.cursor_db.fetchone()
            return received_data
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def view_get_streets_title(self):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from view_title_streets")
            received_data = [x[0] for x in self.cursor_db.fetchall()]
            return received_data
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def view_get_specializations(self):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from view_title_specializations")
            received_data = [x[0] for x in self.cursor_db.fetchall()]
            return received_data
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def proc_add_patient(self, surname, name, patr, gender, date, street, n_h, n_f, phone, ins_policy):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"call proc_insert_patient('{surname}', '{name}', '{patr}', '{gender}', '{date}',"
                                   f"'{street}', '{n_h}', '{n_f}', '{phone}', '{ins_policy}')")
            self.connection_db.commit()
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def proc_update_patient(self, id_p, surname, name, patr, gender, street, n_h, n_f, phone):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"call proc_update_patient('{id_p}', '{surname}', '{name}', '{patr}', '{gender}',"
                                   f"'{street}', '{n_h}', '{n_f}', '{phone}')")
            self.connection_db.commit()
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def proc_add_doctor(self, list_args):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"call proc_insert_doctor('{list_args[0]}', '{list_args[1]}', '{list_args[2]}',"
                                   f"'{list_args[3]}', '{list_args[4]}', '{list_args[5]}', '{list_args[6]}',"
                                   f"'{list_args[7]}', '{list_args[8]}')")
            self.connection_db.commit()
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def proc_update_doctor(self, list_args):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"call proc_update_doctor('{list_args[0]}', '{list_args[1]}',"
                                   f"'{list_args[2]}', '{list_args[3]}')")
            self.connection_db.commit()
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def func_get_area(self, id_p):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_get_patient_area('{id_p}')")
            res_query_f = self.cursor_db.fetchone()
            return res_query_f[0]
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def func_get_tickets(self, id_p, spec_d):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_select_tickets('{id_p}', '{spec_d}')")
            res_query_f = self.cursor_db.fetchall()
            return res_query_f
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def proc_update_ticket(self, id_p, id_t):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"call proc_update_ticket('{id_p}', '{id_t}')")
            self.connection_db.commit()
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def func_select_taken_tickets(self, id_p):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_select_taken_tickets('{id_p}')")
            res_query_f = self.cursor_db.fetchall()
            return res_query_f
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def func_get_ticket_data(self, id_t):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_get_ticket_data('{id_t}')")
            res_query_f = self.cursor_db.fetchone()
            return res_query_f
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def proc_record_reception(self, list_args):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"call proc_record_reception('{list_args[0]}',"
                                   f"'{list_args[1]}', '{list_args[2]}', '{list_args[3]}')")
            self.connection_db.commit()
        except psycopg2.DatabaseError as err:
            print(err)
            raise Exception("Данный талон не был использован. Нельзя создать прием")
        finally:
            self.cursor_db.close()

    def func_select_reception(self, id_v, id_spec=0):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_select_receptions('{id_v}','{id_spec}')")
            res_f = self.cursor_db.fetchall()
            return res_f
        except Exception as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def func_get_doctor_data(self, log_d):
        try:
            self.cursor_db = self.connection_db.cursor()
            self.cursor_db.execute(f"select * from func_get_doctor_data('{log_d}')")
            res_query_f = self.cursor_db.fetchone()
            return res_query_f
        except (Exception, Error) as err:
            print(err)
            raise err
        finally:
            self.cursor_db.close()

    def close_connection(self):
        try:
            self.connection_db.close()
            self.connection_db = None
        except (Exception, Error) as ex:
            print(ex)
            raise ex


if __name__ == "__main__":
    try:
        db_con = ConnectorDB("127.0.0.1", "patient_public", "12345678")
        db_con.create_connection()
        res_query = db_con.check_patient_data("1263000000000001", "1977-12-12")
        db_con.close_connection()
        print(res_query)
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        raise error
