from tkinter import *
from tkinter import messagebox
from collections import Counter

from task_manager import TaskManager
from profile import Profile


# 옷장 화면 보여주는 클래스
class ClosetScreen:
    # 화면 구성
    def __init__(self, count):
        self.count = count
        self.p = Profile()

        self.item_hat = ["h1.png", "h2.png", "h3.png", "h4.png"]
        self.item_top = ["t1.png", "t2.png", "t3.png", "t4.png"]
        self.item_bottom = ["b1.png", "b2.png", "b3.png", "b4.png"]
        self.item_shoes = ["s1.png", "s2.png", "s3.png", "s4.png"]
        self.used_hat = []
        self.used_top = []
        self.used_bottom = []
        self.used_shoes = []

        self.get_hat = []
        self.get_top = []
        self.get_bottom = []
        self.get_shoes = []

        CANVAS_SIZE = 600

        self.root = Toplevel()
        self.root.title("Try, Do it !")
        self.root.configure(bg="white")
        self.root.geometry(str(CANVAS_SIZE+800) + "x" + str(CANVAS_SIZE+100) + "+100+50")
        self.root.resizable(False, False)

        lb1 = Label(self.root, text='Items', bg="white")
        lb1.grid(row=0, column=2, columnspan=2)

        self.name = Entry(self.root, bg="white", width=20, relief="solid", bd=1)
        self.name.grid(row=1, column=0)
        self.bt_name = Button(self.root, text="확인", bg="white", command=self.null_check)
        self.bt_name.grid(row=1, column=1)

        self.bt_often_item = Button(self.root, text="많이 쓴 아이템 확인", bg="white", command=self.show_often_used)
        self.bt_often_item.grid(row=1, column=2)

        # 기본 이미지
        hi = PhotoImage(file="head.png")
        self.head = Label(self.root, image=hi)
        self.head.grid(row=2, column=0, columnspan=2)

        ti = PhotoImage(file="top.png")
        self.top = Label(self.root, image=ti)
        self.top.grid(row=3, column=0, columnspan=2)

        bi = PhotoImage(file="bottom.png")
        self.bottom = Label(self.root, image=bi)
        self.bottom.grid(row=4, column=0, columnspan=2)

        fi = PhotoImage(file="shoes.png")
        self.feet = Label(self.root, image=fi)
        self.feet.grid(row=5, column=0, columnspan=2)

        # 옷이랑 아이템 이미지
        h1 = PhotoImage(file="h1.png")
        h2 = PhotoImage(file="h2.png")
        h3 = PhotoImage(file="a.png")
        h4 = PhotoImage(file="a.png")
        t1 = PhotoImage(file="t1.png")
        t2 = PhotoImage(file="t2.png")
        t3 = PhotoImage(file="a.png")
        t4 = PhotoImage(file="a.png")
        b1 = PhotoImage(file="b1.png")
        b2 = PhotoImage(file="b2.png")
        b3 = PhotoImage(file="a.png")
        b4 = PhotoImage(file="a.png")
        s1 = PhotoImage(file="s1.png")
        s2 = PhotoImage(file="s2.png")
        s3 = PhotoImage(file="a.png")
        s4 = PhotoImage(file="a.png")

        # 모자
        self.hat_selected = IntVar(self.root)
        f1 = Frame(self.root, relief="solid", bd=1, bg="white")
        f1.grid(row=2, column=2)
        self.rd1 = Radiobutton(f1, bg="white", value=1, image=h1, variable=self.hat_selected, state='disabled', command=self.select_hat)
        self.rd1.grid(row=1, column=2)
        self.rd2 = Radiobutton(f1, bg="white", value=2, image=h2, variable=self.hat_selected, state='disabled', command=self.select_hat)
        self.rd2.grid(row=1, column=3)
        self.rd3 = Radiobutton(f1, bg="white", value=3, image=h3, variable=self.hat_selected, state='disabled', command=self.select_hat)
        self.rd3.grid(row=1, column=4)
        self.rd4 = Radiobutton(f1, bg="white", value=4, image=h4, variable=self.hat_selected, state='disabled', command=self.select_hat)
        self.rd4.grid(row=1, column=5)
        # 상의
        self.top_selected = IntVar(self.root)
        f2 = Frame(self.root, relief="solid", bd=1, bg="white")
        f2.grid(row=3, column=2)
        self.rd5 = Radiobutton(f2, bg="white", value=1, image=t1, variable=self.top_selected, state='disabled', command=self.select_top)
        self.rd5.grid(row=1, column=2)
        self.rd6 = Radiobutton(f2, bg="white", value=2, image=t2, variable=self.top_selected, state='disabled', command=self.select_top)
        self.rd6.grid(row=1, column=3)
        self.rd7 = Radiobutton(f2, bg="white", value=3, image=t3, variable=self.top_selected, state='disabled', command=self.select_top)
        self.rd7.grid(row=1, column=4)
        self.rd8 = Radiobutton(f2, bg="white", value=4, image=t4, variable=self.top_selected, state='disabled', command=self.select_top)
        self.rd8.grid(row=1, column=5)
        # 바지
        self.bottom_selected = IntVar(self.root)
        f3 = Frame(self.root, relief="solid", bd=1, bg="white")
        f3.grid(row=4, column=2)
        self.rd9 = Radiobutton(f3, bg="white", value=1, image=b1, variable=self.bottom_selected, state='disabled', command=self.select_bottom)
        self.rd9.grid(row=1, column=2)
        self.rd10 = Radiobutton(f3, bg="white", value=2, image=b2, variable=self.bottom_selected, state='disabled', command=self.select_bottom)
        self.rd10.grid(row=1, column=3)
        self.rd11 = Radiobutton(f3, bg="white", value=3, image=b3, variable=self.bottom_selected, state='disabled', command=self.select_bottom)
        self.rd11.grid(row=1, column=4)
        self.rd12 = Radiobutton(f3, bg="white", value=4, image=b4, variable=self.bottom_selected, state='disabled', command=self.select_bottom)
        self.rd12.grid(row=1, column=5)
        # 신발
        self.shoe_selected = IntVar(self.root)
        f4 = Frame(self.root, relief="solid", bd=1, bg="white")
        f4.grid(row=5, column=2)
        self.rd13 = Radiobutton(f4, bg="white", value=1, image=s1, variable=self.shoe_selected, state='disabled', command=self.select_shoes)
        self.rd13.grid(row=1, column=2)
        self.rd14 = Radiobutton(f4, bg="white", value=2, image=s2, variable=self.shoe_selected, state='disabled', command=self.select_shoes)
        self.rd14.grid(row=1, column=3)
        self.rd15 = Radiobutton(f4, bg="white", value=3, image=s3, variable=self.shoe_selected, state='disabled', command=self.select_shoes)
        self.rd15.grid(row=1, column=4)
        self.rd16 = Radiobutton(f4, bg="white", value=4, image=s4, variable=self.shoe_selected, state='disabled', command=self.select_shoes)
        self.rd16.grid(row=1, column=5)
        
        # count 개수를 세서 옷장을 업그레이드 해준다.
        self.update_closet()

        self.root.mainloop()

    # 이름이나 아이템이 있는지 확인
    def null_check(self):
        name = str(self.name.get())
        print(name)
        if name == "":
            messagebox.showinfo("Profile", "이름을 지정해주세요.")
        if self.item_hat == "" or self.item_top == "" or self.item_bottom == "" or self.item_shoes == "":
            messagebox.showinfo("Profile", "아이템이 없습니다.")

    # 작성한 이름 받아옴
    def get_name(self):
        name = self.name.get()
        print(name)

        self.p.set_name(name)

    # count 개수를 세서 아이템 얻은 거 쓸 수 있도록 해줌
    def update_closet(self):
        if self.count >= 1:
            self.get_top.append(self.item_top[0])
            self.rd5.configure(state='normal')
            self.rd5.update()
        if self.count >= 5:
            self.get_bottom.append(self.item_bottom[0])
            self.rd9.configure(state='normal')
            self.rd9.update()
        if self.count >= 10:
            self.get_shoes.append(self.item_shoes[0])
            self.rd13.configure(state='normal')
            self.rd13.update()
        if self.count >= 15:
            self.get_hat.append(self.item_hat[0])
            self.rd1.configure(state='normal')
            self.rd1.update()
        if self.count >= 25:
            self.get_top.append(self.item_top[1])
            self.rd6.configure(state='normal')
            self.rd6.update()
        if self.count >= 35:
            self.get_bottom.append(self.item_bottom[1])
            self.rd10.configure(state='normal')
            self.rd10.update()
        if self.count >= 45:
            self.get_shoes.append(self.item_shoes[1])
            self.rd14.configure(state='normal')
            self.rd14.update()
        if self.count >= 55:
            self.get_hat.append(self.item_hat[1])
            self.rd2.configure(state='normal')
            self.rd2.update()
        if self.count >= 65:
            self.get_top.append(self.item_top[2])
            self.rd7.configure(state='normal')
            self.rd7.update()
        if self.count >= 75:
            self.get_bottom.append(self.item_bottom[2])
            self.rd11.configure(state='normal')
            self.rd11.update()
        if self.count >= 85:
            self.get_shoes.append(self.item_shoes[2])
            self.rd15.configure(state='normal')
            self.rd15.update()
        if self.count >= 95:
            self.get_hat.append(self.item_hat[2])
            self.rd3.configure(state='normal')
            self.rd3.update()
        if self.count >= 135:
            self.get_top.append(self.item_top[3])
            self.rd8.configure(state='normal')
            self.rd8.update()
        if self.count >= 165:
            self.get_bottom.append(self.item_bottom[3])
            self.rd12.configure(state='normal')
            self.rd12.update()
        if self.count >= 185:
            self.get_shoes.append(self.item_shoes[3])
            self.rd16.configure(state='normal')
            self.rd16.update()
        if self.count >= 200:
            self.get_hat.append(self.item_hat[3])
            self.rd4.configure(state='normal')
            self.rd4.update()

    # 선택된 모자 아이템으로 캐릭터가 바뀌도록 함.
    def select_hat(self):
        hat = str(self.hat_selected.get())
        hf = "h" + hat + ".png"
        # if self.used_item
        hi = PhotoImage(file=hf)
        self.head.configure(image=hi)
        self.head.image = hi
        self.used_hat.append(hf)
        for item in self.used_hat:
            print(item)
        print("---")

    # 선택된 상의 아이템으로 캐릭터가 바뀌도록 함.
    def select_top(self):
        top = str(self.top_selected.get())
        tf = "t" + top + ".png"
        ti = PhotoImage(file=tf)
        self.top.configure(image=ti)
        self.top.image = ti
        self.used_top.append(tf)
        for item in self.used_top:
            print(item)
        print("---")

    # 선택된 하의 아이템으로 캐릭터가 바뀌도록 함.
    def select_bottom(self):
        bottom = str(self.bottom_selected.get())
        bf = "b" + bottom + ".png"
        bi = PhotoImage(file=bf)
        self.bottom.configure(image=bi)
        self.bottom.image = bi
        self.used_bottom.append(bf)
        for item in self.used_bottom:
            print(item)
        print("---")

    # 선택된 신발 아이템으로 캐릭터가 바뀌도록 함.
    def select_shoes(self):
        shoes = str(self.shoe_selected.get())
        sf = "s" + shoes + ".png"
        si = PhotoImage(file=sf)
        self.feet.configure(image=si)
        self.feet.image = si
        self.used_shoes.append(sf)
        for item in self.used_shoes:
            print(item)
        print("---")

    # 가장 많이 사용된 아이템 보여주는 함수
    def show_often_used(self):
        # 가장 많이 사용된 모자(머리) 아이템
        result = Counter(self.used_hat)
        for k, v in result.items():
            if max(list(result.values())) == v:
                messagebox.showinfo("머리", (k+"아이템을 많이 사용하셨군요 !"))
        # 가장 많이 사용된 상의 아이템
        result = Counter(self.used_top)
        for k, v in result.items():
            if max(list(result.values())) == v:
                messagebox.showinfo("상의", (k+"아이템을 많이 사용하셨군요 !"))
        # 가장 많이 사용된 하의 아이템
        result = Counter(self.used_bottom)
        for k, v in result.items():
            if max(list(result.values())) == v:
                messagebox.showinfo("하의", (k+"아이템을 많이 사용하셨군요 !"))
        # 가장 많이 사용된 신발 아이템
        result = Counter(self.used_shoes)
        for k, v in result.items():
            if max(list(result.values())) == v:
                messagebox.showinfo("신발", (k+"아이템을 많이 사용하셨군요 !"))


if __name__ == '__main__':
    c = ClosetScreen()
