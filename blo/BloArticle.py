# -*- coding: utf-8 -*-
import re
import pathlib
import CommonMark
import MeCab
import jinja2
from hashlib import sha512


class BloArticle:
    """Article of Blo. written markdown style.
    """
    def __init__(self, template_name: str= ""):
        """ BloArticle class initializer.

        :param template_name: Jinja template file name (find on templates directory), default is empty"""
        self._raw_text = ""
        self._html_text = ""
        self._template_name = ""
        self.hs = sha512()
        self.has_text = False

    def load_from_file(self, file_path: str):
        """ The main markdown contents oad from file.

        :param file_path: path to target markdown file. if file_path is not exists then raise FileNotFoundError.
        """
        if pathlib.Path(file_path).exists():
            with open(file_path) as f:
                self._raw_text = "".join(f.readlines())
            self.has_text = True
        else:
            raise FileNotFoundError()

    def get_html(self) -> str:
        if self._html_text == "":
            self._html_text = self._convert_to_html()
        return self._html_text

    def _convert_to_html(self) -> str:
        """ Convert from raw markdown text to html.

        :return: html formatted text
        """
        html = ""
        if self._template_name == "":
            html = CommonMark.commonmark(self._raw_text)
        else:
            template = self._get_template()
            html_parts = self._get_html_parts()
            html = template.render(title=html_parts['title'], bdoy=html_parts['body'])

        return html

    def _get_html_parts(self):
        ret = dict()
        # TODO: implement get html parts dictionary from MarkDown document.
        # TODO: it dictionary need 'title' key and 'body' key.
        ret['title'] = self._html_text
        ret['body'] = self._html_text
        return ret

    def _get_raw_text_body(self) -> str:
        """Get text data from raw markdown text without any markup.

        :return: text data without any markup
        """
        if self._html_text == '':
            self._convert_to_html()

        # remove html tags
        return re.sub(r'\n+', '\n', re.sub(r'<.+?>', "", self._html_text))

    def get_digest(self) -> str:
        self.hs.update(self._html_text.encode('utf-8'))
        return self.hs.digest()

    def get_wakati_txt(self) -> str:
        mcb = MeCab.Tagger("-Owakati")
        wakachi_txt = mcb.parse(self._get_raw_text_body())
        return wakachi_txt

    def _get_template(self):
        ld = jinja2.FileSystemLoader('template')
        e = jinja2.Environment(loader=ld, trim_blocks=True, lstrip_blocks=True)
        return e.get_template(self._template_name)

