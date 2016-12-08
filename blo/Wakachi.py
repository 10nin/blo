import MeCab
from . import BloArticle


class Wakachi:
    def __init__(self, article: BloArticle.BloArticle):
        self._target_article = article

    def wakachi(self) -> str:
        mcb = MeCab.Tagger("-Owakati")
        wakachi_txt = mcb.parse(self._target_article.get_raw_text_body())
        return wakachi_txt
