import unittest
from blo.BloArticle import BloArticle


class TestBloArticle(unittest.TestCase):
    def setUp(self):
        self.blo_article = BloArticle()

    def test_failed_load_from_file(self):
        file_path = ""
        with self.assertRaises(FileNotFoundError):
            self.blo_article.load_from_file(file_path)

    def test_success_load_from_file(self):
        file_path = "./test_article_1.md"
        self.assertIsNone(self.blo_article.load_from_file(file_path))
        self.assertFalse(self.blo_article._raw_text == "")

    def test_convert_to_html(self):
        pass

    def test_get_digest(self):
        pass
