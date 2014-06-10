
# dictionary: melons
# key: melon name
# value: list containing melon-price, and is-seedless

melons = {
    'Honeydew':[0.99, True],
    'Crenshaw':[2.99, False],
    'Crane':[2.50, False],
    'Casaba':[2.50, False],
    'Cantaloupe':[0.99, False]
}

def update_melons(dictionary_new_data):
    """takes a dictionary with key: melon name, value: list of new data"""
    for melon in melons.keys():
        if melon in dictionary_new_data.keys():
            melons[melon] += dictionary_new_data[melon]
        else:
            melons[melon] += [None]