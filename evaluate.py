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


if __name__ == '__main__':
	print(evaluate('3+5'))
	print(evaluate('a = 5'))
	print(evaluate('a==5?1:2'))
	print(evaluate('1==2'))
	print(evaluate('deffn funca(x,y) = x*y'))
	print(evaluate('funca(2,3)'))
