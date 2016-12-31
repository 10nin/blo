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
    def __init__(self, template_directory:str='templates'):
        """ BloArticle class initializer.

        :param template_directory: Jinja template directory, default is 'templates'"""
        self._raw_text = ""
        self._html_text = ""
        self._template_directory = template_directory
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

    def get_html(self, template_name: str='') -> str:
        if self._html_text == "":
            self._html_text = self._convert_to_html(template_name)
        return self._html_text

    def _convert_to_html(self, template_name: str='') -> str:
        """ Convert from raw markdown text to html.

        :return: html formatted text
        """
        html = ""
        if template_name == "":
            html = CommonMark.commonmark(self._raw_text)
        else:
            template = self._get_template(template_name)
            html_parts = self._get_html_parts()
            html = template.render(html_parts=html_parts)

        return html

    def _get_html_parts(self):

        # initialize html parts dictionary
        ret = {'title': '', 'body': ''}
        for l in self._raw_text.split('\n'):
            # First H1 size text set to page title
            if re.match(r'# .+$', l):
                ret['title'] = l.replace('#', '').strip()
                break

        # self html text set to body html
        ret['body'] = CommonMark.commonmark(self._raw_text)

        return ret

    def _get_raw_text_body(self) -> str:
        """Get text data from raw markdown text without any markup.

        :return: text data without any markup
        """
        if self._html_text == '':
            self.get_html()

        # remove html tags
        return re.sub(r'\n+', '\n', re.sub(r'<.+?>', "", self._html_text))

    def get_digest(self) -> str:
        self.hs.update(self._html_text.encode('utf-8'))
        return self.hs.hexdigest()

    def get_wakati_txt(self) -> str:
        mcb = MeCab.Tagger("-Owakati")
        wakachi_txt = mcb.parse(self._get_raw_text_body())
        return wakachi_txt

    def _get_template(self, template_name:str):
        ld = jinja2.FileSystemLoader(self._template_directory)
        e = jinja2.Environment(loader=ld, trim_blocks=True, lstrip_blocks=True)
        return e.get_template(template_name)

