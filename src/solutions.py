from pprint import pprint

def sort_people(people_list, field, direction):
    people_list.sort(key=lambda p: p[field], reverse= (direction == 'desc'))


def filter_male(people_list):
    new_list = list(filter(lambda p: p['sex'] == 'male', people_list))
    return new_list


def calc_bmi(people_list2): 
    bmi_list = list(map(lambda person: {**person, 'bmi': round(person['weight_kg'] / person['height_meters'] ** 2, 1)}, people_list2)) 
    return bmi_list