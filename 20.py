my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4, 5]

def analizer(data):
    if isinstance(data, tuple):
        print("Zmienna jest tuplą.")
    elif isinstance(data, list):
        print("Zmienna jest listą.")
    else:
        print("Nieznany typ danych")

analizer(my_list)
analizer(my_tuple)
analizer(3)