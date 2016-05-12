#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

reserved = {
    'VAR'    : 'var',    # eval -> stmt
    'IF'     : 'if',    # eval -> stmt
    'ELSE'   : 'else',    # eval -> stmt
    'WHILE'  : 'while',    # eval -> stmt
    'FOR'    : 'for',    # eval -> stmt
    'INT'    : 'int',    # eval to object
    'FLOAT'  : 'float',  # eval to object
    'BOOL'   : 'bool',   # eval to object
    'VOID'   : 'void',   # eval to object
    'STR'    : 'str',    # eval to object
    'CLASS'  : 'class',      # eval -> stmt
    'DEF'    : 'def',    # eval -> stmt
    'TRUE'   : 'true',   # eval to object
    'FALSE'  : 'false',  # eval to object
    'RETURN' : 'return',    # eval -> stmt
    'LN'     : 'ln',    # eval -> stmt
    'LOG'    : 'log',    # eval -> stmt
    'EXP'    : 'exp',    # eval -> stmt
    'PRINT'  : 'print',    # eval -> stmt
    'ROUND'  : 'round',    # eval -> stmt
    'FLOOR'  : 'floor',    # eval -> stmt
    'CEILING': 'ceiling',    # eval -> stmt
    'ARRAY'  : 'array',   # eval to object
    'SET'    : 'set',    # eval to object
    'DICT'   : 'dict',   # eval to object
    'DO'     : 'do',    # eval -> stmt
    'NIL'    : 'nil',   # eval to object
}
# List of token names.   
tokens = ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LCURLY', 'RCURLY', 'SEMI', 'EQ_OP', 'NE_OP', 'LE_OP', 'GE_OP',
          'EQUALS', 'LT_OP', 'GT_OP', 'MINUS', 'PLUS', 'MULT', 'DIV', 'PRCNT', 'BANG', 'COMMA', 'SQUOTE', 'DOT',
          'SIMB', 'NUM', 'TEXT', 'SIMB'] + list(reserved.keys())

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\['
t_RBRACE = r']'
t_LCURLY = r'{'
t_RCURLY = r'\}'
t_SEMI   = r';'
t_EQ_OP  = r'=='
t_NE_OP  = r'!='
t_LE_OP  = r'<='
t_GE_OP  = r'>='
t_EQUALS = r'='
t_LT_OP  = r'<'
t_GT_OP  = r'>'
t_MINUS  = r'-'
t_PLUS   = r'\+'
t_MULT   = r'\*'
t_DIV    = r'/'
t_PRCNT  = r'%'
t_BANG   = r'!'
t_COMMA  = r','
t_SQUOTE = r"'"
t_DOT    = r'.'

# Ryan's regular expressions, not sure if I need to make tokens for all of these or simply leave as symbols and lookup in built in function dict


def t_NUM(t):
    r'\d+'
    try:
        t.value = int(t.value)    
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_SIMB(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.type = t.value.upper()
    else:
        t.type = 'SIMB'
    return t

def t_TEXT(t):
    r'\'[ -~]+\''
    #r'\'[a-zA-Z0-9_+\*\- :,]*\''
    if t.value.upper() in reserved: # Check for reserved words
        t.type = t.value.upper()
    else:
        t.type = 'TEXT'
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
