from Homework.peekable import Peekable, peek
from Homework.newsplit import new_split_iter
from random import randint


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


def to_postfix(expr):
	return postfix_sum(Peekable(new_split_iter(expr)))


def postfix_sum(expr):
	"""
	convert normal math expression into postfix expression
	:param expr: a normal math wexpression waiting to be converted
	:return: converted postfix expression
	"""
	operator_stack = []
	for x in expr:
		if is_number(x):
			yield x
		else:
			# Handle ";", pop all the rest in the stack into new expression
			if x == ';':
				while len(operator_stack) != 0:
					if operator_stack[-1] != '(':
						yield operator_stack.pop()
					else:
						raise SyntaxError('Missing bracket')
			# Handle "(", put it into stack
			elif x == '(':
				operator_stack.append(x)
			# Handle ")", pop all operators into new expression until a "(" found
			elif x == ')':
				while len(operator_stack) > 0 and operator_stack[-1] != "(":
					yield operator_stack.pop()
				if len(operator_stack) > 0 and operator_stack[-1] == '(':
					operator_stack.pop()
				else:
					raise SyntaxError('Missing bracket')
			# Handel "*" or "/", put it into stack and do nothing, since they have highest priority
			elif x in '*/':
				while len(operator_stack) > 0 and operator_stack[-1] in "/**" and operator_stack[-1] != '(':
					yield operator_stack.pop()
				operator_stack.append(x)
			# Handle "+" or "-", first put all higher priority operators into new expression, then put itself into new expression
			elif x in '+-':
				while len(operator_stack) > 0 and operator_stack[-1] in "+-/**" and operator_stack[-1] != "(":
					yield operator_stack.pop()
				operator_stack.append(x)
			# Handel "**", put it into stack, waiting for next different operator being added to pop it out
			elif x == '**':
				operator_stack.append(x)
			else:
				raise SyntaxError('Unrecognized operator found:' + x)


operators = ["+", "-", "*", "/", "**"]
