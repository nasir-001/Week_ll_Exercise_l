# Authur: Nasir Lawal
# Date: 29-Nov-2019

"""
Description: Exercise on endswith builtin function
"""

def main():
	
	qoute = 'Behind every great furtune there is a crime'

	# for only substring
	print(qoute.endswith('e'))
	# for substring and starting argument
	print(qoute.endswith('rime', 10))
	# for substring, starting argument and ending argument
	print(qoute.endswith('eat', 0, 9))


if __name__ == "__main__":
	main()