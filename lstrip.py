# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on lstrip builtin function
"""

def main():

	user_input = input("Enter your name\nWith whitespace at the begining\n").lstrip()
	print(user_input)

	"""
	This will also work
	"""

	name = " Musa Lawal"
	print(name.lstrip())

if __name__ == "__main__":
	main()