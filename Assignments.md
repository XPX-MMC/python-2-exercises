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

# Ex. 3 Map BMI
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


# Ex. 5 Word Counter
Create a class called `WordCounter`.  This class is to be consumed in the following manner:

```python
    sentence = "This is a test of the emergency broadcast system"
    word_counter = WordCounter(sentence)
    word_counter.count_words()
    print(word_counter.get_word_count())    # Returns the number of all the words.
    print(word_counter.get_shortest_word()) # Returns the length of the shortest word.
    print(word_counter.get_longest_word())  # Returns the length of the longest word.
```

Output:
```
9
1
9
```

Create the `WordCounter` class in your student directory and don't forget to import it in your `assignments.py` file.

# Ex. 6 Tax Man
Consider the following code:
```
    items = [
        {"id": 1, "desc": "clock", "price": 1.00},
        {"id": 2, "desc": "socks", "price": 2.00},
        {"id": 3, "desc": "razor", "price": 3.00},
    ]
    tm = TaxMan(items, "10%")
    tm.calc_total()
    print(tm.get_total())
```

Create a Python class called `TaxMan` that accepts two arguments:
  - A list of items (above)
  - The percent sales tax (string)

The `TaxMan` class has two methods:
  - `calc_total()`: Sums the price of all the items and applies the sales tax (saved to a private instance variable)
  - `get_total()`: Returns the total price including the sales tax.

Output:
```
6.6
```

# Ex. 7 Calculator
Create a `Calculator` class that supports the following:

```python
    calculator1 = Calculator(4, 3)
    calculator1.add()
    print(calculator1.get_result())

    calculator2 = Calculator(4, 3)
    calculator2.sub()
    print(calculator2.get_result())

    calculator3 = Calculator(2, 3)
    calculator3.mul()
    print(calculator3.get_result())

    calculator4 = Calculator(8, 2)
    calculator4.div()
    print(calculator4.get_result())
```

Output:
```
7
1
6
4.0
```
Create the `Calculator` class in your student directory and don't forget to import it in your `assignments.py` file.


# Ex. 8 Car Collector
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
        return <<object>>
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
Create the `CarCollector` class in your student directory and don't forget to import it in your `assignments.py` file.

# Ex. 9  Inheritance
Consider the following base class:
```python
import random


class Character:

    def __init__(self, hit_points):
        self.hit_points = hit_points

    def fight(self, character):
        random_number = random.randint(1, 20)
        character.hit_points -= random_number
```
This base class represents a medieval character (not a character on your computer keyboard).  Create `Fighter` and `Drawf` 
classes that subclass the `Character` class.  Implement the `__repr__()` method in the `Fighter` and `Drawf` classes.  Add some 
logic in the `Character` base class `fight()` method to make sure the hit points do not fall below zero when the `fight()` method 
has finished executing.

The `Fighter` and `Drawf` class must support this usage:
```python
    f = Fighter(18)
    d = Dwarf(15)
    print(f)
    print(d)
    f.fight(d)
    d.fight(f)
    print(f)
    print(d)
```

Example output:
```
Fighter: 18 hit points.
Drawf: 15 hit points.
Fighter: 5 hit points.
Drawf: 0 hit points.
```
Be sure to place all classes in your student directory and don't forget to import them in your `assignments.py` file.


# Ex. 10 Data Class
Given the following data:
```python
    data = [
        "1, 2322, 10.00, False",
        "2, 5435, 60.30, True",
        "3, 3433, 15.63, False",
        "4, 8439, 12.77, False",
        "5, 3424, 11.34, False",
    ]
```

Convert this data that contains a list of `Invoice` data classes, such that when this list is pprinted to the console, 
it appears as the following:
```
[Invoice(invoice_id='1', user_id='2322', amount='10.00', paid='False'),
Invoice(invoice_id='2', user_id='5435', amount='60.30', paid='True'),
Invoice(invoice_id='3', user_id='3433', amount='15.63', paid='False'),
Invoice(invoice_id='4', user_id='8439', amount='12.77', paid='False'),
Invoice(invoice_id='5', user_id='3424', amount='11.34', paid='False')]
```

Be sure to place the `Invoice` data class in your student directory and don't forget to import them in your `assignments.py` file.
