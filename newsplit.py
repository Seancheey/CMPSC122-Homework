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
		elif token in "+-**/(<>!=":
			neg_sign_possible = True
			# Handle + - / (
			if token in "+-/(":
				out = token
			# Handle <= >= != ==
			elif expr[pos + 1] == "=" and token in "<>!=":
				out = token + expr[pos + 1]
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
		raise ValueError("Cannot get a number")
	return num


if __name__ == "__main__":
	print(list(new_split_iter("3+ (4 *5)")))
	print(list(new_split_iter("3  +(4* 5)")))
	print(list(new_split_iter("3+ -2")))
	print(list(new_split_iter("3+-2")))
	print(list(new_split_iter("3 + -2")))
	print(list(new_split_iter("3+-   2")))
	print(list(new_split_iter("3- -2")))
	print(list(new_split_iter("3** 2")))
	print(list(new_split_iter("3>=2")))
	print(list(new_split_iter("3   !=   2")))
