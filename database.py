import pymysql, datetime
from datetime import datetime

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
            query = f"select username from todo, users where todo.userid = users.userid and complete = 'Y' group by todo.userid order by count(*) desc;"
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
            date = datetime.now()
            now_date = date.strftime("%Y-%m-%d")
            query = f"insert into neckdata(userid, angle, detectdate, checkcom) values('jiseok', {str(angle_value)}, '{now_date}', 'Y')" 
            print(now_date)
            cursor.execute(query)
            self.connection.commit()
            print(cursor.rowcount, "record inserted.")
        
        else:
            print("error")
    
    def select_health(self, id):
        if self.connect_db:
            cursor = self.connection.cursor()
            query = f"select userid, avg(angle), detectdate, checkcom from neckdata where userid = '{id}' group by detectdate order by detectdate desc limit 7;"
            cursor.execute(query)
            result = cursor.fetchall() # db 결과 저장
            
            cursor.close()
            self.connection.close()
            
            return result
        else:
            print("error")
    def get_health_neck(self, id):
        if self.connect_db:
            cursor = self.connection.cursor()
            query = f"select userid, angle, detectdate, checkcom from neckdata where userid = '{id}' detectdate desc limit 7;"
            cursor.execute(query)
            result = cursor.fetchall() # db 결과 저장
            
            cursor.close()
            self.connection.close()
            
            return result
        else:
            print("error")

if __name__ == "__main__":
    A = Graph()
    A.connect_db()
    result = A.select_health('jiseok') # 1은 아이디 번호를 말함. 
    
    print(result)