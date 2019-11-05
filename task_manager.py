import pymysql


class TaskManager:
    count = 0

    def __init__(self):

        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        self.tasks = []

        try:
            with conn.cursor() as curs:
                sql = "SELECT content FROM task"
                curs.execute(sql)
                rows = curs.fetchall()
                row = rows[0]
                row_a = row[0]
                #l_rows = list(rows)
                print(row_a)
                for row in rows:
                    #foo, bar = l_rows
                    self.tasks.append(row[0])
        finally:
            conn.close()

    # DB 연결된 메소드
    def add_task(self, content):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        tm = TaskManager()

        try:
            with conn.cursor() as curs:
                sql = "INSERT INTO task(listnum, content) VALUES (%s, %s)"
                value = (0, content)
                curs.execute(sql, value)

                data = curs.fetchall()

                if not data:
                    conn.commit()
                    print("추가 완료")
                else:
                    conn.rollback()
                    print("추가 실패")

        finally:
            conn.close()

    def update_task(self, listnum, content, percent):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        tm = TaskManager()

        # listnum 이 task 테이블에 있는지 확인해야 함.
        result = tm.check_task(listnum)

        ln = int(listnum)
        per = int(percent)
        print(content, ln, per)

        try:
            with conn.cursor() as curs:
                if result == 1:
                    sql = "UPDATE task SET content='%s', percent='%s' WHERE listnum='%s'"
                    value = (content, per, ln)
                    curs.execute(sql, value)

                    data = curs.fetchall()

                    if not data:
                        conn.commit()
                        print("업데이트 완료")
                    else:
                        conn.rollback()
                        print("업데이트 실패")
                else:
                    print("할 일 번호를 다시 확인해주세요.")
        finally:
            conn.close()

    def get_listnum(self, content):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT listnum FROM task WHERE content = '%s'" % content
                curs.execute(sql)
                t = str(curs.fetchone()[0])
                print(t)
                if t:
                    return t
                else:
                    print("Error")
                    return 0
        # listnum 이 존재하지 않을 때 Type Error 발생하므로 처리해줌
        except TypeError:
            print("TypeError 발생")
            return 0
        finally:
            conn.close()

    def check_task(self, listnum):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT listnum FROM task WHERE listnum = '%s'" % listnum
                curs.execute(sql)
                t_num = int(str(curs.fetchone()[0]))

                if t_num == int(listnum):
                    return 1
                else:
                    print("t_num != listnum")
                    return 0
        # listnum 이 존재하지 않을 때 Type Error 발생하므로 처리해줌
        except TypeError:
            print("TypeError 발생")
            return 0
        finally:
            conn.close()

    def find_listnum(self, content):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT listnum FROM task WHERE content = '%s'" % content
                curs.execute(sql)
                t_num = int(str(curs.fetchone()[0]))

                if t_num:
                    return t_num
                else:
                    print("t_num == 0")
                    return 0
        # listnum 이 존재하지 않을 때 Type Error 발생하므로 처리해줌
        except TypeError:
            print("TypeError 발생")
            return 0
        finally:
            conn.close()

    def delete_task(self, listnum):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        tm = TaskManager()

        # listnum 이 task 테이블에 있는지 확인해야 함.
        result = tm.check_task(listnum)

        try:
            with conn.cursor() as curs:
                if result == 1:
                    sql = "DELETE FROM task WHERE listnum='%s'" % listnum
                    curs.execute(sql)

                    data = curs.fetchall()

                    if not data:
                        conn.commit()
                        print("삭제 완료")
                        return 1
                    else:
                        conn.rollback()
                        print("삭제 실패")
                        return 0
                else:
                    print("할 일 번호를 다시 확인해주세요.")
        finally:
            conn.close()

    def complete_task(self, task):
        self.count += 1
        listnum = self.find_listnum(task)
        result = self.delete_task(listnum)
        self.tasks.remove(task)
        # 일 완료했으면 리턴 1
        if result == 1:
            return 1
        else:
            return 0

    def open_closet(self):
        pass



if __name__ == '__main__':
    tm = TaskManager()
    # tm.get_listnum("blabla")
