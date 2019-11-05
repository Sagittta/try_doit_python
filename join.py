from tkinter import messagebox

import pymysql


class Join:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    # 회원가입 (데이터베이스에 insert)
    def sign_up(self, id, pwd, pwd_ck):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        j = Join(id, pwd)
        # id 중복 체크 및 비밀번호 사용 가능한지 체크
        result = j.null_check(id, pwd, pwd_ck)

        try:
            with conn.cursor() as curs:
                if result == 1:
                    sql = "INSERT INTO profile(prof_num, id, pwd) VALUES (%s, %s, %s)"
                    value = (0, id, pwd)
                    curs.execute(sql, value)

                    data = curs.fetchall()

                    if not data:
                        conn.commit()
                        messagebox.showinfo("Join", (id + "님 가입 완료되었습니다."))
                    else:
                        conn.rollback()
                        messagebox.showinfo("Join", "가입 실패")
        finally:
            conn.close()

    # id 중복 체크
    def null_check(self, id, pwd, pwd_ck):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        j = Join(id, pwd)
        try:
            with conn.cursor() as curs:
                sql = "SELECT id FROM profile WHERE id='%s'" % id
                curs.execute(sql)
                data = curs.fetchall()

                if data:
                    messagebox.showinfo("Join", "다른 아이디를 사용해주세요.")

                    return 0
                else:
                    messagebox.showinfo("Join", "사용할 수 있는 아이디입니다.")

                    result2 = j.pwd_check(pwd, pwd_ck)

                    if result2 == 1:
                        return 1
        finally:
            conn.close()

    # 비밀번호와 비밀번호 확인이 같은지 체크
    def pwd_check(self, pwd, pwd_ck):
        if pwd == pwd_ck:
            messagebox.showinfo("Join", "올바른 비밀번호입니다.")
            return 1
        else:
            messagebox.showinfo("Join", "비밀번호를 다시 입력해주세요.")
            return 0


# id = input("아이디 : ")
# pwd = input("비밀번호 : ")
# j = Join(id, pwd)
# j.sign_up(id, pwd)
