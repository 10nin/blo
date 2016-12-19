from .BloArticle import BloArticle


class Blo:
    def __init__(self):
        pass

if __name__ == '__main__':
    # TODO: implement main routine of Blo.
    # blo [-c config_file] markdown_file.md
    # -- if no -c option then load config file from default path (current directory).
    # ---- if no configuration file on current directory blo said error.
    # 1. init database (database name from environment variable or configuration file)
    # 2. parse markdown file from command line argument.
    # -- if command line argument path is directory then it will do recursive in directory.
    # 3. generate html and commit to database
    pass
