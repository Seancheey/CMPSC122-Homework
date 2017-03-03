from Homework.newsplit import new_split_iter


def priority(operator):
	if operator in '+-':
		return 1
	elif operator in '*/':
		return 2
	elif operator == '**':
		return 3
	elif operator == '(':
		return 4
	elif operator == ')':
		return 0
	elif operator == '=':
		return -1
	else:
		raise ValueError("%s not supported by priority function" % operator)


def to_postfix(expr_iter):
	# make sure the type of parameter is Iterator
	if type(expr_iter) == str:
		expr_iter = list(new_split_iter(expr_iter))

	operator_list = []
	for item in expr_iter:
		if item.isnumeric() or item[1:].isnumeric() and item[0] == '-' or item.isalpha():
			yield item
		else:
			if item == ';':
				operator_list.reverse()
				for op in operator_list:
					yield op
			elif item == '(':
				operator_list.append(item)
			elif item == ')':
				while operator_list[-1] != '(':
					yield operator_list.pop()
				operator_list.pop()
			else:
				if item != '**' and item != '=':
					while len(operator_list) > 0 and operator_list[-1] != '(' and priority(
							operator_list[-1]) >= priority(
						item):
						yield operator_list.pop()
				operator_list.append(item)
