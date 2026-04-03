import json
# ça c'est un dictionaire en python
food_ratings = {"Organic dog food": 2, "human food": 10}
print(json.dumps(food_ratings))

numbers_present = {1: True, 2: True, 3:False}
print(json.dumps(numbers_present))

number_present2 = {(1,2): True, 3:False}
#some datatypes in python can't be use as keys in json format
# the skipkeys argument ignore the non usable keys but the informationcan be lost
print(json.dumps(number_present2, skipkeys=True))

#it possible to make some eidt during the serialization into json format, for example :
#here we use the sort_keys arg to sort the dictionary by keys

toys_conditions = {"chew bone" : 7, "ball": 3, "sock": -1}
json.dumps(toys_conditions, sort_keys=True)

dog_data = {
  "name": "Frieda",
  "is_dog": True,
  "hobbies": ["eating", "sleeping", "barking",],
  "age": 8,
  "address": {
    "work": None,
    "home": ("Berlin", "Germany",),
  },
  "friends": [
    {
      "name": "Philipp",
      "hobbies": ["eating", "sleeping", "reading",],
    },
    {
      "name": "Mitch",
      "hobbies": ["running", "snacking", "dancing"],
    },
  ],
}

with open("data.json", mode="w", encoding="utf_8") as write_file:
    json.dump(dog_data, write_file)