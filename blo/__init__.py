from blo.BloArticle import BloArticle
from blo.DBControl import DBControl


class Blo:
    def __init__(self, db_file_path, template_dir=""):
        self.template_dir = template_dir
        # create tables
        self.db_file_path = db_file_path
        self.db_control = DBControl(self.db_file_path)
        self.db_control.create_tables()
        self.db_control.close_connect()

    def insert_article(self, file_path):
        self.db_control = DBControl(self.db_file_path)
        article = BloArticle(self.template_dir)
        article.load_from_file(file_path)
        self.db_control.insert_article(article)
        self.db_control.close_connect()
