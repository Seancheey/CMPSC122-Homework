# author: Qiyi Shan
# Date: 1/11/2017
from Homework.infixtoiter import to_postfix


def eval_infix(expr):
	return eval_postfix(to_postfix(expr.split() + [";"]))


def eval_postfix(expr):
	"""
	Use RPN expression to calculate result
	:param expr: RPN expression
	:return: result of the expression, a single number
	"""
	numbers = []
	for x in expr:
		if is_num(x):
			numbers.append(int(x))
		else:
			b = numbers.pop()
			a = numbers.pop()
			if x == '+':
				numbers.append(a + b)
			if x == '-':
				numbers.append(a - b)
			if x == '*':
				numbers.append(a * b)
			if x == '/':
				numbers.append(a / b)
			if x == '**':
				numbers.append(a ** b)
	if len(numbers) == 1:
		return numbers[0]
	else:
		raise SyntaxError("Too less operators")


def is_num(expr):
	try:
		a = int(expr)
		return True
	except:
		return False


if __name__ == "__main__":
	print(eval_infix("15 "))
	print(eval_infix("2 + 3 "))
	print(eval_infix(" 2 * 3 + 1  "))
	print(eval_infix(" 2 + 3 * 1"))
	print(eval_infix(" 3 ** 2"))
	print(eval_infix(" 3 ** 2 ** 2 / ( 3 + 6 )"))
