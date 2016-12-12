import unittest
from pathlib import Path
from blo.DBControl import DBControl
from blo.BloArticle import BloArticle


class TestDBControlOnMemory(unittest.TestCase):
    def setUp(self):
        self.db_control = DBControl()

    def test_initializer_for_file(self):
        file_path = "./test.sqlite"
        self.db_control.close_connect()
        self.db_control = DBControl(file_path)
        self.db_control.create_tables()
        self.assertTrue(Path(file_path).exists())
        self.db_control.close_connect()
        Path(file_path).unlink()
        self.assertFalse(Path(file_path).exists())
        self.db_control = DBControl()

    def test_create_table_and_select_all(self):
        self.db_control.create_tables()
        ret = self.db_control._select_all('Articles')
        self.assertIsInstance(ret, list)

    def test_insert_article(self):
        self.db_control.create_tables()
        article1 = BloArticle()
        article1.load_from_file('test_article_1.md')
        self.db_control.insert_article(article1)

    def test_select_last_n(self):
        self.db_control.create_tables()
        article1 = BloArticle()
        article2 = BloArticle()
        article1.load_from_file('test_article_1.md')
        article2.load_from_file('test_article_2.md')
        self.db_control.insert_article(article1)
        self.db_control.insert_article(article2)
        ret = self.db_control.select_last_n(1)
        self.assertEqual(1, len(ret))
        ret = self.db_control.select_last_n(2)
        self.assertEqual(2, len(ret))
        ret = self.db_control.select_last_n(5)
        self.assertEqual(2, len(ret))

    def doCleanups(self):
        self.db_control.close_connect()
