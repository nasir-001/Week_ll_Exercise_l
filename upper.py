# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on upper builtin function
"""

def main():

	alpha = 'abcdefGHIJ'

	for x in alpha: # loop through the alpha
		if x == x.lower(): # check if x is in lowercase
			print(x.upper()) # if it's in lowercase convert and then print
		else:				 # if it's not in lowercase
			print(x)		 # just print 

if __name__ == "__main__":
	main()