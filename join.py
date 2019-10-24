import pymysql


class Join:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    def sign_up(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        j = Join(self.id, self.pwd)
        result = j.null_check()

        try:
            with conn.cursor() as curs:

                if result == 1:
                    sql = "INSERT INTO profile(prof_num, id, pwd) VALUES (%s, %s, %s)"
                    value = (0, self.id, self.pwd)
                    curs.execute(sql, value)

                    data = curs.fetchall()

                    if not data:
                        conn.commit()
                        print("가입 완료")
                    else:
                        conn.rollback()
                        print("가입 실패")

        finally:
            conn.close()

    def null_check(self):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT id FROM profile WHERE id='%s'" % self.id
                curs.execute(sql)
                data = curs.fetchall()

                if data:
                    print("다른 아이디를 사용해주세요.")

                    return 0
                else:
                    print("사용할 수 있습니다.")

                    return 1
        finally:
            conn.close()


id = input("아이디 : ")
pwd = input("비밀번호 : ")
j = Join(id, pwd)
j.sign_up()
