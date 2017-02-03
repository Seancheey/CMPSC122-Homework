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
	while expr.peek() not in ');':
		if expr.peek() == '+':
			expr.__next__()
			ans += eval_infix_product(expr)
		elif expr.peek() == '-':
			expr.__next__()
			ans -= eval_infix_product(expr)
	return ans


def eval_infix_product(expr):
	"""
	evaluate a product expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	ans = eval_infix_exponent(expr)
	while expr.peek() not in '+-);':
		if expr.peek() == '*':
			expr.__next__()
			ans *= eval_infix_exponent(expr)
		elif expr.peek() == '/':
			expr.__next__()
			ans /= eval_infix_exponent(expr)
	return ans


def eval_infix_exponent(expr):
	"""
	evaluate a exponential expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	ans = eval_infix_factor(expr)
	while expr.peek() not in '*/+-);':
		if expr.peek() == '**':
			expr.__next__()
			ans **= eval_infix_exponent(expr)
		else:
			return eval_infix_factor(expr)
	return ans


def eval_infix_factor(expr):
	"""
	evaluate a factor (number or parenthesized sub-expression)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	a = expr.__next__()
	if a == '(':
		ans = eval_infix_sum(expr)
		return ans
	else:
		return int(a)  # convert string to int, and move past


def eval_infix_iter(iterator):
	"""evaluate an expression, given an iterator to its tokens"""
	return eval_infix_sum(Peekable(iterator))


def eval_infix(expr):
	"""accept a character string, split it into tokens, then evaluate"""
	return eval_infix_iter(new_split_iter(expr))


if __name__ == "__main__":
	print(eval_infix("1+ 2"))
	print(eval_infix("3 * 5"))
	print(eval_infix("2 ** 3"))
	print(eval_infix("1 + 2 * 3"))
	print(eval_infix("2 * 3 + 1"))
	print(eval_infix("2 * ( 3 + 1 )"))
	print(eval_infix("( 3 + 1 ) * 2"))
	print(eval_infix("2 +2 ** 3 ** 2"))
	print(eval_infix("2 + ( 2 ** 3 ) ** 2"))