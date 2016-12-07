import unittest
from blo.BloArticle import BloArticle


class TestBloArticle(unittest.TestCase):
    def setUp(self):
        self.blo_article = BloArticle()
        self.base_file_path_1 = "./test_article_1.md"
        self.base_file_path_2 = "./test_article_2.md"

    def test_failed_load_from_file(self):
        with self.assertRaises(FileNotFoundError):
            self.blo_article.load_from_file("")

    def test_success_load_from_file(self):
        expected_str = '# Test Article\nfirst paragraph \n\nsecond paragraph with semi long length string and the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog.\n\nthird paragraph with bullet list\n- 1st\n  - 1st c1\n  - 1st c2\n- 2nd\n- 3rd\n  - 3rd c1\n  - 3rd c2\n- 4th\n\n**Strong text** *Italic text*'
        self.assertIsNone(self.blo_article.load_from_file(self.base_file_path_1))
        self.assertEqual(expected_str, self.blo_article._raw_text)

    def test_convert_to_simple_html_1(self):
        expected_html = '<h1>Test Article</h1>\n<p>first paragraph</p>\n<p>second paragraph with semi long length string and the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog.</p>\n<p>third paragraph with bullet list</p>\n<ul>\n<li>1st\n<ul>\n<li>1st c1</li>\n<li>1st c2</li>\n</ul>\n</li>\n<li>2nd</li>\n<li>3rd\n<ul>\n<li>3rd c1</li>\n<li>3rd c2</li>\n</ul>\n</li>\n<li>4th</li>\n</ul>\n<p><strong>Strong text</strong> <em>Italic text</em></p>\n'
        self.blo_article.load_from_file(self.base_file_path_1)
        self.assertMultiLineEqual(expected_html, self.blo_article.convert_to_html())

    def test_convert_to_simple_html_2(self):
        expected_html = """<h1>日本語を含んだテストパターンファイル</h1>
<h2>天文と俳句（現代仮名遣い風に編集）</h2>
<h3>寺田寅彦</h3>
<p>俳句季題の分類は普通に <strong>時候</strong> 、''天文'''、 地理 、<code>人事</code>、動物、植物という風になっている。
これらのうちで後の三つは別として、初めの三つの項目中における各季題の分け方は現代の科学知識から見ると、
決して合理的であるとは思われない。</p>
<h2>天文と俳句（原文をそのまま青空文庫より引用）</h2>
<h3>寺田寅彦</h3>
<p><code>俳句季題の分類は普通に時候、天文、地理、人事、動物、植物といふ風になつて居る。此等のうちで後の三つは別として、初めの三つの項目中に於ける各季題の分け方は現代の科學知識から見ると、決して合理的であるとは思はれない。</code></p>
<h2>いくつかの記述要素</h2>
<p>リストを記述する</p>
<ul>
<li>リスト項目1
<ul>
<li>子リスト項目1</li>
<li>子リスト項目2</li>
</ul>
</li>
<li>with english text
<ul>
<li><em>in itarlic</em></li>
<li>日本語の表記と英語( <em>English</em> )の表記を併記した状態でテストを行うためのデータ</li>
</ul>
</li>
</ul>
"""
        self.blo_article.load_from_file(self.base_file_path_2)
        self.assertMultiLineEqual(expected_html, self.blo_article.convert_to_html())

    def test_convert_to_template_html(self):
        pass

    def test_get_digest_1(self):
        expected_html = '<h1>Test Article</h1>\n<p>first paragraph</p>\n<p>second paragraph with semi long length string and the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog repeat the quick brown fox jumps over the lazy dog.</p>\n<p>third paragraph with bullet list</p>\n<ul>\n<li>1st\n<ul>\n<li>1st c1</li>\n<li>1st c2</li>\n</ul>\n</li>\n<li>2nd</li>\n<li>3rd\n<ul>\n<li>3rd c1</li>\n<li>3rd c2</li>\n</ul>\n</li>\n<li>4th</li>\n</ul>\n<p><strong>Strong text</strong> <em>Italic text</em></p>\n'
        self.blo_article.load_from_file(self.base_file_path_1)
        self.blo_article.convert_to_html()
        from hashlib import sha512
        hs = sha512()
        hs.update(expected_html.encode('utf-8'))
        self.assertEqual(hs.digest(), self.blo_article.get_digest())

    def test_get_digest_2(self):
        expected_html = """<h1>日本語を含んだテストパターンファイル</h1>
<h2>天文と俳句（現代仮名遣い風に編集）</h2>
<h3>寺田寅彦</h3>
<p>俳句季題の分類は普通に <strong>時候</strong> 、''天文'''、 地理 、<code>人事</code>、動物、植物という風になっている。
これらのうちで後の三つは別として、初めの三つの項目中における各季題の分け方は現代の科学知識から見ると、
決して合理的であるとは思われない。</p>
<h2>天文と俳句（原文をそのまま青空文庫より引用）</h2>
<h3>寺田寅彦</h3>
<p><code>俳句季題の分類は普通に時候、天文、地理、人事、動物、植物といふ風になつて居る。此等のうちで後の三つは別として、初めの三つの項目中に於ける各季題の分け方は現代の科學知識から見ると、決して合理的であるとは思はれない。</code></p>
<h2>いくつかの記述要素</h2>
<p>リストを記述する</p>
<ul>
<li>リスト項目1
<ul>
<li>子リスト項目1</li>
<li>子リスト項目2</li>
</ul>
</li>
<li>with english text
<ul>
<li><em>in itarlic</em></li>
<li>日本語の表記と英語( <em>English</em> )の表記を併記した状態でテストを行うためのデータ</li>
</ul>
</li>
</ul>
"""
        self.blo_article.load_from_file(self.base_file_path_2)
        self.blo_article.convert_to_html()
        from hashlib import sha512
        hs = sha512()
        hs.update(expected_html.encode('utf-8'))
        self.assertEqual(hs.digest(), self.blo_article.get_digest())

    def test_get_raw_text_body(self):
        pass
        # TODO: Implement test pattern for wakachigaki-text
        #self.blo_article.load_from_file(self.base_file_path)
        #ast = self.blo_article.get_raw_text_body()


