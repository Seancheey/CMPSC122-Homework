# author Qiyi Shan
# date 3.16.2017

from abc import ABCMeta, abstractmethod
from Homework.vartree import VarTree, FuncBody
from Homework.newsplit import NegativeSign


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
	def evaluate(self, variables, functions):
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

	def evaluate(self, variables: VarTree, functions: VarTree):
		return variables.lookup(self._name)


class Value(ExprTree):
	"""A Value leaf"""
	__slots__ = '_value'

	def __init__(self, v):
		if type(v) == str:
			v = int(v)
		self._value = v

	def __iter__(self):
		yield self._value

	def postfix(self):
		yield self._value

	def evaluate(self, variables, functions: VarTree):
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
		yield from self._value1.postfix()
		yield from self._value2.postfix()
		yield self._operator

	def evaluate(self, variables, functions: VarTree):
		o = self._operator
		v1 = self._value1.evaluate(variables, functions)
		v2 = self._value2.evaluate(variables, functions)
		if o == '+':
			return v1 + v2
		elif o == '-':
			return v1 - v2
		elif o == '*':
			return v1 * v2
		elif o == '/':
			return v1 / v2
		elif o == '%':
			return v1 % v2
		elif o == '**':
			return v1 ** v2
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
		elif o == '!=':
			return v1 != v2
		elif o == 'and':
			return bool(v1) and bool(v2)
		elif o == 'or':
			return bool(v1) or bool(v2)
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
		yield self._expr.__str__()
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

	def evaluate(self, variables, functions: VarTree):
		if self._expr.evaluate(variables, functions):
			return self._true.evaluate(variables, functions)
		else:
			return self._false.evaluate(variables, functions)


class Nega(ExprTree):
	"""A Negative Operation leaf"""
	__slots__ = '_expr'

	def __init__(self, expr: ExprTree):
		self._expr = expr

	def __iter__(self):
		yield NegativeSign()
		yield self._expr.__iter__()

	def postfix(self):
		yield self._expr.__iter__()
		yield NegativeSign()

	def evaluate(self, variables, functions: VarTree):
		return -self._expr.evaluate(variables, functions)

	def __str__(self):
		return '( -%s )' % self._expr.__str__()


class Func(ExprTree):
	"""A Function Operation leaf"""
	__slots__ = '_name', '_args'

	def __init__(self, name, args: list):
		self._name = name
		self._args = args

	def __iter__(self):
		yield '('
		yield '%s(%s)' % (self._name, ','.join([str(x) for x in self._args]))
		yield ')'

	def postfix(self):
		yield '%s(%s)' % (self._name, ','.join(self._args.__iter__()))

	def evaluate(self, variables, functions: VarTree):
		body: FuncBody = functions.lookup(self._name)
		params = VarTree()
		for i, key in enumerate(body.args):
			params.assign(key, self._args[i].evaluate(variables, functions))
		return body.expr.evaluate(params, functions)
