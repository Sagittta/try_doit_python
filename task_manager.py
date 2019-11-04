from task import Task
# from list_screen import ListScreen

import pymysql


class TaskManager:
    def __init__(self):
        self.t = Task
        self.task = self.t.task

    # DB 연결된 메소드
    def add_task(self, prof_num, content, priority, tag, date):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        tm = TaskManager()

        # prof_num 이 profile 테이블에 있는지 확인해야 함.
        result = tm.check_profile(prof_num)

        try:
            with conn.cursor() as curs:
                if result == 1:
                    sql = "INSERT INTO task(listnum, prof_num, content, prio, tag, date) VALUES (%s, %s, %s, %s, %s, %s)"
                    value = (0, prof_num, content, priority, tag, date)
                    curs.execute(sql, value)

                    data = curs.fetchall()

                    if not data:
                        conn.commit()
                        print("추가 완료")
                    else:
                        conn.rollback()
                        print("추가 실패")
                else:
                    print("프로필 번호를 다시 확인해주세요.")

        finally:
            conn.close()

    def check_profile(self, prof_num):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT prof_num FROM profile WHERE prof_num = '%s'" % prof_num
                curs.execute(sql)
                t_num = int(str(curs.fetchone()[0]))

                if t_num == prof_num:
                    return 1
                else:
                    print("t_num != prof_num")
                    return 0
        # prof_num 이 존재하지 않을 때 Type Error 발생하므로 처리해줌
        except TypeError:
            print("TypeError 발생")
            return 0
        finally:
            conn.close()

    def update_task(self, listnum, content, percent):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')
        tm = TaskManager()

        # listnum 이 task 테이블에 있는지 확인해야 함.
        result = tm.check_task(listnum)

        try:
            with conn.cursor() as curs:
                if result == 1:
                    sql = "UPDATE task SET content='%s', percent='%s' WHERE listnum='%s'" % (content, percent, listnum)
                    curs.execute(sql)

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

    def check_task(self, listnum):
        conn = pymysql.connect(host='localhost', user='root', password='mirim2', db='project', charset='utf8')

        try:
            with conn.cursor() as curs:
                sql = "SELECT listnum FROM task WHERE listnum = '%s'" % listnum
                curs.execute(sql)
                t_num = int(str(curs.fetchone()[0]))

                if t_num == listnum:
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
                    else:
                        conn.rollback()
                        print("삭제 실패")
                else:
                    print("할 일 번호를 다시 확인해주세요.")
        finally:
            conn.close()

    def complete_task(self):
        # 일 완료했으면 리턴 1
        # 못 했으면 리턴 0
        return 1

    def open_closet(self):
        pass


if __name__ == '__main__':
    tm = TaskManager()
    tm.update_listbox()
