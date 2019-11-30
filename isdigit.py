# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on isdigit builtin function
"""

def main():

	name = 'Aisha'
	# return false because name is not digit
	print(name.isdigit())

	num = '13455556'
	# return true because num is digit
	print(num.isdigit())

	char = '%$%$%^*()'
	# return false char is no digit
	print(char.isdigit())

if __name__ == "__main__":
	main()