
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)



values_list = [1, 'у меня др', False]
values_dict = {'a': 5, 'b': 'cg go', 'c': True}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)



