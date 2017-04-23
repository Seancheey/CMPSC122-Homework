class VarTree:
	class Node:
		__slots__ = ("_right", "_left", "_value", "_pos", "key")

		def __init__(self, left, key, val, right, pos):
			self._left = left
			self.key = key
			self._value = val
			self._right = right
			self._pos = pos

		@property
		def value(self):
			return self._value

		@property
		def right(self):
			return self._right

		@property
		def left(self):
			return self._left

		@property
		def position(self):
			return self._pos

	__slots__ = "_root"

	def __init__(self):
		self._root = None

	def assign(self, key, value, pos):
		def _insert(here, key, value, pos):
			if here is None:
				return self.Node(None, key, value, None, pos)
			elif here.key is None:
				return here
			elif key < here.key:
				return self.Node(_insert(here.left, key, value, pos), here.key, here.value, here.right, here.position)
			else:
				return self.Node(here.left, here.key, here.value, _insert(here.right, key, value, pos), here.position)

		self._root = _insert(self._root, key, value, pos)

	def lookup(self, var: str):
		node = self.lookup_node(var)
		return node.value if node is not None else None

	def lookup_node(self, var: str):
		def _search(here, key):
			if here is None or here.key == key:
				return here
			elif key < here.key:
				return _search(here.left, key)
			else:
				return _search(here.right, key)

		return _search(self._root, var)

	def __getitem__(self, item):
		return self.lookup(item)

	def is_empty(self):
		return self._root is None

	def __len__(self):
		def count(current):
			return 0 if current is None else count(current.left) + count(current.right) + 1

		return count(self._root)

	def __iter__(self):
		def iter_node(cur: self.Node):
			if cur is None:
				return
			yield from iter_node(cur.left)
			yield cur.key, cur.value
			yield from iter_node(cur.right)

		yield from iter_node(self._root)

	def _str(self, here):
		if here is None:
			return "null"
		return "(%s: %s[%s] --> %s, %s)" % (
			str(here.key), str(here.value), str(here.position), str(self._str(here.left)), str(self._str(here.right)))

	def __str__(self):
		return self._str(self._root)


class FuncBody:
	"""Function representation in a VarTree"""
	__slots__ = 'args', 'expr'

	def __init__(self, args: list, expr):
		self.args = args
		self.expr = expr


class Reference:
	"""Stack element representation in a VarTree"""
	__slots__ = 'pos'

	def __init__(self, pos):
		self.pos = pos


if __name__ == "__main__":
	V = VarTree()
	print(V.is_empty())
	V.assign("sean", "12", 1)
	print(V)
	print(V.lookup("sean"))
	print(V.lookup_node("sean").position)
	print(V["sean"])
	print(V.is_empty())
