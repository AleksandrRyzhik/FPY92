import os
# print(os.getcwd())

with open('3_3_open_file/recipes.txt'
          , encoding='utf-8') as f:
    recipes = f.readlines()

class Recipes:
    def __init__(self, list_recipes):
        self.list_recipes = recipes
        self.cook_book = {}

    def find_dishes(self):
        dishes_list = []
        row = 0
        for word in self.list_recipes:
            row += 1
            if row == 1:
                dishes_list.append(word.strip())
            elif len(word.strip()) == 0:
                row = 0
        return dishes_list
    
    def find_dishes_info(self):
        num_dish = 1
        info_dict = {}
        for word in self.list_recipes:
            if '|' in word:
                if num_dish in info_dict:
                    info_dict[num_dish] += [word.strip().split(' | ')]
                else:
                    info_dict[num_dish] = [word.strip().split(' | ')]
            elif len(word.strip()) == 0:
                num_dish += 1
        return info_dict 

    def get_dict_recipes(self):
        num_dish = 0
        for dish in self.find_dishes():
            num_dish += 1
            info_list = []
            for info in self.find_dishes_info()[num_dish]:
                info_dict = {}        
                info_dict['ingredient_name'] = info[0]
                info_dict['quantity'] = info[1]
                info_dict['measure'] = info[2]
                info_list.append(info_dict)
                self.cook_book[dish] = info_list
        return self.cook_book
    
    def get_shop_list_by_dishes(self, dishes, person_count):
        dict_count = {}
        cook_book = self.get_dict_recipes()
        for dish in dishes:
            for info in self.cook_book[dish]:
                if info['ingredient_name'] in dict_count:
                    dict_count [info['ingredient_name']]['quantity'] += \
                    int(info['quantity']) * person_count
                else:
                    dict_count [info['ingredient_name']] = \
                        {'measure':info['measure']\
                    , 'quantity':int(info['quantity']) * person_count}
        return dict_count

## ЗАДАЧА №3

filenames = ['1', '2', '3']
rel_address_folder = '3_3_open_file/files/'
final_file = '3_3_open_file/files/final_file.txt'

def open_file_to_list(file_name):
    with open (file_name, encoding='utf-8') as f:
        return f.readlines()

file_info = {}

for filename in filenames:
    num_rows = len(open_file_to_list (
        rel_address_folder + filename + '.txt'))
    file_info[filename + '.txt'] = num_rows

value_sequence = sorted(file_info.values())

open(final_file, 'w').close() # очистка итогового файла

def write_append(file, text):
    with open (file, 'a', encoding='utf-8') as f:
        f.write(text)

for rows in value_sequence:
    for name, rn in file_info.items():
        if rows == rn:
            write_append(final_file, name + '\n')
            write_append(final_file, str(rn)+'\n')
            for row in open_file_to_list(rel_address_folder+name):
                write_append(final_file, str(row))
            if value_sequence[-1] == rows:
                pass
            else:
                write_append(final_file, '\n')

# print(cook_book)
# print (sorted(file_info.values()))
recipes = Recipes(recipes)
# print(os.getcwd())
# print(recipes.find_dishes_info())
# print (recipes.find_dishes())
# print(recipes.get_dict_recipes())
print (recipes.get_shop_list_by_dishes(['Запеченный картофель',
                                         'Омлет'], 2))
# recipes.cook_book