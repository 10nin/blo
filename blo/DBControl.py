# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
from blo.BloArticle import BloArticle


class DBControl:
    def __init__(self, db_name: str=":memory:"):
        """Initializer for blo blog engine database controller.

        :param db_name: database file name connect to it database file. default use on memory database.
        """
        self.db_conn = sqlite3.connect(db_name)

    def create_tables(self):
        """Create tables for blo blog engine.
        """
        c = self.db_conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS Articles (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    text TEXT,
                                    digest TEXT UNIQUE,
                                    updatedate TEXT);""")
        c.execute("CREATE VIRTUAL TABLE IF NOT EXISTS Articles_fts USING fts4( words TEXT );")
        self.db_conn.commit()

    def close_connect(self):
        """Close database connect.
        """
        self.db_conn.close()
        self.db_conn = None

    def is_exists(self, digest: str):
        c = self.db_conn.cursor()
        c.execute("SELECT * FROM Articles WHERE digest = ?;", (digest,))
        ret = c.fetchall()
        if ret is None:
            return False
        else:
            return True

    def insert_article(self, article: BloArticle, template_name: str=''):
        """Insert article html and wakati text to Article/Article_fts tables.

        :param article: target article
        :param template_name: template file name on template directory.
        """
        assert(article is not None)
        # if has not text data then no action on this method.
        if article.has_text:
            c = self.db_conn.cursor()

            html = article.get_html(template_name)
            digest = article.get_digest()
            timestamp = self._get_timestamp()
            wakati = article.get_wakati_txt()

            if not self.is_exists(digest):
                c.execute("INSERT INTO Articles (text, digest, updatedate) VALUES (?, ?, ?);", (html, digest, timestamp))
                c.execute("INSERT INTO Articles_fts (words) VALUES (?);", (wakati,))
                self.db_conn.commit()

    def select_last_n(self, n) -> list:
        assert(self.db_conn is not None)
        c = self.db_conn.cursor()
        c.execute("SELECT * FROM Articles ORDER BY updatedate DESC LIMIT ?;", (n,))
        return c.fetchall()

    @staticmethod
    def _get_timestamp() -> str:
        """Get timestamp formatted yyyy/mm/dd hh:nn:ss"""
        return datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    def _select_all(self, table_name: str) -> list:
        """Select all rows from table_name table. but this method is for testing only."""
        c = self.db_conn.cursor()
        c.execute("SELECT * FROM " + table_name)
        return c.fetchall()
