import ply.yacc as yacc
from analizadorlexico import tokens
from analizadorSemantico import *

precedence = (
	('right','ID','CALL','BEGIN','IF','WHILE'),
	('right','PROCEDURE'),
	('right','INTEGER'),
	('right', 'OPER_ASSIG'),
	('right','UPDATE'),
	('left','OPER_NE'),
	('left','OPER_MAYOR','OPER_MENOR','OPER_IDENTICO','OPER_DIFERENTE','OPER_MAYORIGU','OPER_MENORIGU'),
	('left','OPER_SUMA','OPER_DIF'),
	('left','OPER_DIV','OPER_MUL'),
	('left','PAR_INI','PAR_FIN'),
)

def p_program(p):
	'''program : block'''
	p[0] = program(p[1],"program")


def p_block(p):
	'''block : constDecl varDecl procDecl statement'''
	p[0] = block(p[1],p[2],p[3],p[4],"block")

def p_constDecl(p):
	'''constDecl : CONST constAssignmentList DOTCOM'''
	p[0] = constDecl(p[2],"constDecl")

def p_constDeclEmpty(p):
	'''constDecl : empty'''
	p[0] = Null()

def p_constAssignmentList1(p):
	'''constAssignmentList : ID OPER_ASSIG NUMBER'''
	p[0] = constAssignmentList1(Id(p[1]),Assign(p[2]),Number(p[3]),"constAssignmentList1")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMA ID OPER_ASSIG NUMBER'''
	p[0] = constAssignmentList2(p[1],Id(p[3]),Assign(p[4]),Number(p[5]),"constAssignmentList2")

def p_varDecl1(p):
	'''varDecl : type identList DOTCOM'''
	p[0] = varDecl1(p[2],"VarDecl1")

def p_type1(p):
  '''type : INTEGER'''
  p[0] = type1(INTEGER(p[1]),"Integer")
  
def p_type2(p):
  '''type : FLOAT'''
  p[0] = type2(FLOAT(p[1]),"Float")
  
def p_type3(p):
  '''type : DOUBLE'''
  p[0] = type3(DOUBLE(p[1]),"Double")

def p_type4(p):
  '''type : STRING'''
  p[0] = type4(STRING(p[1]),"String")

def p_type5(p):
  '''type : CHARACTER'''
  p[0] = type4(CHARACTER(p[1]),"Character")

def p_type6(p):
  '''type : BOOLEAN'''
  p[0] = type4(BOOLEAN(p[1]),"Boolean")


def p_varDeclEmpty(p):
	'''varDecl : empty'''
	p[0] = Null()

def p_identList1(p):
	'''identList : ID'''
	p[0] = identList1(Id(p[1]),"identList1")
	#p


def p_identList2(p):
	'''identList : identList COMA ID'''
	p[0] = identList2(p[1],Id(p[3]),"identList2")


def p_procDecl1(p):
	'''procDecl : procDecl PROCEDURE ID DOTCOM block DOTCOM'''
	p[0] = procDecl1(p[1],Id(p[3]),p[5],"procDecl1")

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	p[0] = Null()

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	p[0] = statement1(Id(p[1]),Update(p[2]),p[3],"statement1")

def p_statement2(p):
	'''statement : CALL ID'''
	p[0] = statement2(Id(p[2]),"statement2")

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	p[0] = statement3(p[2],"statement3")

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	p[0] = statement4(p[2],p[4],"statement4")

def p_statement5(p):
	'''statement : WHILE condition DO statement'''
	p[0] = statement5(p[2],p[4],"statement5")

def p_statementEmpty(p):
	'''statement : empty'''
	p[0] = Null()

def p_statementList1(p):
	'''statementList : statement'''
	p[0] = statementList1(p[1],"statementList1")

def p_statementList2(p):
  '''statementList : statementList DOTCOM statement'''
  p[0] = statementList2(p[1],p[3],"statementList2")

def p_condition1(p):
	'''condition : expression relation expression'''
	p[0] = condition1(p[1],p[2],p[3],"condition1")

def p_relation1(p):
	'''relation : OPER_ASSIG'''
	p[0] = relation1(Assign(p[1]),"relation1")

def p_relation2(p):
	'''relation : OPER_NE'''
	p[0] = relation2(NE(p[1]),"relation2")

def p_relation3(p):
	'''relation : OPER_MAYOR'''
	p[0] = relation3(OPER_MAYOR(p[1]),"relation3")

def p_relation4(p):
	'''relation : OPER_MENOR'''
	p[0] = relation4(OPER_MENOR(p[1]),"relation4")

def p_relation5(p):
	'''relation : OPER_MAYORIGU'''
	p[0] = relation5(OPER_MAYORIGU(p[1]),"relation5")

def p_relation6(p):
	'''relation : OPER_MENORIGU'''
	p[0] = relation6(OPER_MENORIGU(p[1]),"relation6")


def p_relation7(p):
	'''relation : OPER_DIFERENTE'''
	p[0] = relation7(OPER_DIFERENTE(p[1]),"relation7")


def p_relation8(p):
	'''relation : OPER_IDENTICO'''
	p[0] = relation8(OPER_IDENTICO(p[1]),"relation8")

def p_expression1(p):
	'''expression : term'''
	p[0] = expression1(p[1],"expression1")

def p_expression2(p):
	'''expression : addingOperator term'''
	p[0] = expression2(p[1],p[2],"expression2")

def p_expression3(p):
	'''expression : expression addingOperator term'''
	p[0] = expression3(p[1],p[2],p[3],"expression3")

def p_addingOperator1(p):
  '''addingOperator : OPER_SUMA'''
  p[0] = addingOperator1(Plus(p[1]),"addingOperator")


def p_addingOperator2(p):
	'''addingOperator : OPER_DIF'''
	p[0] = addingOperator2(Minus(p[1]),"subtractionOperator")

def p_term1(p):
	'''term : factor'''
	p[0] = term1(p[1],"term1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	p[0] = term2(p[1],p[2],p[3],"term2")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : OPER_MUL'''
	p[0] = multiplyingOperator1(Times(p[1]),"multiplyingOperator")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : OPER_DIV'''
	p[0] = multiplyingOperator2(Divide(p[1]),"divisiongOperator")

def p_factor1(p):
	'''factor : ID'''
	p[0] = factor1(Id(p[1]),"factor1")


def p_factor2(p):
	'''factor : NUMBER'''
	p[0] = factor2(Number(p[1]),"factor2")

def p_factor3(p):
	'''factor : PAR_INI expression PAR_FIN'''
	p[0] = factor3(p[2],"factor3")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)

def traducir(result):
  graphFile = open('graphviztrhee.vz','w')
  graphFile.write(result.traducir())
  graphFile.close()
  print ("El programa traducido se guardo en \"graphviztrhee.vz\"")

fp = open('ej4.txt',"r")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena, debug=1)

traducir (result)
