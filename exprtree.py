from abc import ABCMeta, abstractmethod
from Homework.vartree import VarTree


class ExprTree(metaclass=ABCMeta):
	"""Abstract class for expression"""

	def __str__(self):
		return ' '.join(str(x) for x in iter(self))

	#   All of the derived class mus implement these functions
	@abstractmethod
	def __iter__(self):
		"""an inorder iterator for this tree node, for display"""
		pass

	@abstractmethod
	def postfix(self):
		"""a post-order iterator to create a postfix expression"""
		pass

	@abstractmethod
	def evaluate(self, variables):
		"""evaluate using the existing variables"""
		pass


class Var(ExprTree):
	"""A variable leaf"""
	__slots__ = '_name'

	def __init__(self, n):
		self._name = n

	def __iter__(self):
		yield self._name

	def postfix(self):
		yield self._name

	def evaluate(self, variables: VarTree):
		return variables.lookup(self._name)


class Value(ExprTree):
	"""A Value leaf"""
	__slots__ = '_value'

	def __init__(self, v):
		self._value = v

	def __iter__(self):
		yield self._value

	def postfix(self):
		yield self._value

	def evaluate(self, variables):
		return self._value


class Oper(ExprTree):
	"""A Operation leaf"""
	__slots__ = '_value1', '_value2', '_operator'

	def __init__(self, v1: ExprTree, o: str, v2: ExprTree):
		self._value1 = v1
		self._operator = o
		self._value2 = v2

	def __iter__(self):
		yield '('
		yield self._value1.__str__()
		yield self._operator
		yield self._value2.__str__()
		yield ')'

	def postfix(self):
		for item in self._value1.postfix():
			yield item
		for item in self._value2.postfix():
			yield item
		yield self._operator

	def evaluate(self, variables):
		o = self._operator
		v1 = self._value1.evaluate(variables)
		v2 = self._value2.evaluate(variables)
		if o == '+':
			return v1 + v2
		elif o == '-':
			return v1 - v2
		elif o == '*':
			return v1 * v2
		elif o == '/':
			return v1 / v2
		elif o == '**':
			return v1 ** v2
		elif o == '%':
			return v1 % v2
		elif o == '=':
			variables.assign(key=self._value1._name, value=v2)
			return v2
		elif o == '>':
			return v1 > v2
		elif o == '<':
			return v1 < v2
		elif o == '>=':
			return v1 >= v2
		elif o == '<=':
			return v1 <= v2
		elif o == '==':
			return v1 == v2
		else:
			raise NotImplementedError(str(o) + " operation is not implemented")


class Cond(ExprTree):
	"""A Condition leaf"""
	__slots__ = '_expr', '_true', '_false'

	def __init__(self, expr: ExprTree, tv: ExprTree, fv: ExprTree):
		self._expr = expr
		self._true = tv
		self._false = fv

	def __iter__(self):
		yield '('
		yield self._expr
		yield '?'
		yield self._true
		yield ':'
		yield self._false
		yield ')'

	def postfix(self):
		yield self._true
		yield self._false
		yield ':'
		yield self._expr
		yield '?'

	def evaluate(self, variables):
		if self._expr.evaluate(variables):
			return self._true.evaluate(variables)
		else:
			return self._false.evaluate(variables)


if __name__ == '__main__':
	V = VarTree()
	VA = Var("A")
	Sum = Oper(Value(2), '+', Value(3))
	A = Oper(VA, '=', Sum)
	print("Infix iteration: ", list(A))
	print("String version ", A)
	print("Postfix iteration: ", list(A.postfix()))
	print("Execution: ", A.evaluate(V))
	print("Afterwards, A = ", VA.evaluate(V))

	# If A == 5, return A+2 else return 3
	CondTest = Cond(Oper(VA, '==', Value(5)), Oper(VA, '+', Value(2)), Value(3))
	print(CondTest, '-->', CondTest.evaluate(V))
