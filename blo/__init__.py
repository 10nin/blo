import configparser
from blo.BloArticle import BloArticle
from blo.DBControl import DBControl


class Blo:
    def __init__(self, config_file_path):
        config = configparser.ConfigParser()
        config.read(config_file_path)
        self.template_dir = config['TEMPLATE']['TEMPLATE_DIR']
        self.db_file_path = config['DB']['DB_PATH']

        # create tables
        self.db_control = DBControl(self.db_file_path)
        self.db_control.create_tables()
        self.db_control.close_connect()

    def insert_article(self, file_path):
        self.db_control = DBControl(self.db_file_path)
        article = BloArticle(self.template_dir)
        article.load_from_file(file_path)
        self.db_control.insert_article(article)
        self.db_control.close_connect()
