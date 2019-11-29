# Authur: Nasir Lawal
# Date: 29-Nov-2019

"""
Description: Exercise on count buitin function
"""

def main():

	lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit"

	print(lorem_ipsum.count('e'))
	print(lorem_ipsum.count('i', 0))
	print(lorem_ipsum.count('o', 0, 20))

if __name__ == "__main__":
	main()