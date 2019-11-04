from tkinter import *
from task_manager import TaskManager


class ListScreen:
    def __init__(self):
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
        self.task = Entry(self.root, width=40)
        # self.task.insert(0, "Write Here")
        self.task.grid(row=1, column=0, columnspan=5)
        # self.task.bind("<Button-1>", self.task.delete(0, 10))

        self.priority = IntVar()
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

        self.tag = Entry(self.root, width=20)
        self.tag.grid(row=2, column=2, columnspan=3)

        self.year = Entry(self.root, width=6)
        self.year.grid(row=3, column=2)
        self.month = Entry(self.root, width=6)
        self.month.grid(row=3, column=3)
        self.day = Entry(self.root, width=6)
        self.day.grid(row=3, column=4)

        self.bt_add_task = Button(self.root, bg="white", text="Add Task", width=20)
        self.bt_add_task.grid(row=4, column=2, columnspan=3)

        # Doing Tasks Part
        self.task_selected = Label(self.root, text="Empty", width=40, bg="white", relief="solid", bd=1)
        self.task_selected.grid(row=8, column=0, columnspan=5)

        self.bt_update = Button(self.root, text="Update", fg="blue", width=15, bg="white", command=self.update)
        self.bt_update.grid(row=9, column=0, columnspan=2)

        self.percent = Entry(self.root, width=10)
        self.percent.grid(row=9, column=3)
        lb4 = Label(self.root, text="%", bg="white")
        lb4.grid(row=9, column=4)

        self.bt_open = Button(self.root, text="Open Your Closet", width=40, bg="white", command=self.open)
        self.bt_open.grid(row=10, column=0, columnspan=5)

        # To do List Part
        self.bt_show_list = Button(self.root, text="Show List", fg="blue", width=40, bg="white", command=self.show_list)
        self.bt_show_list.grid(row=1, column=5, columnspan=5)

        self.bt_show_list = Button(self.root, text="Sort to Priority", fg="blue", width=15, bg="white", command=self.sort_priority)
        self.bt_show_list.grid(row=2, column=5, columnspan=2)
        self.bt_show_list = Button(self.root, text="Sort to Tag", fg="blue", width=15, bg="white", command=self.sort_tag)
        self.bt_show_list.grid(row=2, column=8, columnspan=2)

        self.lb_tasks = Listbox(self.root, width=40)
        self.lb_tasks.grid(row=3, column=5, rowspan=7, columnspan=5)

        self.bt_delete = Button(self.root, text="Delete", fg="brown", width=15, bg="white", command=self.delete)
        self.bt_delete.grid(row=10, column=5, columnspan=2)
        self.bt_complete = Button(self.root, text="Complete", fg="green", width=15, bg="white", command=self.complete)
        self.bt_complete.grid(row=10, column=8, columnspan=2)

        # self.canvas.pack()

        self.root.mainloop()

    def show_list(self):
        pass

    def check_priority(self):
        pass

    def sort_priority(self):
        pass

    def sort_tag(self):
        pass

    def delete(self):
        pass

    def complete(self):
        pass

    def update(self):
        pass

    def open(self):
        pass


if __name__ == '__main__':
    ls = ListScreen()
