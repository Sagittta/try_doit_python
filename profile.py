from tkinter import messagebox
from task_manager import TaskManager

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
        self.item_hat = []
        self.item_top = []
        self.item_bottom = []
        self.item_shoes = []
        self.tasks = ["힘들어", "졸려", "젤리 오천 오백개 먹고 싶다"]

        try:
            with conn.cursor() as curs:
                sql = "SELECT prof_num, pwd, name, hat_list, top_list, pants_list, shoes_list, saved_item FROM profile WHERE id = '%s'" % self.id
                curs.execute(sql)
                rows = curs.fetchall()
                for row in rows:
                    self.prof_num = row[0]
                    self.pwd = row[1]
                    self.name = row[2]
                    self.item_hat = row[3]
                    self.item_top = row[4]
                    self.item_bottom = row[5]
                    self.item_shoes = row[6]
                    self.used_item = row[7]
        finally:
            conn.close()

    def null_check(self):
        if self.name == "null":
            messagebox.showinfo("Profile", "이름을 지정해주세요.")
        if self.item_hat == "null" or self.item_top == "null" or self.item_bottom == "null" or self.item_shoes == "null":
            messagebox.showinfo("Profile", "아이템이 없습니다.")

    def get_items(self):
        tm = TaskManager()
        result = tm.complete_task()
        if result == 1:
            result2 = random.randrange(1, 5)
            if result2 == 1:
                self.item_hat = []
            elif result2 == 2:
                self.item_top = []
            elif result2 == 3:
                self.item_bottom = []
            elif result2 == 4:
                self.item_shoes = []

    def save_items(self):
        pass

    def set_name(self):
        pass


if __name__ == '__main__':
    p = Profile()
    p.null_check()
