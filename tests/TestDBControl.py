import unittest
from pathlib import Path
from blo.DBControl import DBControl


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

    def doCleanups(self):
        self.db_control.close_connect()
