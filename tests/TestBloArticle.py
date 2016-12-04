import unittest
from blo.BloArticle import BloArticle


class TestBloArticle(unittest.TestCase):
    def setUp(self):
        self.blo_article = BloArticle()
        self.base_file_path = "./test_article_1.md"

    def test_failed_load_from_file(self):
        with self.assertRaises(FileNotFoundError):
            self.blo_article.load_from_file("")

    def test_success_load_from_file(self):
        expected_str = '# Test Article\nfirst paragraph \n\nsecond paragraph with semi long length string and the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog.\n\nthird paragraph with bullet list\n- 1st\n  - 1st c1\n  - 1st c2\n- 2nd\n- 3rd\n  - 3rd c1\n  - 3rd c2\n- 4th\n\n**Strong text** *Italic text*'
        self.assertIsNone(self.blo_article.load_from_file(self.base_file_path))
        self.assertEqual(expected_str, self.blo_article._raw_text)

    def test_convert_to_simple_html(self):
        expected_html = '<h1>Test Article</h1>\n<p>first paragraph</p>\n<p>second paragraph with semi long length string and the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog.</p>\n<p>third paragraph with bullet list</p>\n<ul>\n<li>1st\n<ul>\n<li>1st c1</li>\n<li>1st c2</li>\n</ul>\n</li>\n<li>2nd</li>\n<li>3rd\n<ul>\n<li>3rd c1</li>\n<li>3rd c2</li>\n</ul>\n</li>\n<li>4th</li>\n</ul>\n<p><strong>Strong text</strong> <em>Italic text</em></p>\n'
        self.blo_article.load_from_file(self.base_file_path)
        self.assertMultiLineEqual(expected_html, self.blo_article.convert_to_html())

    def test_convert_to_template_html(self):
        pass

    def test_get_digest(self):
        expected_html = '<h1>Test Article</h1>\n<p>first paragraph</p>\n<p>second paragraph with semi long length string and the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog.</p>\n<p>third paragraph with bullet list</p>\n<ul>\n<li>1st\n<ul>\n<li>1st c1</li>\n<li>1st c2</li>\n</ul>\n</li>\n<li>2nd</li>\n<li>3rd\n<ul>\n<li>3rd c1</li>\n<li>3rd c2</li>\n</ul>\n</li>\n<li>4th</li>\n</ul>\n<p><strong>Strong text</strong> <em>Italic text</em></p>\n'
        self.blo_article.load_from_file(self.base_file_path)
        self.blo_article.convert_to_html()
        from hashlib import sha512
        hs = sha512()
        hs.update(expected_html.encode('utf-8'))
        self.assertEqual(hs.digest(), self.blo_article.get_digest())

