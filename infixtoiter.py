# author Qiyi Shan
# date 2.27.2017
from Homework.peekable import Peekable
from Homework.newsplit import new_split_iter
from Homework.linkedlist import LinkedList


def to_postfix(expr):
	return postfix_sum(Peekable(new_split_iter(expr)))


def priority(operator):
	if operator in '+-':
		return 1
	elif operator in '*/%':
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


def postfix_sum(expr_iter):
	# make sure the type of parameter is Iterator
	if type(expr_iter) == str:
		expr_iter = list(new_split_iter(expr_iter))
	operator_list = LinkedList()
	for item in expr_iter:
		if item.isnumeric() or item[1:].isnumeric() and item[0] == '-' or item.isalpha():
			yield item
		else:
			if item == ';':
				while len(operator_list) != 0:
					yield operator_list.pop()
			elif item == ')':
				while operator_list.top() != '(':
					yield operator_list.pop()
				operator_list.pop()  # remove "("
			else:
				if item != '**' and item != '=' and item != '(':
					while len(operator_list) > 0 and operator_list.top() != '(' and priority(
							operator_list.top()) >= priority(
						item):
						yield operator_list.pop()
				operator_list.push(item)


if __name__ == '__main__':
	print(list(to_postfix('4 - (1 - 4) ** 1')))
	print(list(to_postfix('3*(1 - 4 ) ** 1')))
