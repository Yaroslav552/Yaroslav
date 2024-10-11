
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(a=25, b='хи - хи', c=False)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1, 'у меня др', False]
values_dict = {'a': 5, 'b': 'cg go', 'c': True}
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)



