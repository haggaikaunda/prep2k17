from util import *

passed = 0

def test_upsample():
	print("\ntesting question 2: upsample")
	message = [1, 2, 3]
	n = 2
	expected = [1, 1, 2, 2, 3, 3]

	actual = upsample(message, n)

	print_status(expected, actual, 2)

def test_extend_code():
	print("\ntesting question 3: extend_code")
	message = [1, 2, 3]
	n = 2
	expected = [1, 2, 3, 1, 2, 3]
	actual = extend_code(message, n)

	print_status(expected, actual, 3)

def test_multiply_lists():
	print("\ntesting question 4: extend_code")
	lst1, lst2 = [2, 2, 2], [2, 4, 6]
	expected = [4, 8, 12]
	print(f"runing multiply_lists({lst1}, {lst2})")
	actual = multiply_lists(lst1, lst2)

	print_status(expected, actual, 4)

def test_add_lists():
	print("\ntesting question 5: add_lists")
	lst1, lst2 = [2, 2, 2], [2, 4, 6]
	expected = [4, 6, 8]
	print(f"runing add_lists({lst1}, {lst2})")
	actual = add_lists(lst1, lst2)

	print_status(expected, actual, 5)

def test_encode_message():
	print("\ntesting question 6: encode_message")
	message = [1, 2, 3]
	code = [1, -1, 1, -1]

	expected = [1, -1, 1, -1, 2, -2, 2, -2, 3, -3, 3, -3]
	print(f"running encode_message({message}, {code})")
	actual = encode_message(message, code)

	print_status(expected, actual, 6)
	print("\n")


def print_status(expected, actual, q):
	if not actual == expected:
		print(f"question {q} fails:\nExpected {expected} but got {actual}.\n")
	else:
		print(f"question {q} passes!")
		


if __name__ == '__main__':
	test_upsample()
	test_extend_code()
	test_multiply_lists()
	test_add_lists()
	test_encode_message()

