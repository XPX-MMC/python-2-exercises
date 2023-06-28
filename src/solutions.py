from pprint import pprint

def sort_people(people_list, field, direction):
    people_list.sort(key=lambda p: p[field], reverse= (direction == 'desc'))



