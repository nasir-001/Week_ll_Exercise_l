# Authur: Nasir Lawal
# Date: 29-Nov-2019

"""
Description: Exercise on find builtin function
"""

def main():

	language = "python is really really awesome"

	# for only substring
	print(language.find('o'))
	# for substring and starting argument
	print(language.find('a', 0))
	# for substring, starting argument and ending argument
	print(language.find('r', 9, 20))

if __name__ == "__main__":
	main()
