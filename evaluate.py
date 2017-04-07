from Homework.newsplit import new_split_iter
from Homework.infixtotree import to_expr_tree
from Homework.vartree import VarTree, FuncBody

__VarTree = VarTree()
__FuncTree = VarTree()
DEF_KEY = 'deffn'


def evaluate(expr):
	"""evaluate expression or definition"""
	# deffn square(x,y) = x*y
	if type(expr) is str:
		expr = list(new_split_iter(expr))
	if expr[0] == DEF_KEY:
		func_name = expr[1]
		func_args = expr[expr.index('(') + 1:expr.index(')')]
		func_body = expr[expr.index('=') + 1:]
		__FuncTree.assign(func_name, FuncBody(func_args, to_expr_tree(func_body)))
	else:
		return to_expr_tree(expr).evaluate(__VarTree, __FuncTree)


def input_mode():
	while True:
		inp = input()
		if inp is None or inp == '':
			break
		print(evaluate(inp))


if __name__ == '__main__':
	evaluate("deffn abs(x) = x>0?x:-x")
	print(evaluate('-1'))
	print(evaluate('abs(6)'))
	print(evaluate('abs(1*5)'))
	print(evaluate('abs(-9)'))
