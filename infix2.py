# author Qiyi Shan
# date 1.19.2017
from Homework.peekable import Peekable
from Homework.newsplit import new_split_iter


def eval_infix_sum(expr):
	"""
	evaluate a sum expression (zero or more additions and subtractions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numerical answer and the position pointer
	"""
	ans = eval_infix_product(expr)
	oper = expr.peek()
	while oper in '+-':
		expr.__next__()
		other = eval_infix_product(expr)
		if oper == '+':
			ans += other
		elif oper == '-':
			ans -= other
		oper = expr.peek()
	return ans


def eval_infix_product(expr):
	"""
	evaluate a product expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	ans = eval_infix_exponent(expr)
	oper = expr.peek()
	while expr.peek() in "*/%":
		expr.__next__()
		other = eval_infix_exponent(expr)
		if oper == '*':
			ans *= other
		elif oper == '/':
			ans /= other
		oper = expr.peek()
	return ans


def eval_infix_exponent(expr):
	"""
	evaluate a exponential expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	ans = eval_infix_factor(expr)
	oper = expr.peek()
	while expr.peek() == "**":
		expr.__next__()
		other = eval_infix_exponent(expr)
		if oper == '**':
			ans **= other
		else:
			return eval_infix_factor(expr)
		oper = expr.peek()
	return ans


def eval_infix_factor(expr):
	"""
	evaluate a factor (number or parenthesized sub-expression)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	if expr.peek() == '(':
		expr.__next__()
		ans = eval_infix_sum(expr)
	else:
		ans = int(expr.peek())
	expr.__next__()
	return ans  # convert string to int, and move past


def eval_infix_iter(iterator):
	"""evaluate an expression, given an iterator to its tokens"""
	return eval_infix_sum(Peekable(iterator))


def eval_infix(expr):
	"""accept a character string, split it into tokens, then evaluate"""
	return eval_infix_iter(new_split_iter(expr))


if __name__ == "__main__":
	print(eval_infix("2 + ( 2 * 3 ) + 4"))
	print(eval_infix("0+(2*5)+2"))
