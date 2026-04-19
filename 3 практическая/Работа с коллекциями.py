shopping_list = ['роналду', '67', 'месси']
print(f'Список до добавления: {shopping_list}')

shopping_list.append('неймар')
print(f'Список после добавления: {shopping_list}')
shopping_list.append('роналду')
print(f'Список после добавления: {shopping_list}')

unique_items = set(shopping_list)
print(f'Множество unique_items: {unique_items}')