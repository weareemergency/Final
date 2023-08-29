import pymysql

class TodoDataBase():
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'root'
        self.password = '1234'
        self.database = 'test'
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)

    def connect_db(self):
        if self.connection:
            # print("MySQL Connect")
            return True
            
        else:
            print("fail")
            return False
    # # data = DataBase.select_todo(self, 1)

    def select_todo(self, id):
        if TodoDataBase.connect_db(self):
            cursor = self.connection.cursor()
            query = f"SELECT * FROM todolist where id = {id}"  
            cursor.execute(query)

            result = cursor.fetchall()
            
            return result
        
        else:
            print("error")


if __name__ == "__main__":
    A = TodoDataBase()
    A.connect_db()
    result = A.select_todo(1) # 1은 아이디 번호를 말함. 
    print(result)