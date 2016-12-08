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

    def test_get_raw_text_body_2(self):
        expected_txt = "日本語を含んだテストパターンファイル\n天文と俳句（現代仮名遣い風に編集）\n寺田寅彦\n俳句季題の分類は普通に 時候 、''天文'''、 地理 、人事、動物、植物という風になっている。\nこれらのうちで後の三つは別として、初めの三つの項目中における各季題の分け方は現代の科学知識から見ると、\n決して合理的であるとは思われない。\n天文と俳句（原文をそのまま青空文庫より引用）\n寺田寅彦\n俳句季題の分類は普通に時候、天文、地理、人事、動物、植物といふ風になつて居る。此等のうちで後の三つは別として、初めの三つの項目中に於ける各季題の分け方は現代の科學知識から見ると、決して合理的であるとは思はれない。\nいくつかの記述要素\nリストを記述する\nリスト項目1\n子リスト項目1\n子リスト項目2\nwith english text\nin itarlic\n日本語の表記と英語( English )の表記を併記した状態でテストを行うためのデータ\n"
        self.blo_article.load_from_file(self.base_file_path_2)
        base_txt = self.blo_article._get_raw_text_body()
        self.assertEqual(expected_txt, base_txt)

    def text_get_wakati_text_body_2(self):
        expected_txt = "日本語 を 含ん だ テストパターン ファイル 天文 と 俳句 （ 現代 仮名遣い 風 に 編集 ） 寺田 寅彦 俳句 季題 の 分類 は 普通 に 時候 、 '' 天文 '''、 地理 、 人事 、 動物 、 植物 という 風 に なっ て いる 。 これら の うち で 後 の 三つ は 別 として 、 初め の 三つ の 項目 中 における 各 季題 の 分け 方 は 現代 の 科学 知識 から 見る と 、 決して 合理 的 で ある と は 思わ れ ない 。 天文 と 俳句 （ 原文 を そのまま 青空 文庫 より 引用 ） 寺田 寅彦 俳句 季題 の 分類 は 普通 に 時候 、 天文 、 地理 、 人事 、 動物 、 植物 といふ 風 に なつ て 居る 。 此等 の うち で 後 の 三つ は 別 として 、 初め の 三つ の 項目 中 に 於け る 各 季題 の 分け 方 は 現代 の 科 學 知識 から 見る と 、 決して 合理 的 で ある と は 思は れ ない 。 いくつ か の 記述 要素 リスト を 記述 する リスト 項目 1 子 リスト 項目 1 子 リスト 項目 2 with english text in itarlic 日本語 の 表記 と 英語 ( English ) の 表記 を 併記 し た 状態 で テスト を 行う ため の データ \n"
        self.blo_article.load_from_file(self.base_file_path_2)
        self.blo_article._get_raw_text_body()
        wakati_txt = self.blo_article.get_wakati_txt()
        self.assertEqual(expected_txt, wakati_txt)
