
def sort_people(people_list, field, direction):
    people_list.sort(key=lambda p: p[field], reverse= (direction == 'desc'))



people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]

sort_people(people_list, 'weight', 'desc')
print(people_list)
