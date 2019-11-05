from tkinter import *

from login import Login
from join import Join


class LoginScreen:
    def __init__(self):

        CANVAS_SIZE = 600

        self.root = Tk()
        self.root.title("Try, Do it !")
        self.root.configure(bg="white")
        self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE - 450) + "+300+200")
        self.root.resizable(False, False)

        # self.canvas = Canvas(self.root, width=CANVAS_SIZE, height=CANVAS_SIZE)

        join_label = Label(self.root, text='Join', bg="white", width=30)
        join_label.grid(row=0, column=1)
        login_label = Label(self.root, text='Login', bg="white", width=30)
        login_label.grid(row=0, column=4)

        # Join label & entry & button
        lb1 = Label(self.root, text='ID', bg="white", width=10)
        lb1.grid(row=1, column=0)
        self.join_id = Entry(self.root, width=20)
        self.join_id.grid(row=1, column=1)

        lb2 = Label(self.root, text='PWD', bg="white", width=10)
        lb2.grid(row=2, column=0)
        self.join_pwd = Entry(self.root, width=20)
        self.join_pwd.grid(row=2, column=1)

        lb3 = Label(self.root, text='PWD CK', bg="white", width=10)
        lb3.grid(row=3, column=0)
        self.pwd_ck = Entry(self.root, width=20)
        self.pwd_ck.grid(row=3, column=1)

        self.bt1 = Button(self.root, text="Join", fg="blue", bg="white", width="6", command=self.join)
        self.bt1.grid(row=4, column=1)

        # Login label & entry
        lb4 = Label(self.root, text='ID', bg="white", width=10)
        lb4.grid(row=1, column=3)
        self.login_id = Entry(self.root, width=20)
        self.login_id.grid(row=1, column=4)

        lb5 = Label(self.root, text='PWD', bg="white", width=10)
        lb5.grid(row=2, column=3)
        self.login_pwd = Entry(self.root, width=20)
        self.login_pwd.grid(row=2, column=4)

        self.bt2 = Button(self.root, text="Login", fg="blue", bg="white", width="6", command=self.login)
        self.bt2.grid(row=4, column=4)

        self.j = Join("id", "pwd")
        self.l = Login("id", "pwd")

        # self.canvas.pack()

        self.root.mainloop()

    def join(self):
        id = self.join_id.get()
        pwd = self.join_pwd.get()
        pwd_ck = self.pwd_ck.get()
        if id == "" or pwd == "" or pwd_ck == "":
            print("빈 곳을 채워주세요.")
        else:
            self.j.sign_up(id, pwd, pwd_ck)
        # print("join success")

    def login(self):
        id2 = self.login_id.get()
        pwd2 = self.login_pwd.get()
        self.root.destroy()
        self.l.sign_in(id2, pwd2)


if __name__ == '__main__':
    ls = LoginScreen()
