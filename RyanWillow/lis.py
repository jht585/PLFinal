################ Lispy: Scheme Interpreter in Python

## (c) Peter Norvig, 2010-14; See http://norvig.com/lispy.html

################ Types

from __future__ import division

Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float

VariableMap = {}
FunctionMap = {}
ParameterMap = {}
DEBUG = False

################ Parsing: parse, tokenize, and read_from_tokens

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def tokenize(s):
    "Convert a string into a list of tokens."
    return s.replace('(',' ( ').replace(')',' ) ').split()

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        try: return float(token)
        except ValueError:
            return Symbol(token)

################ Environments

class Env(dict):
    "An environment: a dict of {'var':val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        "Find the innermost Env where var appears."
        return self if (var in self) else self.outer.find(var)

################ Interaction: A REPL

def repl(prompt='lis.py> '):
    "A prompt-read-eval-print loop."
    while True:
        val = eval(parse(raw_input(prompt)))
        if val is not None: 
            print(lispstr(val))

def lispstr(exp):
    "Convert a Python object back into a Lisp-readable string."
    if isinstance(exp, list):

        return '(' + ' '.join(map(lispstr, exp)) + ')' 
    else:
        return str(exp)

################ Procedures

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args): 
        return eval(self.body, Env(self.parms, args, self.env))

################ eval

toReturn = None

def eval(x):
    if DEBUG: print x
    # eval takes an AST that I designed and executes the code
    while len(x) != 0:
        # These are functions that I built
        if x[0] == 'VariableDeclaration':
            VariableMap[x[1]] = x[2]
            x = x[3:]
            if DEBUG: print x
        elif x[0] == 'VariableInst':
            VariableMap[x[1]] = 0
            x = x[2:]
            if DEBUG: print x
        elif x[0] == 'Print':
            # Need to check if x[1] is actual string, string representation of symbol in variable map, or list
            if type(x[1]) == type([]):
                for item in x[1]:
                    try:
                        print VariableMap(item)
                    except KeyError:
                        print item
            else:
                try:
                    print VariableMap[x[1]]
                except KeyError:
                    print x[1]
            x = x[2:]
            if DEBUG: print x
        elif x[0] == 'Comment':
            x = x[1:]
        elif x[0] == 'IfStatement':
             if x[1]:
                 eval(x[2])
             x = x[3:]
        elif x[0] == 'IfElseStatement':
            if x[1]:
                eval(x[2])
            else:
                eval(x[3])
            x = x[4:]
        elif x[0] == 'MathExp':
            if x[3] == '*':
                print x[1] * x[2]
            elif x[3] == '+':
                print x[1] + x[2]
            elif x[3] == '-':
                print x[1] - x[2]
            elif x[3] == '/':
                print x[1] / x[2]
            x = x[4:]
        elif x[0] == 'MathAssExp':
            if x[3] == '*':
                 VariableMap[x[4]] = x[1] * x[2]
            elif x[3] == '+':
                VariableMap[x[4]] = x[1] + x[2]
            elif x[3] == '-':
                VariableMap[x[4]] = x[1] - x[2]
            elif x[3] == '/':
                VariableMap[x[4]] = x[1] / x[2]
            x = x[5:]
        elif x[0] == 'DefineFunction':
            FunctionMap[x[1]] = x[2]
            x = x[3:]
        elif x[0] == 'CallFunction':
            try:
                eval(FunctionMap[x[1]])
            except KeyError:
                print "you are trying to call an undefined"
            x = x[3:]
        else:
            print 'Your code may conform to the grammar rules I wrote but eval don\'t know what to do with it'
            x = x[1:]
