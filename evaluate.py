from Homework.newsplit import new_split_iter
from Homework.infixtotree import to_expr_tree
from Homework.vartree import VarTree

__VarTree = VarTree()


def evaluate(expr):
	if type(expr) is str:
		expr = list(new_split_iter(expr))
	if expr[0] == 'deffn':
		pass
	else:
		return to_expr_tree(expr).evaluate(__VarTree)


if __name__ == '__main__':
	print(evaluate('3+5'))
	print(evaluate('a = 5'))
	print(evaluate('a==5?1:2'))
	print(evaluate('1==2'))
