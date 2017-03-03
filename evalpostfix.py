# author: Qiyi Shan
# Date: 1/11/2017
from Homework.linkedlist import LinkedList


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


def eval_postfix(expr):
	"""
	Use RPN expression to calculate result
	:param expr: RPN expression
	:return: result of the expression, a single number
	"""
	number_stack = LinkedList()
	for i in expr:
		if is_number(i):
			number_stack.push(int(i))
		else:
			b = number_stack.pop()
			a = number_stack.pop()
			if i == '+':
				number_stack.push(a + b)
			if i == '-':
				number_stack.push(a - b)
			if i == '*':
				number_stack.push(a * b)
			if i == '/':
				number_stack.push(a / b)
			if i == '**':
				number_stack.push(a ** b)
	if len(number_stack) == 1:
		return number_stack._head._value
	else:
		raise SyntaxError("Too less operators")