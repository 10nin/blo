import sqlite3


class DBControl:
    def __init__(self, db_name=":memory:"):
        self.db_conn = sqlite3.connect(db_name)

    def create_tables(self):
        self.db_conn.execute("""CREATE TABLE IF NOT EXISTS Articles ("
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    text TEXT,
                                    digest TEXT UNIQUE,
                                    updatedate TEXT)""")
        self.db_conn.execute("CREATE VIRTUAL TABLE Articles_fts USING fts4( words TEXT )")
        self.db_conn.commit()

    def close_connect(self):
        self.db_conn.close()