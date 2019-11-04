from list_screen import ListScreen
from profile import Profile
from task_manager import TaskManager


class Task:
    def __init__(self):
        self.l = ListScreen()
        self.p = Profile()
        self.tm = TaskManager

        self.prof_num = self.p.prof_num
        self.content = self.l.task.get()
        self.priority = self.l.check_priority()
        self.tag = self.l.tag.get()
        self.date = str(self.l.year.get()) + str(self.l.month.get()) + str(self.l.day.get())
        self.listnum = self.tm.find_listnum(self.content)
        self.percent = 0

    def set_percent(self, percent):
        self.percent = percent
        self.tm.update_task(self.listnum, self.content, self.percent)