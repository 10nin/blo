import configparser
from blo.BloArticle import BloArticle
from blo.DBControl import DBControl


class Blo:
    def __init__(self, config_file_path):
        config = configparser.ConfigParser()
        config.read(config_file_path)
        self._db_file_path = config['DB']['DB_PATH'].replace('"', '')
        self._template_dir = config['TEMPLATE']['TEMPLATE_DIR'].replace('"', '')
        self._default_template_file = config['TEMPLATE']['DEFAULT_TEMPLATE_FILE'].replace('"', '')

        # create tables
        self._db_control = DBControl(self._db_file_path)
        self._db_control.create_tables()
        self._db_control.close_connect()

    def insert_article(self, file_path):
        self._db_control = DBControl(self._db_file_path)
        article = BloArticle(self._template_dir)
        article.load_from_file(file_path)
        self._db_control.insert_article(article, self._default_template_file)
        self._db_control.close_connect()
