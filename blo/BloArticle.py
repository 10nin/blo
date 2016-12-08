# -*- coding: utf-8 -*-
import re
import pathlib
import CommonMark
from hashlib import sha512


class BloArticle:
    """Article of Blo. written markdown style.
    """
    def __init__(self):
        self._raw_text = ''
        self._html_text = ''
        self.hs = sha512()

    def load_from_file(self, file_path:str):
        """ The main markdown contents oad from file.

        :param file_path: path to target markdown file. if file_path is not exists then raise FileNotFoundError.
        """
        if pathlib.Path(file_path).exists():
            with open(file_path) as f:
                self._raw_text = "".join(f.readlines())
        else:
            raise FileNotFoundError()

    def convert_to_html(self, template_name:str="") -> str:
        """ Convert from raw markdown text to html.

        :param template_name: Jinja template file name (find on templates directory), default is empty
        :return: html formatted text
        """
        if template_name == "":
            self._html_text = CommonMark.commonmark(self._raw_text)
        else:
            # TODO: implement generate from markdown to jinja template applied html text
            pass

        return self._html_text

    def get_raw_text_body(self)->str:
        """Get text data from raw markdown text without any markup.

        :return: text data without any markup
        """
        if self._html_text == '':
            self.convert_to_html()

        # remove html tags
        return re.sub(r'\n+', '\n', re.sub(r'<.+?>', "", self._html_text))

    def get_digest(self)->str:
        self.hs.update(self._html_text.encode('utf-8'))
        return  self.hs.digest()

