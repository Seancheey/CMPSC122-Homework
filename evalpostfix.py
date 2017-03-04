# author: Qiyi Shan
# Date: 1/11/2017
from Homework.linkedlist import LinkedList
from Homework.vartree import VarTree


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


def eval_postfix(V: VarTree, expr):
	"""
	Use RPN expression to calculate result
	:param expr: RPN expression
	:return: result of the expression, a single number
	"""
	number_stack = LinkedList()
	for i in expr:
		if is_number(i) or i.isalpha():
			number_stack.push(int(i) if is_number(i) else i)
		else:
			b = number_stack.pop()
			a = number_stack.pop()
			if i == '=':
				if a.isnumeric():
					raise ValueError("Assign a value to a number")
				else:
					V.assign(a, b)
					number_stack.push(V.lookup(a))
			if V.lookup(a) is not None:
				a = V.lookup(a)
			if i == '+':
				number_stack.push(a + b)
			elif i == '-':
				number_stack.push(a - b)
			elif i == '*':
				number_stack.push(a * b)
			elif i == '/':
				number_stack.push(a / b)
			elif i == '**':
				number_stack.push(a ** b)
	if len(number_stack) == 1:
		return number_stack._head._value
	else:
		raise SyntaxError("Too less operators")
