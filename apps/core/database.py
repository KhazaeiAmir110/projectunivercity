import sqlite3

import secret


class Database:
    instance = None
    _create_table_query = None

    def __init__(self, *args, **kwargs):
        self.db_path = secret.DATABASE_PATH
        self._initialize_instance(*args, **kwargs)

    def _initialize_instance(self, *args, **kwargs):
        pass

    def create_table(self):
        self.instance.db_path = self.db_path
        with self.instance:
            self.instance.execute_raw(self._create_table_query)

    @classmethod
    def _create_instance(cls, *args, **kwargs):
        cls.instance = super().__new__(cls, *args, **kwargs)

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
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __enter__(self):
        self.conn = self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.conn.close()

# db = Database()
