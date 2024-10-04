def raspakovka(**kwargs):
    s = 0
    for i, j in kwargs.items():
        if type(i) == int:
            s += i
        if type(i) == str:
            s += len(i)
        if type(j) == int:
            s += j
        if type(j) == str:
            s += len(j)
    return s

def calculate_structure_sum(data):
    s = 0
    for i in range(len(data)):
        if type(data[i]) == int:
            s += data[i]
        if type(data[i]) == str:
            s += len(data[i])
        if type(data[i]) == list:
            s += calculate_structure_sum(data[i])
        if type(data[i]) == dict:
            s += raspakovka(**data[i])
        if type(data[i]) == tuple:
            s += calculate_structure_sum(data[i])
        if type(data[i]) == set:
            for j in data[i]:
                list_ = []
                list_.append(j)
            s += calculate_structure_sum(list_)
    return s

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)