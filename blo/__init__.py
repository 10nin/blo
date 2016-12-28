# -*- coding: utf-8 -*-
import configparser
import optparse
from .BloArticle import BloArticle


class Blo:
    def __init__(self):
        self.article = BloArticle()

if __name__ == '__main__':
    parser = optparse.OptionParser("usage: %prog [option] markdown_file.md")
    parser.add_option("-c", "--config", dest="config_file",
                      default="./blo.cfg", type="string", help="specify configuration file path to run on")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    cfg_file = options.config_file
    # TODO: implement main routine of Blo.
    # blo [-c config_file] markdown_file.md
    # -- if no -c option then load config file from default path (current directory).
    # ---- if no configuration file on current directory blo said error.
    # 1. init database (database name from environment variable or configuration file)
    # 2. parse markdown file from command line argument.
    # -- if command line argument path is directory then it will do recursive in directory.
    # 3. generate html and commit to database
    pass
