from abc import abstractmethod, ABCMeta
from Homework.vartree import Reference


class Instruction(metaclass=ABCMeta):
	"""Simple instructions representative of a RISC machine

	These instructions are mostly immutable -- once constructed,
	they will not be changed -- only displayed and executed
	"""

	def __init__(self, t):  # default constructor
		self._temp = t  # every instruction has a register

	def get_temp(self):  # which holds its answer
		return self._temp

	@abstractmethod
	def execute(self, temps, stack, pc, sp):
		pass


class Print(Instruction):
	"""A simple non-RISC output function to display a value"""

	def __str__(self):
		return "print T" + str(self._temp)

	def execute(self, temps, stack, pc, sp):
		print(temps[self._temp])


class Init(Instruction):
	"""Initialize a temporary register to a value"""
	__slots__ = '_val'

	def __init__(self, t, val):
		super().__init__(t)
		self._val = val

	def __str__(self):
		return "T%d = %s" % (self._temp, str(self._val))

	def execute(self, temps, stack, pc, sp):
		temps[self._temp] = self._val


class Load(Instruction):
	"""Load a temporary register from a variable"""
	__slots__ = '_stack'

	def __init__(self, t, s):
		super().__init__(t)
		self._stack = s

	def __str__(self):
		return "T%d = stack[%d]" % (self._temp, self._stack)

	def execute(self, temps, stack, pc, sp):
		if type(stack[self._stack]) is Reference:
			temps[self.get_temp()] = temps[stack[self._stack]]
		temps[self._temp] = stack[self._stack]


class Store(Instruction):
	"""Store a temporary register into a variable"""
	__slots__ = '_stack'

	def __init__(self, t, s):
		super().__init__(t)
		self._stack = s

	def __str__(self):
		return "stack[%d] = T%d" % (self._stack, self._temp)

	def execute(self, temps, stack, pc, sp):
		stack[self._stack] = temps[self._temp]


class Comp(Instruction):
	"""Perform a computation using temporary registers"""
	__slots__ = '_temp1', '_operator', '_temp2'

	def __init__(self, t, t1, operator, t2):
		super().__init__(t)
		self._temp1 = t1
		self._operator = operator
		self._temp2 = t2

	def __str__(self):
		return "T%d = T%d %s T%d" % (self._temp, self._temp1, self._operator, self._temp2)

	def execute(self, temps, stack, pc, sp):
		temps[self._temp] = eval(str(temps[self._temp1]) + self._operator + str(temps[self._temp2]))
