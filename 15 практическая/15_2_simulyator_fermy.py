def etapa_1(input_string):
    
    print("=" * 50)
    print("ЭТАП 1: База растений")
    print("=" * 50)
       
    plants = input_string.split(", ")
    
    print("Растения на ферме:")
    for plant in plants:
        print(plant)
    
    return plants


def etapa_2(hybrids_string, plant1, plant2):
    
    print("\n" + "=" * 50)
    print("ЭТАП 2: Проверка возможности скрещивания")
    print("=" * 50)
        
    hybrids = {}
       
    pairs = hybrids_string.split(";")
    for pair in pairs:
        if "=" in pair:
            parents, child = pair.split("=")
            parent1, parent2 = parents.split("+")
                        
            key1 = parent1 + "+" + parent2
            key2 = parent2 + "+" + parent1
            hybrids[key1] = child
            hybrids[key2] = child
        
    key = plant1 + "+" + plant2
    if key in hybrids:
        print(f"Получен гибрид: {hybrids[key]}")
        return hybrids[key]
    else:
        print("Эти растения нельзя скрестить")
        return ""


def etapa_3_1(name1, color1, name2, color2):
    
    print("\n" + "=" * 50)
    print("ЭТАП 3.1: Определение цвета гибрида")
    print("=" * 50)
        
    if name1.lower() < name2.lower():
        hybrid_color = color1
        print(f"Цвет гибрида: {hybrid_color} (т.к. '{name1}' < '{name2}')")
    elif name2.lower() < name1.lower():
        hybrid_color = color2
        print(f"Цвет гибрида: {hybrid_color} (т.к. '{name2}' < '{name1}')")
    else:  
        hybrid_color = color1
        print(f"Цвет гибрида: {hybrid_color} (названия одинаковы, берем цвет первого растения)")
    
    return hybrid_color


def etapa_3_2(size1, size2):
    
    print("\n" + "=" * 50)
    print("ЭТАП 3.2: Определение размера гибрида")
    print("=" * 50)
        
    size_order = {"малый": 0, "средний": 1, "крупный": 2}
    
    if size1 == size2:
        hybrid_size = size1
        print(f"Размер гибрида: {hybrid_size} (размеры одинаковы)")
    else:
        
        sizes = [size1, size2]
        sizes.sort(key=lambda x: size_order[x])
        hybrid_size = sizes[0] + "/" + sizes[1]
        print(f"Размер гибрида: {hybrid_size} (размеры разные, записываем через /)")
    
    return hybrid_size


def etapa_3_3(growth1, growth2):
    
    print("\n" + "=" * 50)
    print("ЭТАП 3.3: Определение скорости роста гибрида")
    print("=" * 50)
        
    growth_order = {"медленный": 0, "средний": 1, "быстрый": 2}
        
    if growth_order[growth1] <= growth_order[growth2]:
        hybrid_growth = growth1
        print(f"Скорость роста гибрида: {hybrid_growth} (наименьшая скорость)")
    else:
        hybrid_growth = growth2
        print(f"Скорость роста гибрида: {hybrid_growth} (наименьшая скорость)")
    
    return hybrid_growth


def get_plant_info(plants, name):
    
    for plant in plants:
        parts = plant.split()
        if parts[0] == name:
            return parts[1], parts[2], parts[3]
    return "", "", ""


def print_hybrid_info(name1, color1, size1, growth1, 
                      name2, color2, size2, growth2,
                      hybrid_color, hybrid_size, hybrid_growth):
    
    print("\n" + "=" * 50)
    print("ИТОГОВАЯ ИНФОРМАЦИЯ О ГИБРИДЕ")
    print("=" * 50)
    print(f"Родитель 1: {name1} ({color1}, {size1}, {growth1})")
    print(f"Родитель 2: {name2} ({color2}, {size2}, {growth2})")
    print("-" * 50)
    print(f"Цвет гибрида: {hybrid_color}")
    print(f"Размер гибрида: {hybrid_size}")
    print(f"Скорость роста гибрида: {hybrid_growth}")


def main():
    
    plants_string = "Роза красный средний быстрый, Тюльпан желтый малый средний, Подсолнух оранжевый крупный медленный"
        
    hybrids_string = "Роза+Тюльпан=Розотюльпан;Тюльпан+Подсолнух=Тюльпансолнух"
    plant1_name = "Роза"
    plant2_name = "Тюльпан"
        
    plants = etapa_1(plants_string)
    print()
        
    color1, size1, growth1 = get_plant_info(plants, plant1_name)
    color2, size2, growth2 = get_plant_info(plants, plant2_name)
        
    if color1 == "" or color2 == "":
        print("Ошибка: одно из растений не найдено в базе!")
        return
       
    hybrid = etapa_2(hybrids_string, plant1_name, plant2_name)
    print()
        
    if hybrid != "":
        print("=" * 50)
        print("ЭТАП 3: Определение характеристик гибрида")
        print("=" * 50)
                
        hybrid_color = etapa_3_1(plant1_name, color1, plant2_name, color2)
                
        hybrid_size = etapa_3_2(size1, size2)
               
        hybrid_growth = etapa_3_3(growth1, growth2)
                
        print_hybrid_info(plant1_name, color1, size1, growth1, 
                         plant2_name, color2, size2, growth2,
                         hybrid_color, hybrid_size, hybrid_growth)


main()