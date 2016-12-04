import sqlite3


class DBControl:
    def __init__(self, db_name=":memory:"):
        self.db_conn = sqlite3.connect(db_name)
