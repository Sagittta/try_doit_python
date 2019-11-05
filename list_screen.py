from tkinter import *
from tkinter import messagebox

from task_manager import TaskManager
from profile import Profile
from closet_screen import ClosetScreen


class ListScreen:
    def __init__(self):
        self.tm = TaskManager()
        self.p = Profile()

        CANVAS_SIZE = 600

        self.root = Tk()
        self.root.title("Try, Do it !")
        self.root.configure(bg="white")
        self.root.geometry(str(CANVAS_SIZE) + "x" + str(CANVAS_SIZE-300) + "+300+100")
        self.root.resizable(False, False)

        lb1 = Label(self.root, text='Add Tasks', bg="white")
        lb1.grid(row=0, column=2)
        lb2 = Label(self.root, text='To do List', bg="white")
        lb2.grid(row=0, column=7)
        lb3 = Label(self.root, text='Doing Task', bg="white")
        lb3.grid(row=7, column=2)

        # Add Tasks Part
        self.task = Entry(self.root, width=40, relief="solid", bd=1)
        self.task.grid(row=1, column=0, columnspan=5)

        self.priority = IntVar(self.root, 1)
        frame = Frame(self.root, relief="solid", bd=1, bg="white")
        frame.grid(row=2, column=0, rowspan=4)
        rd1 = Radiobutton(frame, bg="white", text="중요 & 긴급", value=1, variable=self.priority, command=self.check_priority)
        rd1.pack()
        rd2 = Radiobutton(frame, bg="white", text="중요 & 긴급X", value=2, variable=self.priority, command=self.check_priority)
        rd2.pack()
        rd3 = Radiobutton(frame, bg="white", text="중요X & 긴급", value=3, variable=self.priority, command=self.check_priority)
        rd3.pack()
        rd4 = Radiobutton(frame, bg="white", text="중요X & 긴급X", value=4, variable=self.priority, command=self.check_priority)
        rd4.pack()

        self.tag = Entry(self.root, width=20, relief="solid", bd=1)
        self.tag.grid(row=2, column=2, columnspan=3)

        self.year = Entry(self.root, width=6, relief="solid", bd=1)
        self.year.grid(row=3, column=2)
        self.month = Entry(self.root, width=6, relief="solid", bd=1)
        self.month.grid(row=3, column=3)
        self.day = Entry(self.root, width=6, relief="solid", bd=1)
        self.day.grid(row=3, column=4)

        self.bt_add_task = Button(self.root, bg="white", text="Add Task", width=20, command=self.add)
        self.bt_add_task.grid(row=4, column=2, columnspan=3)

        # Doing Tasks Part
        self.task_selected = Entry(self.root, width=40, bg="white", relief="solid", bd=1)
        self.task_selected.grid(row=8, column=0, columnspan=5)

        self.bt_update = Button(self.root, text="Update", fg="blue", width=15, bg="white", command=self.update)
        self.bt_update.grid(row=9, column=0, columnspan=2)

        self.percent = Entry(self.root, width=10, relief="solid", bd=1)
        self.percent.grid(row=9, column=3)
        lb4 = Label(self.root, text="%", bg="white")
        lb4.grid(row=9, column=4)

        self.bt_open = Button(self.root, text="Open Your Closet", width=40, bg="white", command=self.open)
        self.bt_open.grid(row=10, column=0, columnspan=5)

        # To do List Part
        self.bt_show_list = Button(self.root, text="Show List", fg="blue", width=40, bg="white", command=self.show_list)
        self.bt_show_list.grid(row=1, column=5, columnspan=5)

        self.bt_show_list = Button(self.root, text="Sort", fg="blue", width=40, bg="white", command=self.sort)
        self.bt_show_list.grid(row=2, column=5, columnspan=5)

        self.lb_tasks = Listbox(self.root, width=40, relief="solid", bd=1)
        self.lb_tasks.grid(row=3, column=5, rowspan=7, columnspan=5)

        self.bt_delete = Button(self.root, text="Delete", fg="brown", width=15, bg="white", command=self.delete)
        self.bt_delete.grid(row=10, column=5, columnspan=2)
        self.bt_complete = Button(self.root, text="Doing Tasks", fg="blue", width=8, bg="white", command=self.list_select)
        self.bt_complete.grid(row=10, column=7)
        self.bt_complete = Button(self.root, text="Complete", fg="green", width=15, bg="white", command=self.closet)
        self.bt_complete.grid(row=10, column=8, columnspan=2)

        self.root.mainloop()

    def list_select(self):
        # 리스트 박스에서 선택된 항목 찾기
        task = self.lb_tasks.get("active")
        self.task_selected.delete(0, "end")
        self.task_selected.insert(0, task)

    def show_list(self):
        # 현재 리스트 지우기
        self.clear_listbox()

        # self.tm.tasks db 연결
        # result = self.tm.find_listnum(self.task.get())
        # 리스트 띄우기
        for task in self.tm.tasks:
            self.lb_tasks.insert("end", task)
        print(self.tm.tasks)

    def add(self):
        # 작성한 거 추가하기
        lb = self.task.get()
        self.tm.tasks.append(lb)
        # 현재 리스트 지우기
        self.clear_listbox()
        # 리스트 띄우기
        for task in self.tm.tasks:
            self.lb_tasks.insert("end", task)

        self.tm.add_task(lb)

    def update(self):
        # 작성한 거 추가하기
        lb = self.lb_tasks.get("active")
        if lb != self.task_selected.get():
            past = self.lb_tasks.get("active")
            self.tm.tasks.remove(past)
            self.tm.tasks.append(self.task_selected.get())
        # 현재 리스트 지우기
        self.clear_listbox()
        # 리스트 띄우기
        for task in self.tm.tasks:
            self.lb_tasks.insert("end", task)

        content = lb
        percent = self.percent.get()
        if percent == "":
            percent = 0
        listnum = self.tm.get_listnum(content)
        print(content, " + ", percent, "+", listnum)
        self.tm.update_task(listnum, content, percent)

    def delete(self):
        # 리스트 박스에서 선택된 항목 찾기
        task = self.lb_tasks.get("active")
        if task in self.tm.tasks:
            # 지우기
            self.tm.tasks.remove(task)
        # 리스트 보여주기
        self.show_list()
        # DB 에서 task 항목을 지움
        listnum = self.tm.get_listnum(task)
        self.tm.delete_task(listnum)

    def clear_listbox(self):
        self.lb_tasks.delete(0, "end")

    def check_priority(self):
        return str(self.priority.get())

    def sort(self):
        print(type(self.tm.tasks))
        self.tm.tasks.sort()
        self.show_list()

    def open(self):
        # 바꿔야 함
        ClosetScreen()

    def closet(self):
        select = self.lb_tasks.get("active")
        result = self.tm.complete_task(select)
        # 현재 리스트 지우기
        self.clear_listbox()
        # 리스트 띄우기
        for task in self.tm.tasks:
            self.lb_tasks.insert("end", task)
        print(self.tm.tasks)
        # 여기가 문제 !
        if result == 1:
            self.c.update_closet(result)


if __name__ == '__main__':
    ls = ListScreen()
