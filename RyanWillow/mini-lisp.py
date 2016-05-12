# -*- coding: utf-8 -*-
from yacc import yacc, willow_list
import lis as lis

def main():
    with open('testfile.c', 'r') as content_file:
        content = content_file.read()
        print content
        AST = yacc.parse(content)
        if AST != None:
            result = lis.eval(AST)
            print (result)

main()