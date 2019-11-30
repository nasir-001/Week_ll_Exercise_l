# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on rpartition builtin function
"""

def main():

	user_input = input("Enter your name: ")
	print(user_input.rpartition(' '))

	"""
	Note: we can also do this
	"""
	name = 'Musa Lawal'
	print(name.rpartition(' '))

if __name__ == "__main__":
	main()