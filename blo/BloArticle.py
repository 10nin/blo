# -*- coding: utf-8 -*-
import pathlib
from hashlib import sha512


class BloArticle:
    """Article of Blo. written markdown style.
    """
    def __init__(self):
        self.raw_text = ''
        self.html_text = ''
        self.hs = sha512()

    def load_from_file(self, file_path):
        """ The main markdown contents oad from file.
        :param file_path: path to target markdown file. if file_path is not exists then raise FileNotFoundError.
        """
        if pathlib.Path(file_path).exists():
            with open(file_path) as f:
                self.raw_text = f.readlines()
        else:
            raise FileNotFoundError()

    def convert_to_html(self):
        pass

    def get_digest(self):
        self.hs.update(self.html_text.encode('utf-8'))
        return  self.hs.digest()

