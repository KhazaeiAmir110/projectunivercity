import sqlite3

import secret


class Database:
    instance = None

    def __init__(self, db_path=secret.DATABASE_PATH):
        self.db_path = db_path

    @classmethod
    def _create_instance(cls, *args, **kwargs):
        cls.instance = super().__new__(*args, **kwargs)

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls._create_instance(*args, **kwargs)

        return cls.instance

    def connect(self):
        return sqlite3.connect(self.db_path)

    def execute_queries(self, queries):

        for query in queries:
            self.execute_raw(query)

    def execute_raw(self, query):
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute(query)

        conn.commit()
        conn.close()


db = Database()
