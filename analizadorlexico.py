import ply.lex as lex

reservadas = [ 'IF', 'ELSE', 'WHILE','THEN', 'IN','FOR', 'BREAK', 'CLASS','RETURN', 'TRUE', 'FALSE','DO','AND','OR','IS','CONST','PROCEDURE','BEGIN','END','CALL','INTEGER','FLOAT','DOUBLE','CHARACTER','STRING', 'BOOLEAN','MAIN','INPUT', 'OUTPUT','TRY', 'CATCH','FUNTION', 'PRINT']

#reserved = {
 #   'si' : 'IF',
  #  'entonce' : 'ELSE',
  #  'mientras' : 'WHILE',
  #  'Detente' : 'BREAK',
 #   'gimnasio': 'CLASS',
 #   'regresa' : 'RETURN',
 #   'cierto' : 'TRUE',
 #   'falacia' : 'FALSE',
 #   'y' : 'AND',
 #   'o' : 'OR',
 #   'es': 'IS',
  #  'entero' : 'INTEGER',
  #  'letra' : 'CHARACTER',
  #  'palabra' : 'STRING',
  #  'boleano' : 'BOOLEAN',
  #  'pokebola' : 'MAIN',
  #  'obten' : 'INPUT',
  #  'habla' : 'OUTPUT',
  #  'trata':'TRY',
  #  'captura': 'CATCH',
  #  'entrenador' : 'FUNTION',
  #  'yo_te_elijo' : 'PRINT'
#}
#tokens = tokens +reservadas.Value()


tokens = reservadas+[
'ID',
'NUMBER',
'OPER_SUMA',
'OPER_DIF',
'OPER_DIV',
'OPER_MUL',
'OPER_ASSIG',
'OPER_MOD',
'OPER_NE',
'OPER_MAYOR',
'OPER_MENOR',
'OPER_IDENTICO',
'OPER_DIFERENTE',
'OPER_MAYORIGU',
'OPER_MENORIGU',
'PAR_INI',
'PAR_FIN',
'KEY_INI',
'KEY_FIN',
'CORCH_INI',
'CORCH_FIN',
'OPER_ACCES',
'COMA',
'DOTCOM',
'UPDATE'
]



t_ignore = '\t '
t_OPER_SUMA = r'\+'
t_OPER_DIF = r'\-'
t_OPER_MUL = r'\*'
t_OPER_DIV = r'/'
t_OPER_ASSIG = r'='
t_OPER_MOD = r'%'
t_OPER_NE = r'<>'
t_OPER_MENOR = r'<'
t_OPER_IDENTICO = r'=='
t_OPER_DIFERENTE = r'!='
t_OPER_MENORIGU = r'<='
t_OPER_MAYOR = r'>'
t_OPER_MAYORIGU = r'>='
t_PAR_INI = r'\('
t_PAR_FIN = r'\)'
t_KEY_INI = r'\{'
t_KEY_FIN = r'\}'
t_CORCH_INI = r'\['
t_CORCH_FIN = r'\]'
t_COMA = r','
t_DOTCOM = r';'
t_OPER_ACCES = r'\.'
t_UPDATE = r':='

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()

		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_COMMENT(t):
	r'\#.*'
	pass

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_error(t):
	print ("caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)


analizador = lex.lex()


