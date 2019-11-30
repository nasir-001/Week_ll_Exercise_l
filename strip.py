# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on strip builtin function
"""

def main():

	user_input = input("Enter your name\nWhitespace in the begining and the end\n").strip()

	print(user_input)

	"""
	Note we can alos make like this
	"""

	name = " Aisha Yusuf "
	print(name.strip())

if __name__ == "__main__":
	main()