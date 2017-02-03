def new_split_iter(expr):
	"""divide a character string into individual tokens, which need not be separated by spaces (but can be!)
	also, the results are returned in a manner similar to iterator instead of a new data structure
	"""
	expr = expr + ";"  # append new symbol to mark end of data, for simplicity
	pos = 0  # begin at first character position in the list

	while expr[pos] != ";":  # repeat until the end of the input is found
		token = expr[pos]
		out = ""
		if token in "+-**/(<>!=":
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
			# Handle "-" sign
			i = pos + 1
			while expr[i] == " ":
				pos += 1
				i += 1
			if expr[i] == "-":
				pos += len(out)
				yield out
				i += 1
				while expr[i] == " ":
					pos += 1
					i += 1
				num = "-"
				while expr[i].isnumeric() or expr[i] == ".":
					num += expr[i]
					i += 1
				out = num
		# Handle )
		elif token == ")":
			out = ")"
		# Handle number
		elif token.isnumeric():
			num = token
			i = pos + 1
			while expr[i].isnumeric() or expr[i] == ".":
				num += expr[i]
				i += 1
			out = num
		# Handle other characters like blank space
		else:
			pos += 1
			continue
		pos += len(out)
		yield out

	yield ";"


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
	print(list(new_split_iter("3 wow 2")))
	print(list(new_split_iter("3.2 + that is good 2")))
