# author Qiyi Shan
# Date 3.16.2017

from Homework.exprtree import Var, Cond, Oper, Value, Nega
from Homework.newsplit import new_split_iter, NegativeSign

__priority_list = ['=', 'and', 'or', '?', '< > <= >= == !=', '+ -', '* / %', NegativeSign, '**']
__to_right_direction = {'=': False, 'and': True, 'or': True, '?': False, '< > <= >= == !=': True, '+ -': True,
						'* / %': True, NegativeSign: True, '**': False}


def to_expr_tree(expr):
	if type(expr) == str:
		expr = new_split_iter(expr)
	expr = list(expr)[0:-1]
	return __to_tree(expr)


def __to_tree(expr):
	"""Recursively convert expression to tree"""
	if len(expr) == 1:
		if expr[0].isnumeric():
			return Value(expr[0])
		else:
			return Var(expr[0])

	for operator in __priority_list:
		index_order = range(len(expr) - 1, -1, -1) if __to_right_direction[operator] else range(len(expr))
		for i in index_order:
			if expr[i] in operator.split(' ') and not __in_brackets(expr, i):
				if expr[i] == '?':
					colon_pos = expr.index(':')
					return Cond(__to_tree(expr[:i]), __to_tree(expr[i + 1:colon_pos]), __to_tree(expr[colon_pos + 1:]))
				elif expr[i] is NegativeSign:
					return Nega(__to_tree(expr[i + 1:]))
				else:
					return Oper(__to_tree(expr[:i]), expr[i], __to_tree(expr[i + 1:]))

	if expr[0] == '(':
		return __to_tree(expr[1:-1])

	raise NotImplementedError(str(expr) + " not implemented")


def __in_brackets(expr, pos):
	"""Test if an operator is included in brackets"""
	return expr[:pos].count('(') > expr[:pos].count(')')


if __name__ == "__main__":
	print(to_expr_tree("5"))
	print(to_expr_tree('-5**9'))
	print(to_expr_tree("A = 5"))
	print(to_expr_tree("A = 2 + 3 * B - xyz"))
	print(to_expr_tree("x < 0 ? 0 - x : x"))
	print(to_expr_tree("3* (5+4 /3) + 6"))
	print(to_expr_tree('1 and 1'))
	print(to_expr_tree('3 == 4'))
