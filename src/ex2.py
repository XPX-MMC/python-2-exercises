def filter_males(people_list):
    new_list = list(filter(lambda p: p['sex'] == 'male', people_list))
    return new_list


people = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]

filtered_list = filter_males(people)
print(filtered_list)