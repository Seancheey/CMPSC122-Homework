from Homework.infixtoiter import to_postfix
from Homework.evalpostfix import eval_postfix


def test(expr):
	print(expr, '=', eval_postfix(to_postfix(expr)))


test("3+4")
test("3+2 ** 2")
test("3+(3- 1)**2")
test("3+(8 /4)**2**2/4")
test("3*4 / 4+4")