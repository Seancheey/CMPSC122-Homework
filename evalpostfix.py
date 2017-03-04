# author: Qiyi Shan
# Date: 3.4.2017
from Homework.linkedlist import LinkedList
from Homework.vartree import VarTree


def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False


def eval_postfix(tree: VarTree, expr):
	number_stack = LinkedList()
	for item in expr:
		if is_number(item) or item.isalpha():  # item is a variable or number
			number_stack.push(int(item) if is_number(item) else item)
		else:  # item is an operator
			b_num = number_stack.pop()
			a_num = number_stack.pop()
			if type(b_num) is str:
				b_num = tree.lookup(b_num)
			if item == '=':
				if a_num.isnumeric():
					raise ValueError("Assign a value to a number")
				else:
					tree.assign(a_num, b_num)
					number_stack.push(tree.lookup(a_num))
			if type(a_num) is str:
				if tree.lookup(a_num) is not None:
					a_num = tree.lookup(a_num)
				else:
					raise ValueError("Can't find variable with name " + a_num)
			if item == '+':
				number_stack.push(a_num + b_num)
			elif item == '-':
				number_stack.push(a_num - b_num)
			elif item == '*':
				number_stack.push(a_num * b_num)
			elif item == '/':
				number_stack.push(a_num / b_num)
			elif item == '**':
				number_stack.push(a_num ** b_num)
	if len(number_stack) == 1:
		if type(number_stack._head._value) is str:
			return V.lookup(number_stack._head._value)
		return number_stack._head._value
	else:
		raise SyntaxError("Too less operators: " + str(number_stack))


if __name__ == '__main__':
	V = VarTree()
	print(eval_postfix(V, ['sean', '2', '=']))
	print(eval_postfix(V, ['new', 'sean', '3', '+', '=']))
	print(eval_postfix(V, ['new', '1', '+']))
	print(eval_postfix(V, ['new']))
