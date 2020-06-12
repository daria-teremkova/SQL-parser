import sys

import json
import astpretty
from antlr4 import FileStream
from antlr4.tree import Trees

from sqlast import parse

from printer import print_tree
from sql_parser.sqlLexer import sqlLexer
from sql_parser.sqlParser import sqlParser, CommonTokenStream
from utils import *


def select_query():
    path = './sw_templates.json'

    with open(path, 'r') as f:
        data = json.loads(f.read())
        for i in data['employee']:
            if i['id'] == '3':
                print(i['firstName'])


def main():
    # input_stream = FileStream('./sql_stmt.sql')
    # lexer = sqlLexer(input_stream)
    # stream = CommonTokenStream(lexer)
    # parser = sqlParser(stream)
    # tree = parser.root()
    #
    # t = Trees.Trees.toStringTree(tree, parser.ruleNames)
    # print(t)
    #select_query()
    ast_tree = parse(read_file('./sql_stmt.sql'))
    print_tree(ast_tree)


if __name__ == '__main__':
    main()
