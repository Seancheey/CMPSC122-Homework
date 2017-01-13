operators=['+','-','*','/','**','(',')']

def get_item(str):
	out=""
	non_blank_started=False
	is_number=False
	for i in range(0,len(str)):
		if is_num(str[i]):
			if non_blank_started and not is_number:
				return out, i
			else:
				non_blank_started=True
				is_number=True
				out+=str[i]
		elif is_opt(str[i]):
			if non_blank_started and is_number:
				return out, i
			else:
				non_blank_started=True
				is_number=False
				out+=str[i]
	return out, len(str)

def new_split_iter(str):
	while True:
		a, i = get_item(str)
		str.split(2)

def is_num(expr):
	if expr=='.':
		return True
	try:
		a = int(expr)
		return True
	except:
		return False

def is_opt(expr):
	for i in operators:
		if i==expr:
			return True
	return False

if __name__=="__main__":
	a="1+3/4"
	for i in new_split_iter(a):
		print(i+",")
	print("done")