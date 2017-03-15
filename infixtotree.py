from Homework.exprtree import Var, Cond, Oper, Value
from Homework.newsplit import new_split_iter

__oper_priority_list = ['=', '?', '<><=>=', '+-', '*/%', '**']
__to_right_direction = {'=': False, '?': False, '<><=>=': True, '+-': True, '*/%': True, '**': False}


def to_expr_tree(expr):
	if type(expr) == str:
		expr = new_split_iter(expr)
	expr = list(expr)[0:-1]
	return __to_tree(expr)


def __to_tree(expr):
	if len(expr) == 1:
		if expr[0].isnumeric():
			return Value(expr[0])
		else:
			return Var(expr[0])

	for operator in __oper_priority_list:
		if __to_right_direction[operator]:
			index_order = range(len(expr) - 1, -1, -1)
		else:
			index_order = range(len(expr))
		for i in index_order:
			if expr[i] in operator and not __in_brackets(expr, i):
				if expr[i] == '?':
					for j in range(i + 1, len(expr)):
						if expr[j] == ':':
							return Cond(__to_tree(expr[:i]), __to_tree(expr[i + 1:j]), __to_tree(expr[j + 1:]))
				else:
					return Oper(__to_tree(expr[:i]), expr[i], __to_tree(expr[i + 1:]))

	if expr[0] == '(':
		for i in range(len(expr)):
			if i == ')' and i == len(expr) - 1:
				return __to_tree(expr[1:i - 1])

	raise NotImplementedError(str(expr) + " not implemented")


def __in_brackets(expr, pos):
	inbracket = False
	for i in range(len(expr)):
		if i == pos:
			return inbracket
		if expr[i] == '(':
			inbracket = True
		elif expr[i] == ')':
			inbracket = False
	raise IndexError(str(pos) + " Out of Bound")


if __name__ == "__main__":
	print(to_expr_tree("5"))
	print(to_expr_tree("A = 5"))
	print(to_expr_tree("A = 2 + 3 * B - xyz"))
	print(to_expr_tree("x < 0 ? 0 - x : x"))
