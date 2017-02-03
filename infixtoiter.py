from Homework.peekable import Peekable, peek
from Homework.newsplit import new_split_iter
from Homework.linkedlist import LinkedList

def is_num(expr):
	try:
		a = int(expr)
		return True
	except:
		return False

def to_postfix( expr ):
	return postfix_sum(Peekable(new_split_iter(expr)))

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


def postfix_sum(expr):
	"""
	convert normal math expression into postfix expression
	:param expr: a normal math wexpression waiting to be converted
	:return: converted RPN expression
	"""
	notations = []
	new_expr = []
	for x in expr:
		if is_num(x):
			new_expr.append(x)
		else:
			# Handle ";", pop all the rest in the stack into new expression
			if x == ';':
				while len(notations) != 0:
					if notations[-1] != '(':
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
			elif x in '*/':
				while len(notations) > 0 and get_priority(notations[-1]) >= 3 and notations[-1] != '(':
					new_expr.append(notations.pop())
				notations.append(x)
			# Handle "+" or "-", first put all higher priority operators into new expression, then put itself into new expression
			elif x in '+-':
				while len(notations) > 0 and get_priority(notations[-1]) >= 2 and notations[-1] != '(':
					new_expr.append(notations.pop())
				notations.append(x)
			# Handel "**", put it into stack, waiting for next different operator being added to pop it out
			elif x == '**':
				notations.append(x)
			else:
				raise SyntaxError('Unrecognized operator found')
	# print(new_expr)
	return new_expr


