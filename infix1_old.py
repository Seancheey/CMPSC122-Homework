# author: Qiyi Shan
# Date: 1/11/2017

def eval_infix(expr):
	return RPN_to_result(to_RPN_expr(expr.split() + [ ";"]))


def get_priority(notation):
	"""
	:param notation: accept + - * / ** ( notation
	:return: it's operating priority
	"""
	if notation == '+' or notation == '-':
		return 1
	if notation == '*' or notation == '/':
		return 2
	if notation == '**':
		return 3
	if notation == '(':
		return 10

def to_RPN_expr(expr):
	"""
	convert normal math expression into RPN(Reverse Polish Notation) expression, which I learned in data structure
	:param expr: a normal math expression waiting to be converted
	:return: converted RPN expression
	"""
	notations=[]
	new_expr=[]
	for x in expr:
		if is_num(x):
			new_expr.append(x)
		else:
			# Handle ";", pop all the rest in the stack into new expression
			if x == ';':
				while len(notations)!=0:
					if notations[-1]!='(':
						new_expr.append(notations.pop())
					else:
						raise SyntaxError('Missing bracket')
			# Handle "(", put it into stack
			elif x == '(':
				notations.append(x)
			# Handle ")", pop all operators into new expression until a "(" found
			elif x == ')':
				while len(notations) > 0 and notations[-1] != "(":
					new_expr.append(notations.pop())
				if len(notations) > 0 and notations[-1] == '(':
					notations.pop()
				else:
					raise SyntaxError('Missing bracket')
			# Handel "*" or "/", put it into stack and do nothing, since they have highest priority
			elif x == '*' or x == '/':
				while len(notations) > 0 and get_priority(notations[-1])>=3 and notations[-1]!='(':
					new_expr.append(notations.pop())
				notations.append(x)
			# Handle "+" or "-", first put all higher priority operators into new expression, then put itself into new expression
			elif x == '+' or x == '-':
				while len(notations) > 0 and get_priority(notations[-1])>=2 and notations[-1]!='(':
					new_expr.append(notations.pop())
				notations.append(x)
			# Handel "**", put it into stack, waiting for next different operator being added to pop it out
			elif x == '**':
				notations.append(x)
			else:
				raise SyntaxError('Unrecognized operator found')
	#print(new_expr)
	return new_expr


def RPN_to_result(expr):
	"""
	Use RPN expression to calculate result
	:param expr: RPN expression
	:return: result of the expression, a single number
	"""
	numbers = []
	for x in expr:
		if is_num(x):
			numbers.append(int(x))
		else:
			b=numbers.pop()
			a=numbers.pop()
			if x == '+':
				numbers.append(a + b)
			if x == '-':
				numbers.append(a - b)
			if x == '*':
				numbers.append(a * b)
			if x == '/':
				numbers.append(a / b)
			if x == '**':
				numbers.append(a ** b)
	if len(numbers) == 1:
		return numbers[0]
	else:
		raise SyntaxError("Too less operators")


def is_num(expr):
	try:
		a = int(expr)
		return True
	except:
		return False

if __name__ == "__main__":
	print ( eval_infix("15 ") )
	print ( eval_infix( "2 + 3 " ) )
	print ( eval_infix( " 2 * 3 + 1  " ) )
	print ( eval_infix( " 2 + 3 * 1" ) )
	print ( eval_infix( " 3 ** 2" ))
	print ( eval_infix( " 3 ** 2 ** 2 / ( 3 + 6 )" ))