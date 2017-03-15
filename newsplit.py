# author Qiyi Shan
# date created 1.19.2017
# date modified 3.15.2017


def new_split_iter(expr):
	if expr[-1] != ';':
		expr += ";"
	pos = 0  # begin at first character position in the list
	neg_sign_possible = True
	while expr[pos] != ";":  # repeat until the end of the input is found
		token = expr[pos]
		out = ""
		if neg_sign_possible and token == '-' and expr[pos + 1].isnumeric():
			out = get_number(expr, pos)
			neg_sign_possible = False
		elif token.isalpha():
			out = get_variable(expr, pos)
			neg_sign_possible = False
		elif token in "+-**/(<>!==?:%":
			neg_sign_possible = True
			# Handle <= >= != ==
			if expr[pos + 1] == "=" and token in "<>!=":
				out = token + expr[pos + 1]
			# Handle + - / (
			elif token in "+-/(=?:<>%":
				out = token
			# Handle * and **
			elif token == "*":
				if expr[pos + 1] == "*":
					out = "**"
				else:
					out = "*"
		else:
			# Handle )
			if token == ")":
				out = ")"
			# Handle number
			elif token.isnumeric():
				neg_sign_possible = False
				out = get_number(expr, pos)
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
	print(list(new_split_iter("3   !=   2")))
	print(list(new_split_iter("a + 5-6+beta")))
	print(list(new_split_iter("1 = 4?33:3334")))
	print(list(new_split_iter("1 + 0 ? 0 +3 : 5")))
	print(list(new_split_iter("1+2-3*4/5%6**7=6==5!=4<6>(8<=9>=10?3:10) and 5 or 6")))
