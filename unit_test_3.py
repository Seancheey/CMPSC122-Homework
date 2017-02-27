from Homework.newsplit import new_split_iter
from Homework.evalpostfix import eval_postfix
from Homework.infixtoiter import to_postfix
from random import randint

operators = ["+", "-", "*", "/"]


# operators = ["+", "-", "*", "/", "**"]


def rand_num():
	return str(randint(1, 6)) if randint(1, 2) == 1 else str(randint(-6, -1))


def rand_space():
	return " " * randint(0, 1)


def rand_operator():
	return operators[randint(0, len(operators) - 1)]


def genexpr(_len):
	s = ""
	curent_len = 0
	while curent_len < _len - 1:
		s += (rand_num() if randint(0, 5) != 0 else "(" + rand_space() + genexpr(
			2) + rand_space() + ")") + rand_space() + rand_operator() + rand_space()
		curent_len += 1
	s += rand_num()
	return s


def test(_expr):
	try:
		if eval_infix(_expr) == eval(_expr):
			print('Correct')
		else:
			print(list(new_split_iter(_expr)))
			print('Wrong ', str(_expr), '=', eval_infix(_expr), 'should be', eval(_expr))
	except ValueError:
		print('!!get value error', list(new_split_iter(_expr)))
	except ZeroDivisionError:
		print('zero division error')


for i in range(20):
	expr = genexpr(3)
	test(expr)
