# Authur: Nasir Lawal
# Date: 29-Nov-2019

"""
Description: Exercise on how index builtin function
"""

def main():

	alpha = 'abcdefghijklmnop'

	# for only substring
	print(alpha.index('p'))
	# for substring and starting argument
	print(alpha.index('i', 5))
	# for substring, starting and ending argument
	print(alpha.index('c', 0, 15))

if __name__ == "__main__":
	main()