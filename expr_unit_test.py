from Homework.evalpostfix import eval_postfix
from random import randint
from Homework.infixtopostfix import to_postfix
from Homework.vartree import VarTree


class ExprUnitTest:
	operators = []
	num_range = range(-5, 5)
	tested_expr = ""

	def __init__(self, operators=["+", "-", "*", "/", '**'], num_range=range(-5, 5)):
		self.operators = operators
		self.num_range = num_range

	def rand_num(self):
		return str(list(self.num_range)[randint(0, len(self.num_range) - 1)])

	@staticmethod
	def __rand_space():
		return " " * randint(0, 1)

	def __rand_operator(self):
		return self.operators[randint(0, len(self.operators) - 1)]

	def genexpr(self, _len):
		s = ""
		curent_len = 0
		while curent_len < _len - 1:
			s += (self.rand_num() if randint(0, 5) != 0 else "(" + self.__rand_space() + self.genexpr(
				2) + self.__rand_space() + ")") + self.__rand_space() + self.__rand_operator() + self.__rand_space()
			curent_len += 1
		s += self.rand_num()
		return s

	def test(self, test_func, compare_func=eval):
		try:
			self.tested_expr = self.genexpr(3)
			cor = compare_func(self.tested_expr)
			tes = test_func(self.tested_expr)
			if cor == tes:
				return True
			else:
				return False
		except ValueError:
			print('!!get value error')
		except ZeroDivisionError:
			print('zero division error')
		return True


V = VarTree()


def test_eval(expr):
	a = eval_postfix(V, to_postfix(expr))
	return a


def main():
	a = ExprUnitTest()
	for i in range(200):
		result_correct = a.test(test_eval)
		print("Correct" if result_correct else "Wrong")
		if not result_correct:
			print(a.tested_expr)
			print(test_eval(a.tested_expr))
			print(eval(a.tested_expr))


if __name__ == '__main__':
	main()
