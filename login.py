import pymysql


class Login:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd

    # id 존재하는지, 맞는지 확인
    def check_id(self, id):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT id FROM profile WHERE id = '%s'" % id
                curs.execute(sql)
                t_id = str(curs.fetchone()[0])

                if t_id == id:
                    return 1
                else:
                    return 0
        # id 가 존재하지 않을 때 TypeError 가 발생하므로 예외 처리를 한다.
        except TypeError:
            print("아이디를 잘못 입력하셨습니다.")
            return 0
        finally:
            conn.close()

    # 비밀번호 존재하는지, 맞는지 확인
    def check_pwd(self, id, pwd):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT pwd FROM profile WHERE id = '%s'" % id
                curs.execute(sql)
                t_pwd = str(curs.fetchone()[0])

                if t_pwd == pwd:
                    return 1
                else:
                    return 0
        # id 가 존재하지 않을 때 TypeError 가 발생하므로 예외 처리를 한다.
        except TypeError:
            return 0
        finally:
            conn.close()

    # 로그인
    def sign_in(self, id, pwd):
        l = Login(id, pwd)
        result_id = l.check_id(id)
        result_pwd = l.check_pwd(id, pwd)

        if result_id == 1:
            if result_pwd == 1:
                print(id, "님 로그인 완료되었습니다.")
            else:
                print("비밀번호를 잘못 입력하셨습니다.")


# id = input("아이디 입력 : ")
# pwd = input("비밀번호 입력 : ")
# l = Login(id, pwd)
# l.sign_in(id, pwd)
