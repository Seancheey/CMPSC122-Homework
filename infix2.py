# author Qiyi Shan
# date 1.22.2017

def eval_infix_sum(expr):
	"""
	evaluate a sum expression (zero or more additions and subtractions)
	:param expr: expression in a list
	:return: numerical answer
	"""


def eval_infix_product(expr):
	"""
	evaluate a product expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:return: numberical answer
	"""


def eval_infix_exponent(expr):
	"""
	evaluate a exponential expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:return: numberical answer
	"""

def eval_infix_factor(expr):
	"""
	evaluate a factor (number or parenthesized sub-expression)
	:param expr: expression in a list
	:return: numberical answer
	"""
	a = expr.__next__()
	if a == "(":
		return eval_infix_sum()
	else:
		return a


def eval_infix_iter(expr):
	return eval_infix_sum(expr)


def eval_infix(expr):
	"""
	evaluate an expression represented as a single space-separated string
	"""
	return eval_infix_iter(expr)  # make a list, and append semicolon


if __name__ == "__main__":
	print(eval_infix_iter(iter(["3",";"])))
