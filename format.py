# Authur: Nasir Lawal
# Date: 29-Nov-2019

"""
Description: Exercise on format builtin function
"""

def main():

	firstName = "Nasir"
	middleName = "Lawal"
	lastName = "Aliyu"

	# first method
	print("{}, {}, {}".format(firstName, middleName, lastName))
	# second method
	print(f"{firstName}, {middleName}, {lastName}")

if __name__ == "__main__":
	main()
