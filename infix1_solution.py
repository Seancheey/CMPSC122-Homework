"""Evaluating an expression given as a list of tokens
This solution is intended for the benefit of the students
taking CMPSC 122 at the Pennsylvania State University
during the Spring Semester of 2017, and is not intended
for any other audience, or to distributed outside of the course.

Roger Christman, Pennsylvania State University
"""


def eval_infix_sum(expr, pos):
	"""evaluate a sum expression (zero or more additions and subtractions)
	  expr      Python string list  complete expression to be evaluated
	  pos       integer             subscript to current token
	since pos is an immutable integer, its updated value must be returned
	"""
	ans, pos = eval_infix_product(expr, pos)  # get one term
	oper = expr[pos]
	while oper == '+' or oper == '-':  # if there is another
		other, pos = eval_infix_product(expr, pos + 1)  # obtain it
		if oper == '+':
			ans = ans + other  # and compute
		else:
			ans = ans - other
		oper = expr[pos]
	return ans, pos


def eval_infix_product(expr, pos):
	"""evaluate a product expression (zero or more multiplications/divisions)
	  expr      Python string list  complete expression to be evaluated
	  pos       integer             subscript to current token
	since potes is an immutable integer, its updated value must be returned
	"""
	ans, pos = eval_infix_factor(expr, pos)  # get one factor
	oper = expr[pos]
	while oper == '*' or oper == '/' or oper == '%':  # if there is another
		other, pos = eval_infix_factor(expr, pos + 1)  # obtain it
		if oper == '*':
			ans = ans * other  # and compute
		elif oper == '/':
			ans = ans // other  # integer division
		else:
			ans = ans % other
		oper = expr[pos]
	return ans, pos


def eval_infix_factor(expr, pos):
	"""evaluate a factor expression (number or parenthesized expression)
	  expr      Python string list  complete expression to be evaluated
	  pos       integer             subscript to current token
	"""
	if expr[pos] == '(':  # parenthesized
		ans, pos = eval_infix_sum(expr, pos + 1)
	else:
		ans = int(expr[pos])
	return ans, pos + 1


def eval_infix_list(expr):
	"""evaluate an expression represented as a python list"""
	ans, discard = eval_infix_sum(expr, 0)
	return ans


def eval_infix(expr):
	"""evaluate an expression represented as a character string"""
	return eval_infix_list(expr.split() + [";"])


#   just a few simple tests (not what the TA uses)
if __name__ == "__main__":
	print(eval_infix("15 "))
	print(eval_infix("2 + 3 "))
	print(eval_infix(" 2 * 3 + 4  "))
	print(eval_infix(" 2 + 3 * 4"))
	print(eval_infix(" 1 + ( 2 + 10 * 3 ) * 10 "))
