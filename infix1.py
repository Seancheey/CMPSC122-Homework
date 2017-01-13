__operators__ = ['+', '-', '*', '/', '**']


def isoperator(str):
	for o in __operators__:
		if str == o:
			return True
	return False


def getpriority(operator):
	if operator == '+' or operator == '-':
		return 1
	elif operator == '*' or operator == '/':
		return 2
	elif operator == '(':
		return 3
	else:
		return 0


def doOperation(expr):
	if expr[1] == '+':
		return expr[0] + expr[2]
	elif expr[1] == '-':
		return expr[0] - expr[2]
	elif expr[1] == '*':
		return expr[0] * expr[2]
	elif expr[1] == '/':
		return expr[0] / expr[2]
	elif expr[1] == '**':
		return expr[0] ** expr[2]
	else:
		raise SyntaxError("Missing operator")
		return None


def eval_infix_sum(expr, pos):
	"""evaluate a sum expression (zero or more additions and subtractions)
	expr      Python string list           complete expression to be evaluated
	pos       integer                          subscript to current token
	"""
	ans = 0
	print(expr[pos])
	if expr[pos].isnumeric():
		if pos + 1 != len(expr):
			if isoperator(expr[pos + 1]):
				if pos + 3 < len(expr):
					if isoperator(expr[pos + 3]) and getpriority(expr[pos + 3]) <= 1:
						return doOperation(expr[pos:pos + 2]) + eval_infix_sum(expr, pos + 2)
					else:
						return 0, pos + 2
				else:
					if getpriority(expr[pos + 1]) == 1:
						return doOperation(expr[pos:pos + 2]), pos + 2
					else:
						return 0, pos + 2
			else:
				raise SyntaxError("two Numbers are put together")
		else:
			return 0
	else:
		return eval_infix_sum(expr,pos+1)
	return ans, pos  # return result and updated subscript


def eval_infix_product(expr, pos):
	"""evaluate a product expression (zero or more multiplications/divisions)
   """


# NOTE:   This must be extended to support parenthesized sub-expressions)

def eval_infix_factor(expr, pos):
	"""evaluate a factor (number or parenthesized sub-expression)
   """
	return int(expr[pos]), pos + 1  # convert string to int, and move past


#  the following functions are defined to supply a 'friendlier' interface to the clients,
# which will later also be used to provide some degree of implementation hiding.
def eval_infix_list(expr):
	"""evaluate an expression represented as a list of strings
	"""
	ans, discard = eval_infix_sum(expr, 0)  # start subscript at 0, then forget it
	return ans


def eval_infix(expr):
	"""evaluate an expression represented as a single space-separated string
	"""
	return eval_infix_list(expr.split() + [";"])  # make a list, and append semicolon


if __name__ == "__main__":
	print(eval_infix("15 "))
	print(eval_infix("2 + 3 "))
	print(eval_infix(" 2 * 3 + 1  "))
	print(eval_infix(" 2 + 3 * 1"))
	print(eval_infix(" 1 + ( 2 + 10 * 3 ) * 10 "))
