import sqlite3

class Database:
    def __init__(self, db_name: str = "main.db"):
        self.database = db_name

    def execute(self, sql, *args, commit: bool = False, fetchone: bool = False, fetchall: bool = False):
        with sqlite3.connect(self.database) as db:
            cursor = db.cursor()
            cursor.execute(sql, args)

            res = None
            if commit:
                db.commit()
            elif fetchone:
                res = cursor.fetchone()
            elif fetchall:
                res = cursor.fetchall()
        return res


    def create_table_courses(self):
        sql = '''CREATE TABLE IF NOT EXISTS courses(
            id  INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL
        )'''
        self.execute(sql, commit=True)


    def add_course(self, course_name):
        sql = '''INSERT INTO courses (course_name) VALUES (?)'''
        self.execute(sql, course_name, commit=True)

    def get_info(self):
        sql = '''SELECT course_name FROM courses'''
        return self.execute(sql, fetchall=True)

    def delete_info(self):
        sql = '''DELETE FROM courses'''
        self.execute(sql, commit=True)


