import pymysql, datetime

class TodoDataBase():
    def __init__(self):
        self.host = 'emer.iptime.org'
        self.user = 'emer'
        self.password = 'emergency_team_2434'
        self.database = 'emergency'
        self.connection = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        
    def connect_db(self):
        if self.connection:
            return True
        else:
            print("fail")
            return False
    # # data = DataBase.select_todo(self, 1)

    def select_todo(self, id):
        if TodoDataBase.connect_db(self):
            cursor = self.connection.cursor()
            query = f"SELECT * FROM todo where userid = '{id}' order by todonum desc limit 9;"
            cursor.execute(query)
            
            result = cursor.fetchall()
            cursor.close()
            self.connection.close()
            return result
        else:
            print("error")

    def select_rank(self):
        if TodoDataBase.connect_db(self):
            cursor = self.connection.cursor()
            query = f"select username from todo, users where todo.userid = users.userid group by todo.userid order by count(*) desc;"  
            cursor.execute(query)
            result = cursor.fetchall()
            
            cursor.close()
            self.connection.close()
            
            return result
        else:
            print("error")
        

class Graph(TodoDataBase):
    def __init__(self):
        super().__init__()

    def connect_db(self):
        if self.connection:
            # print("MySQL Connect")
            return True
            
        else:
            print("fail")
            return False

    def inesrt_angle(self, angle_value):
        if self.connect_db:
            cursor = self.connection.cursor()
            query = f"insert into ranking values('1', '양유빈', `{angle_value}`, '{datetime.datetime.now()}')"  
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