# Authur: Nasir Lawal
# Date: 30-Nov-2019

"""
Description: Exercise on lower builtin function
"""

def main():

	alpha = 'ABcDEFGHIJ'

	for a in alpha: # loop through the alpha
		if a.islower(): # if lowercase letter is found in the iteration
			print("This is a lowercase aplhabet " + a) # print statement for lowercase
		else:										   # if not lowercase 
			print("This not a lowercase aplhabet " + a)# print statement for uppercase

	"""
	Note we can still convert the uppercase into lowercase if needed
	"""

	for x in alpha: # loop through the alpha
		if x == x.upper(): # check if x is in uppercase
			print(x.lower()) # if it's then convert it to lowercase and print it

if __name__ == "__main__":
	main()