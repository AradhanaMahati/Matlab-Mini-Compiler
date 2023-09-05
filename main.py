#ARADHANA MAHATI PES1UG21CS105
#AMRITHA GK PES1UG21CS073

import ply.lex as lex
import ply.yacc as yacc


fh=open('data5.txt')
data=fh.read()

tokens = [
    'ASSIGN',
    'NUMBER',
    'SEMICOLON',
    'COMMA',
    'COLON',
    'L_BRACES',
    'R_BRACES',
    'SQR_LBRACE',
    'SQR_RBRACE',
    'EQUALS',
    'NOTEQUALS',
    'GREATER_THAN_OR_EQUAL_TO',
    'LESSER_THAN_OR_EQUAL_TO',
    'GREATER_THAN',
    'LESSER_THAN',
    'QUOTE',
    'ID',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'AND',
    'OR',
    'NOT',
    'POW',
    'PLACEHOLDER',
]

reserved = {
    'fprintf' : 'fprintf',
    'for' : 'for',
    'end' : 'end',
    'while' : 'while',
    'if' : 'if',
    'elseif' : 'elseif',
    'else' : 'else',
}

t_ignore = " \t\n"
t_EQUALS = r'[=]{2}'
t_ASSIGN = r'[=]'
t_NUMBER = r'\d+'
t_SEMICOLON=r'[;]'
t_COMMA = r'[,]'
t_COLON=r'[:]'
t_QUOTE=r'[\']'
t_L_BRACES=r"[(]"
t_R_BRACES=r"[)]"
t_SQR_LBRACE = r'[\[]'
t_SQR_RBRACE = r'[\]]'
t_NOTEQUALS = r'!='
t_GREATER_THAN_OR_EQUAL_TO = r'>='
t_LESSER_THAN_OR_EQUAL_TO = r'<='
t_GREATER_THAN = r'[>]'
t_LESSER_THAN = r'[<]'
t_PLUS = r'[+]'
t_MINUS = r'[-]'
t_MULTIPLY = r'[*]'
t_DIVIDE = r'[/]'
t_AND = r'[&]'
t_OR = r'[|]'
t_NOT = r'[~]'
t_POW = r'[\^]'
t_PLACEHOLDER = r'%d'


tokens += list(reserved.values())


def t_ID(t): #variables 
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input(data)

for tok in lexer:
    print(tok)

def p_main(p):
    '''main : program'''
    print("Syntax is Correct.")

def p_program(p):
    '''program : Declaration program
                | Fprintf program
                | For program End
                | While program End
                | If program End
                | 
    '''
def p_operator(p):
    '''Operator : EQUALS
            | NOTEQUALS
            | GREATER_THAN_OR_EQUAL_TO
            | LESSER_THAN_OR_EQUAL_TO
            | GREATER_THAN
            | LESSER_THAN
            | AND
            | OR
            | PLUS
            | MINUS
            | MULTIPLY
            | DIVIDE
            | POW
    '''

def p_declaration(p):
    '''Declaration : ID ASSIGN exp SEMICOLON
    '''

def p_exp(p):
    '''exp : exp Operator exp
            | L_BRACES exp R_BRACES
            | Operand
            | NOT exp
    '''

def p_forcondition(p):
    '''forCondition : ID ASSIGN NUMBER COLON NUMBER COLON NUMBER
                    | ID ASSIGN NUMBER COLON NUMBER 
    '''

def p_array(p):
    '''array : SQR_LBRACE vector SQR_RBRACE '''

def p_vector(p):
    '''vector : rowvector
                | colvector
    '''

def p_rowvector(p):
    '''rowvector : Operand COMMA rowvector
                | Operand
    '''

def p_colvector(p):
    '''colvector : Operand SEMICOLON colvector
                | Operand
    '''

def p_End(p):
    '''End : end'''

def p_If(p):
    '''If : if checkCondition program Block '''

def p_Block(p):
    '''Block : elseif checkCondition program else program
            | else program 
            | elseif checkCondition program Block 

            '''

def p_Fprintf(p):
    '''Fprintf : fprintf L_BRACES QUOTE content QUOTE COMMA exp R_BRACES SEMICOLON
            | fprintf L_BRACES QUOTE content QUOTE R_BRACES SEMICOLON
    '''

def p_content(p):
    '''content : ID content
                | PLACEHOLDER content
                |
    '''

def p_For(p):
    '''For : for L_BRACES forCondition R_BRACES program'''


def p_While(p):
    '''While : while checkCondition program '''

def p_Condition(p):
    '''checkCondition : L_BRACES exp R_BRACES '''

def p_operand(p):
    '''Operand : NUMBER 
            | ID
            | array
    '''

def p_error(p):
    print(p, "Syntax error in this line")
    quit()

start = ('main')

yacc.yacc()

yacc.parse(data)

fh.close()