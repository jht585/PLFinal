import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = False

# Namespace & built-in functions

BuiltInFuctionMap = {}

def generic_function(l):
    return [l[0]] + l[1]

BuiltInFuctionMap['generic_function'] = generic_function

def willow_list(l):
    def recur(outList,inList):
        print str(outList) + '\n' + str(inList)
        if type(inList[0]) == type([]):
            return recur(outList,inList[0])
        if len(inList) > 1:
           outList += inList
           return recur(outList,inList[1:])
        else:
            outList += inList
            #return recur(outList,inList[1:])
        return outList
    return recur([],l)




# eval rules
def p_exp_stmt(p):
    'stmts : stmt'
    if DEBUG: print "handling a line"
    p[0] = p[1]

def p_exp_exp_stmt(p):
    'stmts : stmts stmt'
    if DEBUG: print str(p[1]) + '   ' + str(p[2])
    if type(p[2]) == type(' '):
        p[0] = p[1] + [p[2]]
    else:
        p[0] = p[1] + p[2]


def p_atoms_atom(p):
    'atoms : atom'
    if DEBUG: print "Evaluating atom to atoms"
    p[0] = p[1]

def p_atoms(p):
    'atoms : atom atoms'
    if DEBUG: print "Evaluating atoms to atoms"
    p[0] = p[1] + p[2]

def p_atom_simb(p):
    'atom : simb'
    if DEBUG: print "Evaluating simb to atom"
    p[0] = p[1]

def p_dec_stmt(p):
    'stmt : declaration'
    if DEBUG: print "evaluating declaration to stmt"
    p[0] = p[1]

# handling basic token rules
def p_atom_int(p):
    'atom : NUM'
    if DEBUG: print "SawToken INT"
    p[0] = p[1]

def p_atom_float(p):
    'atom : NUM DOT NUM'
    if DEBUG: print "SawToken FLOAT"
    p[0] = str(p[1]) + '.' + str(p[3])

def p_atom_word(p):
    'atom : TEXT'
    if DEBUG: print "SawToken Text"
    p[0] = p[1]

def p_false(p):
    'atom : FALSE'
    if DEBUG: print "SawToken FALSE"
    p[0] = False

def p_true(p):
    'atom : TRUE'
    if DEBUG: print "SawToken TRUE"
    p[0] = True

def p_empty(p):
    'atom :'
    if DEBUG: print "Saw empty"
    pass

def p_simb(p):
    'simb : SIMB'
    if DEBUG: print "SawToken Simbol"
    p[0] = p[1]

def p_math_op_plus(p):
    'mathop : PLUS'
    if DEBUG: print 'SawToken Plus'
    p[0] = p[1]

def p_math_op_minus(p):
    'mathop : MINUS'
    if DEBUG: print 'SawToken MINUS'
    p[0] = p[1]

def p_math_op_mult(p):
    'mathop : MULT'
    if DEBUG: print 'SawToken MULT'
    p[0] = p[1]

def p_math_op_div(p):
    'mathop : DIV'
    if DEBUG: print 'SawToken DIV'
    p[0] = p[1]



# Statement Grammar Rules
def p_dec_variable(p):
    'declaration : VAR simb EQUALS atoms SEMI'
    if DEBUG: print "Saw a variable declaration"
    p[0] = ["VariableDeclaration",p[2],p[4]]

def p_inst_var(p):
    'declaration : VAR simb SEMI'
    if DEBUG: print "Saw a variable instantiation"
    p[0] = ["VariableInst",p[2]]

def p_assignment(p):
    'stmt : simb EQUALS atoms SEMI'
    if DEBUG: "print saw an assignment"
    p[0] = ['Assignment',p[1],p[3]]

def p_comment(p):
    'stmt : DIV DIV atoms'
    if DEBUG: print "Saw a Comment"
    p[0] = "Comment"

def p_comment_stmt(p):
    'stmt : DIV DIV stmts'
    if DEBUG: print "Saw a Comment"
    p[0] = "Comment"


def p_print(p):
    'stmt : PRINT atoms SEMI'
    if DEBUG: print "saw print statement"
    p[0] = ["Print",p[2]]

def p_if(p):
    'stmt : IF LPAREN exp RPAREN LCURLY stmts RCURLY'
    if DEBUG: print "saw an if stmt"
    p[0] = ["IfStatement",p[3],p[6]]

def p_if_else(p):
    'stmt : IF LPAREN exp RPAREN LCURLY stmts RCURLY ELSE LCURLY stmts RCURLY'
    if DEBUG: print "saw an if else stmt"
    p[0] = ["IfElseStatement",p[3],p[6],p[10]]

def p_def_fun(p):
    'stmt : DEF SIMB LPAREN RPAREN LCURLY stmts RCURLY'
    if DEBUG: print "saw a function defnition"
    p[0] = ["DefineFunction",p[2],p[6]]

def p_call_fun(p):
    'stmt : SIMB LPAREN RPAREN SEMI'
    if DEBUG: print "saw a function call"
    p[0] = ["CallFunction", p[1]]

def p_exp_equals(p):
    'exp : atoms EQ_OP atoms'
    if DEBUG: print "saw == expression"
    if p[1] == p[3]:
        p[0] = True
    else:
        p[0] = False

def p_math_exp(p):
    'stmt : atom mathop atom SEMI'
    if DEBUG: print "handling math expression"
    p[0] = ["MathExp",p[1],p[3],p[2]]

def p_math_ass(p):
    'stmt : simb EQUALS atom mathop atom SEMI'
    if DEBUG: print "handling math assignment expression"
    p[0] = ["MathAssExp",p[3],p[5],p[4],p[1]]

def p_float_int(p):
    'stmt : VAR simb EQUALS LPAREN FLOAT RPAREN atom SEMI'
    if DEBUG: print "casting num to float"
    p[0] = ["FloatCast",p[2],p[7]]

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()


