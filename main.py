
# Update with the exercise you are trying to test
from src import solutions


def main():

    people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]   
    
    # solutions.sort_people()
    solutions.sort_people(people_list, 'name', 'desc')
    print(people_list)
if __name__ == '__main__':
    main()
