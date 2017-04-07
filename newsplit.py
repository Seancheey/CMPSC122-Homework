# author Qiyi Shan
# date created 1.19.2017
# date modified 3.16.2017

from abc import ABCMeta


class Neg_meta(ABCMeta):
	def __repr__(self):
		return '-'

	def __len__(self):
		return 1

	def __iter__(self):
		yield NegativeSign

	def split(cls, sep=None, maxsplit=-1):
		return NegativeSign


class NegativeSign(metaclass=Neg_meta):
	pass


def new_split_iter(expr):
	if expr[-1] != ';':
		expr += ";"
	pos = 0  # begin at first character position in the list
	neg_sign_possible = True
	while expr[pos] != ";":  # repeat until the end of the input is found
		token = expr[pos]
		out = ""
		if neg_sign_possible and token == '-':
			neg_sign_possible = False
			out = NegativeSign
		elif token.isalpha():
			neg_sign_possible = False
			out = get_variable(expr, pos)
		# Handle number
		elif token.isnumeric():
			neg_sign_possible = False
			out = get_number(expr, pos)
		elif token in "+-**/(<>!==?:%":
			neg_sign_possible = True
			# Handle <= >= != ==
			if expr[pos + 1] == "=" and token in "<>!=":
				out = token + expr[pos + 1]
			# Handle **
			elif expr[pos:pos + 2] == "**":
				out = "**"
			# Handle other operators
			elif token in "+-/(=?:<>%*":
				out = token
			else:
				raise ValueError(token + " is not correct")
		elif token == ")":
			neg_sign_possible = False
			out = ")"
		# Handle other characters like blank space
		else:
			pos += 1
			continue
		pos += len(out)
		yield out

	yield ";"


def get_variable(expr, pos):
	if expr[pos].isalpha():
		v = expr[pos]
		while pos + 1 < len(expr) and expr[pos + 1].isalpha():
			pos += 1
			v += expr[pos]
		return v
	else:
		raise ValueError("get_variable(expr, pos) expects to take a variable but get", expr[pos])


def get_number(expr, pos):
	num = ''
	if expr[pos] == '-':
		num += '-'
		pos += 1
	if expr[pos].isnumeric():
		num += expr[pos]
		pos += 1
		while expr[pos].isnumeric() or expr[pos] == ".":
			num += expr[pos]
			pos += 1
	else:
		raise ValueError("get_number(expr, pos) expects to take a number but get", expr[pos])
	return num


if __name__ == "__main__":
	print(list(new_split_iter("1+2--3*4/5%6**7=6==5!=4<6>(8<=9>=10?3:10) and 5 or 6")))
	print(list(new_split_iter("deffn gcf(a,b) = (rem = a%b) == 0 ? b : gcf(b,rem)")))
