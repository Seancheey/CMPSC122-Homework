# author Qiyi Shan
# date 1.19.2017

def eval_infix_sum(expr, pos):
	"""
	evaluate a sum expression (zero or more additions and subtractions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numerical answer and the position pointer
	"""
	ans, pos = eval_infix_product(expr, pos)
	while expr[pos] not in ');':
		if expr[pos] == '+':
			a, pos = eval_infix_product(expr, pos + 1)
			ans += a
		elif expr[pos] == '-':
			a, pos = eval_infix_product(expr, pos + 1)
			ans -= a
	return ans, pos


def eval_infix_product(expr, pos):
	"""
	evaluate a product expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	ans, pos = eval_infix_exponent(expr, pos)
	while expr[pos] not in '+-);':
		if expr[pos] == '*':
			a, pos = eval_infix_exponent(expr, pos + 1)
			ans *= a
		elif expr[pos] == '/':
			a, pos = eval_infix_exponent(expr, pos + 1)
			ans /= a
	return ans, pos


def eval_infix_exponent(expr, pos):
	"""
	evaluate a exponential expression (zero or more multiplications/divisions)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	ans, pos = eval_infix_factor(expr, pos)
	while expr[pos] not in '*/+-);':
		if expr[pos] == '**':
			a, pos = eval_infix_exponent(expr, pos + 1)
			ans **= a
		else:
			return eval_infix_factor(expr, pos)
	return ans, pos


def eval_infix_factor(expr, pos):
	"""
	evaluate a factor (number or parenthesized sub-expression)
	:param expr: expression in a list
	:param pos: current list pointer
	:return: numberical answer and the position pointer
	"""
	if expr[pos] == '(':
		ans, pos = eval_infix_sum(expr, pos + 1)
		return ans, pos + 1
	else:
		return int(expr[pos]), pos + 1  # convert string to int, and move past


def eval_infix_list(expr):
	"""
	evaluate an expression represented as a list of strings
	"""
	ans, _ = eval_infix_sum(expr, 0)  # start subscript at 0, then forget it
	return ans


def eval_infix(expr):
	"""
	evaluate an expression represented as a single space-separated string
	"""
	return eval_infix_list(expr.split() + [";"])  # make a list, and append semicolon


if __name__ == "__main__":
	print(eval_infix("1 + 2"))
	print(eval_infix("3 * 5"))
	print(eval_infix("2 ** 3"))
	print(eval_infix("1 + 2 * 3"))
	print(eval_infix("2 * 3 + 1"))
	print(eval_infix("2 * ( 3 + 1 )"))
	print(eval_infix("( 3 + 1 ) * 2"))
	print(eval_infix("2 + 2 ** 3 ** 2"))
	print(eval_infix("2 + ( 2 ** 3 ) ** 2"))