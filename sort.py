import numpy as np
def generate_unordered_list(list_edge):
    unordered_list = list(range(-list_edge, list_edge + 1))
    np.random.shuffle(unordered_list)
    
    return unordered_list

def generate_uneven_list(size):
    uneven_list = []
    
    for i in range(size):
        num = np.random.randint(1, 1001)
        uneven_list.append(num)
    
    return uneven_list

def avg_sort(numbers_list, old_list = None):
    if len(numbers_list) <= 1 or old_list == numbers_list:
        return numbers_list
    avg = sum(numbers_list) / len(numbers_list)
    halfs = [[],[]]
    halfs[0] = [x for x in numbers_list if x < avg]
    halfs[1] = [x for x in numbers_list if x >= avg]
    return  avg_sort(halfs[0], numbers_list) + avg_sort(halfs[1], numbers_list)



list_edge = 500
numbers = generate_unordered_list(list_edge)

print("Unordered List:",numbers)

print("Ordered List:",avg_sort(numbers))

numbers = generate_uneven_list(list_edge)

print("Unordered Uneven List:",numbers)

print("Ordered Uneven List:",avg_sort(numbers))