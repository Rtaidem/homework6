my_dict = {'Felix': 1999, 'Dima': 2000, 'Masha': 2002}
print(my_dict)
print(my_dict['Felix'])
my_dict['Anton'] = 1990
print(my_dict['Anton'])
my_dict.update({'Sasha': 2005,
                'Inna': 2004})
a = my_dict.pop('Dima')
print(a)
print(my_dict)


my_set = {1, 2, 'apple', 4, True, 5, 2, 1,}
print(my_set)
my_set.add(6)
my_set.add(3)
my_set.discard(2)
print(my_set)