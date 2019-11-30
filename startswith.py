# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on startwith builtin function
"""

def main():

	sentence = "Great things takes time"

	# for only substring
	print(sentence.startswith('G'))
	# for substring and starting argument
	print(sentence.startswith('t', 6))

	"""
	Note we can still convert the letter
	"""
	print(sentence.startswith('g'.upper()))

if __name__ == "__main__":
	main()