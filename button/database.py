import pymysql


class DataBase:
    def __init__(self):
        self.config = {
            'user': 'root',
            'password': '1234',
            'host': 'localhost',
            'db': 'test'
        }

    def load_todo_data(self):
        cursor = None
        conn = None

        try:
            conn = pymysql.connect(**self.config)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todolist;")
            print("mysql 실행")
            # for row in cursor.fetchall():
            #     print(row)

        except pymysql.Error as err:
            print(f"mysql is not opened, error code : {err}")

        finally:
            cursor.close()
            conn.close()


    def


data = DataBase().load_todo_data()



