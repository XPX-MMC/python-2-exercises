
# Update with the exercise you are trying to test
from src import solutions


def main():
 
    people_list2 = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]


    new_people_list = solutions.calc_bmi(people_list2) 
    print(new_people_list)
    
    



if __name__ == '__main__':
    main()
