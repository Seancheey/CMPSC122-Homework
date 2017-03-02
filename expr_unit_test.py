from Homework.evalpostfix import eval_postfix
from Homework.infixtoiter import to_postfix
from random import randint


class ExprUnitTest:
	operators = []
	num_range = ()
	tested_expr = ""

	def __init__(self, operators=["+", "-", "*", "/", '**'], num_range=(-5, 5)):
		self.operators = operators
		self.num_range = num_range

	def rand_num(self):
		return str(randint(1, self.num_range[1])) if randint(1, 2) == 1 else str(randint(self.num_range[0], -1))

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

	def test(self, test_func, correct_output, wrong_output):
		try:
			self.tested_expr = self.genexpr(3)
			cor = eval(self.tested_expr)
			tes = test_func(self.tested_expr)
			if cor == tes:
				print(correct_output)
			else:
				print(wrong_output)
		except ValueError:
			print('!!get value error')
		except ZeroDivisionError:
			print('zero division error')


def test_eval(expr):
	return eval_postfix(to_postfix(expr))


def main():
	a = ExprUnitTest()
	for i in range(20):
		a.test(test_eval, "Correct", "Wrong: "+a.tested_expr)


if __name__ == '__main__':
	main()
