# Python Intro II Assignments
Submit a PR for each exercise.

# Ex. 1 Sort with Lambda
Given the following list:

```python
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `sort_people()` that accepts the following arguments:
- A list of people
- A field that will used to sort the people (e.g. name, age, weight, etc...)
- The sort direction (e.g. asc or desc)

This function must use a Lambda function to perform the sort.

Usage:

```python
def ex1():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    sort_people(people_list, 'weight', 'desc')
    print(people_list)
```

Output:
```
[{'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1},
 {'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}, 
 {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3}]
```

# Ex. 2 Filter
Given the following list:

```python
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `filter_males()` that accepts the following arguments:
- A list of people

This function returns only the males from the list of people.

The function is used in the following manner:

```python
def ex2():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    filtered_list = filter_males(people_list)
    print(filtered_list)
```
Output:
```
[{'name': 'alice', 'age': 20, 'weight': 160, 'sex': 'male', 'id': 1}, 
{'name': 'bob', 'age': 10, 'weight': 130, 'sex': 'male', 'id': 2}]
```

# Ex. 3 Map
Given the following list:

```python
people_list = [
    {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
    {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
]
```

Create a function called `calc_bmi()` that accepts this list and calculates the BMI (Body Mass Index) for
each person.  The formula for BMI is:  BMI = weight/height<sup>2</sup>.  This can be expressed in python
using this syntax: `round(weight / height ** 2, 1)`.

The `calc_bmi()` function must use the `map()` function.

Usage:
```python
def ex3():
    people_list = [
        {'id': 2, 'name': 'bob',     'weight_kg': 90, 'height_meters': 1.7},
        {'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8},
    ]
    new_people_list = calc_bmi(people_list)
    print(new_people_list)
```

Output:
```
[{'id': 2, 'name': 'bob', 'weight_kg': 90, 'height_meters': 1.7, 'bmi': 31.1}, 
{'id': 3, 'name': 'charlie', 'weight_kg': 80, 'height_meters': 1.8, 'bmi': 24.7}]
```

# Ex. 4 List Comprehension
Given the following list:

```python
people_list = [
    {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
    {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
    {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
]
```

Create a function called `get_people()` that accepts a list of people.  Use a list comprehension
to return the names of people that are equal to or greater than 15 years old.

Usage:
```python
def ex4():
    people_list = [
        {'name': 'alice',   'age': 20, 'weight': 160, 'sex': 'male',   'id': 1},
        {'name': 'bob',     'age': 10, 'weight': 130, 'sex': 'male',   'id': 2},
        {'name': 'charlie', 'age': 15, 'weight': 120, 'sex': 'female', 'id': 3},
    ]
    print(get_people(people_list))
```

Output:
```
['alice', 'charlie']
```

# Ex. 5 Car Collector
Consider the following class:
```python
class CarCollector:
    car_list = [
        {"id": 1, "price": 10000},
        {"id": 2, "price": 20000},
        {"id": 3, "price": 30000},
    ]
    car_dict = {
        1: "Ford",
        2: "Mazda",
        3: "Chevy"
    }

    @staticmethod
    def get_data():
        return list(map(CarCollector._combine, CarCollector.car_list))
    
    @staticmethod
    def _combine(c):
        # Todo...
        return <<an object>>
```

Complete the `_combine()` method so that the `get_data()` method returns the following:
```
[{'id': 1, 'make': 'Ford', 'price': 10000},
 {'id': 2, 'make': 'Mazda', 'price': 20000},
 {'id': 3, 'make': 'Chevy', 'price': 30000}]
```

Usage:
```python
  pprint(CarCollector.get_data())
```
Add this class to your student directory.  Make sure to import it at the top of your `assignments.py` file:

```python
from students.stu<your student id>.CarCollector import CarCollector
```


# Ex. 6 


# Ex. 7 


# Ex. 8 


# Ex. 9 


# Ex. 10


