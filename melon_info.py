"""
melon_info.py - Prints out all the melons in our inventory

"""

from melons import melons


def print_melon(name, price, seedless): # changed order to reflect dictionary
	hashasnot = 'have'
	if seedless:
		hashasnot = 'do not have'
	
	print "%ss %s seeds and are $%0.2f" % ( name, hashasnot, price)



if __name__ == '__main__':
    for i in melons.iteritems():

    	melon_name = i[0]
    	melon_price = i[1][0]
    	melon_seedless = i[1][1]

        print_melon(melon_name, melon_price, melon_seedless)
