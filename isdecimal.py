# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on isdecimal builtin function
"""

def main():

	user_input = input("Enter any numbers here: ")
	print(user_input.isdecimal())

	"""
	Note: we can still do this 
	"""

	num = '21344356'
	print(num.isdecimal())

	alpha = 'abcdefghi'
	print(alpha.isdecimal())

if __name__ == "__main__":
	main()