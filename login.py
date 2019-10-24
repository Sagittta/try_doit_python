import pymysql


class Login:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    def check_id(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        curs = conn.cursor()

        try:
            with conn.cursor() as curs:
                sql = "SELECT id FROM profile WHERE id = '%s'" % self.id
                curs.execute(sql)
                t_id = str(curs.fetchone()[0])
                if t_id:
                    sql = "SELECT pwd FROM profile WHERE id = '%s'" % t_id
                    curs.execute(sql)
                    t_pwd = str(curs.fetchone()[0])
                    if t_pwd:
                        print(t_id, "님 로그인되었습니다.")
                    else:
                        print("비밀번호가 틀립니다.")
                else:
                    print("아이디가 틀립니다.")
        finally:
            conn.close()


id = input("아이디 입력 : ")
pwd = input("비밀번호 입력 : ")
l = Login(id, pwd)
l.check_id()
