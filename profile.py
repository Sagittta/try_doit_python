from tkinter import messagebox
from task_manager import TaskManager
# from closet_screen import ClosetScreen

import pymysql
import random
# from login_screen import LoginScreen
# from login import Login


class Profile:
    def __init__(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        self.prof_num = 0
        self.id = "a"
        self.pwd = ""
        self.name = ""
        
        # DB 에서 값 가져옴
        try:
            with conn.cursor() as curs:
                sql = "SELECT prof_num, pwd, name FROM profile WHERE id = '%s'" % self.id
                curs.execute(sql)
                rows = curs.fetchall()
                for row in rows:
                    self.prof_num = row[0]
                    self.pwd = row[1]
                    self.name = row[2]
        finally:
            conn.close()

    # prof_num 리턴하는 함수
    def return_num(self):
        return self.prof_num

    # Profile 테이블에 이름 추가
    def set_name(self, name):

        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "INSERT INTO profile(name) VALUES (%s) WHERE id='%s'" % (name, self.id)
                curs.execute(sql)
                data = curs.fetchall()

                if not data:
                    conn.commit()
                    messagebox.showinfo("Profile", (name + "님 이름이 추가되었습니다."))
                else:
                    conn.rollback()
                    messagebox.showinfo("Profile", "이름 추가 실패")
        finally:
            conn.close()


if __name__ == '__main__':
    p = Profile()
