import pymysql


class Login:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    def check_id(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT id FROM profile WHERE id = '%s'" % self.id
                curs.execute(sql)
                t_id = str(curs.fetchone()[0])

                if t_id:
                    return 1
                else:
                    return 0
        finally:
            conn.close()

    def check_pwd(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT pwd FROM profile WHERE id = '%s'" % self.id
                curs.execute(sql)
                t_pwd = str(curs.fetchone()[0])

                if t_pwd:
                    return 1
                else:
                    return 0
        finally:
            conn.close()

    def sign_in(self):
        l = Login(self.id, self.pwd)
        result_id = l.check_id()
        result_pwd = l.check_pwd()

        if result_id == 1:
            if result_pwd == 1:
                print(self.id, "님 로그인 완료되었습니다.")
            else:
                print("비밀번호를 잘못 입력하셨습니다.")
        else:
            print("아이디를 잘못 입력하셨습니다.")


id = input("아이디 입력 : ")
pwd = input("비밀번호 입력 : ")
l = Login(id, pwd)
l.sign_in()
