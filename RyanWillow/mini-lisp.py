# -*- coding: utf-8 -*-
from yacc import yacc, willow_list
import lis as lis

def main():
    with open('testfile.c', 'r') as content_file:
        content = content_file.read()
        AST = yacc.parse(content)
        print AST
        if AST != None:
            lis.eval(AST)


main()