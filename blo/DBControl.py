import sqlite3


class DBControl:
    def __init__(self, db_name=":memory:"):
        self.db_conn = sqlite3.connect(db_name)

    def create_tables(self):
        c = self.db_conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Articles (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    text TEXT,
                                    digest TEXT UNIQUE,
                                    updatedate TEXT)""")
        c.execute("CREATE VIRTUAL TABLE Articles_fts USING fts4( words TEXT )")
        self.db_conn.commit()

    def close_connect(self):
        self.db_conn.close()
        self.db_conn = None

    def _select_all(self, table_name):
        c = self.db_conn.cursor()
        c.execute("SELECT * FROM " + table_name)
        return c.fetchall()
