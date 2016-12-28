# -*- coding: utf-8 -*-
import optparse
from blo import Blo

if __name__ == '__main__':
    parser = optparse.OptionParser("usage: %prog [options] markdown_file.md")
    parser.add_option("-c", "--config", dest="config_file",
                      default="./blo.cfg", type="string", help="specify configuration file path to run on")
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("incorrect number of arguments")
    cfg_file = options.config_file

    blo_main = Blo(cfg_file)
    blo_main.insert_article(args[0])

    print('%s complete process.'%('blo',))
