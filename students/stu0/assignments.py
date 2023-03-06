
def ex1():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)


def ex2():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_people(people_list)
    print(filtered_list)


def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)


def ex4():
    people_list = [
        {'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
        {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))


def ex5():
    pass


def ex6():
    pass


def ex7():
    pass


def ex8():
    pass


def ex9():
    pass


def ex10():
    pass


#
# Place your functions here...
#


def sort_people(people, field, direction):
    people.sort(key=lambda p: p[field], reverse=False if direction == "asc" else True)


def filter_people(people):
    return list(filter(lambda p: p['sex'] == 'male', people))


def calc_bmi(people):
    return list(map(lambda p:
                    {
                        'id': p['id'],
                        'name': p['name'],
                        'weight_kg': p['weight_kg'],
                        'height_meters': p['height_meters'],
                        'bmi': round(p['weight_kg'] / p['height_meters'] ** 2, 1)
                    },
                    people))


def get_people(people):
    return [p['name'] for p in people if p['age'] >= 15]
