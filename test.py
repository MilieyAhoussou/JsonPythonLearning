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

#the following line open/create a file called data.json and convert the dictionary into a json array
with open("data.json", mode="w", encoding="utf_8") as write_file:
    json.dump(dog_data, write_file)

dog_registry = {1:{"name": "Frieda"}}
#we turn the dictionary into a json object
dog_json = json.dumps(dog_registry)
print(dog_json)
#we turn the json object into a python object
new_dog_registry = json.loads(dog_json)
#this line return false, it looks like we lost the primary format of our dictionary
print(dog_registry == new_dog_registry)
#in json, the keys of an object are str but in python they canbe whatever.
#so we see that we we convert the element into a json object the key that was a int became a str
print(new_dog_registry)

dog_data_json = json.dumps(dog_data)
print(dog_data_json)
new_dog_data = json.loads(dog_data_json)
print(new_dog_data)

#convert a json file into a python type object
with open("data.json", mode="r", encoding="utf_8") as read_file:
    frie_data = json.load(read_file)

print(frie_data)
print(type(frie_data))
print(frie_data["name"])
print(json.dumps(dog_registry, indent=" ⮑ "))
