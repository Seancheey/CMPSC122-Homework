def new_split_iter(expr):
	"""divide a character string into individual tokens, which need not be separated by spaces (but can be!)
	also, the results are returned in a manner similar to iterator instead of a new data structure
	"""
	expr = expr + ";"  # append new symbol to mark end of data, for simplicity
	pos = 0  # begin at first character position in the list
	operator_taken = True

	while expr[pos] != ";":  # repeat until the end of the input is found
		token = expr[pos]

		# Handle + - / and (
		if expr[pos + 1] == "=" and token in "<>!=":
			operator_taken = True
			yield token + expr[pos + 1]
		elif token in "+/(":
			operator_taken = True
			yield token
		# Handle "-" operator
		elif token == "-" and not operator_taken:
			operator_taken = True
			yield token
		# Handle "-" sign
		elif token == "-" and operator_taken:
			number = token
			allow_blank = True
			for i in range(pos + 1, len(expr)):
				if expr[i].isnumeric() or expr[i]==".":
					allow_blank = False
					number += expr[i]
				elif allow_blank:
					continue
				else:
					pos += i - 1 - pos
					break
			operator_taken = False
			yield number
		# Handle )
		elif token == ")":
			operator_taken = False
			yield token
		# Handle * and **
		elif token == "*":
			operator_taken = True
			if expr[pos + 1] == "*":
				yield "**"
				pos += 1
			else:
				yield token
		# Handle number
		elif token.isnumeric():
			number = token
			for i in range(pos + 1, len(expr)):
				if expr[i].isnumeric() or expr[i]==".":
					number += expr[i]
				else:
					pos += i - 1 - pos
					break
			operator_taken = False
			yield number
		# Handle other characters like blank space
		else:
			pass
		pos += 1
	yield ";"


if __name__ == "__main__":
	print(list(new_split_iter("3+   (4 * 5)")))
	print(list(new_split_iter("3+5--2*2/(-6**   34.5<=5   != 10)--5")))