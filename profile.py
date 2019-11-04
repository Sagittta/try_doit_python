from tkinter import messagebox
from task_manager import TaskManager

import pymysql
import random
# from login_screen import LoginScreen
# from login import Login


class Profile:
    def __init__(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        self.id = "a"
        self.pwd = ""
        self.name = ""
        self.item_hat = []
        self.item_top = []
        self.item_bottom = []
        self.item_shoes = []
        self.tasks = []

        try:
            with conn.cursor() as curs:
                sql = "SELECT pwd, name, hat_list, top_list, pants_list, shoes_list, saved_item FROM profile WHERE id = '%s'" % self.id
                curs.execute(sql)
                rows = curs.fetchall()
                for row in rows:
                    self.pwd = row[0]
                    self.name = row[1]
                    self.item_hat = row[2]
                    self.item_top = row[3]
                    self.item_bottom = row[4]
                    self.item_shoes = row[5]
                    self.used_item = row[6]

                print(self.pwd + ", " + self.name + ", " + self.item_hat + ", " + self.item_top + ", " + self.item_bottom + ", " + self.item_shoes + ", " + self.used_item)
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
            random.randint()

    def save_items(self):
        pass

    def set_name(self):
        pass


if __name__ == '__main__':
    p = Profile()
    p.null_check()
