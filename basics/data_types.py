
import requests

response = requests.get("https://api.github.com")

print(response.status_code)


print(f"----" * 10 + "\n Strings")

age = 28
has_license = True

long_stg = """
Name is Hannah
It's a palindrome too
It is a long string that is used to test the string functions in Python. It contains multiple lines and various characters to ensure that the functions work correctly. The string ends with the word system.
"""
print(long_stg)
print(long_stg.startswith("N"))
print(long_stg.endswith("system"))
print(long_stg.find("palindrome")) # i.e its index 
print(long_stg.count("to"))

print(f"----" * 10 + "\n List: ordered, mutable(i.e., can be changed), allows duplicates")

lst = ["Alice", age, True, has_license]

lst.remove("Alice")
lst.insert(0, "Alice")
print(lst)

print(lst.count(age))
print(lst.index(has_license))
#lst.sort() , lst.reverse() => TypeError: '<' not supported between instances of 'int' and 'str'
new_lst = lst.copy()
print(new_lst)



print(f"----" * 10 + "\n Dictionaries: unordered, mutable(i.e., can be changed), no duplicates")

person = {
  "name": "Alice",
  "age": 30,
  "city": "New York"
}

print(person.keys())
print(person.values())
print(person.items())

person.update(
  {
    "age": 31,
    "job": "Accountant"
  }
)

if "job" not in person:
  print("Career not found")
else:
  print("Career found")

print(person)

print(f"----" * 10 + "\n Tuples: ordered, immutable(i.e., cannot be changed), allows duplicates")

coordinates = (10.0, 20.0)
print(coordinates[0]) # 10.0

print(f"----" * 10 + "\n Sets: unordered, mutable(i.e., can be changed), no duplicates")

unique_numbers = {1,1, 2, 3, 4, 5}
unique_numbers.add(2)
print(unique_numbers) # {1, 2, 3, 4, 5} - no duplicates
unique_numbers.remove(2) # error if 2 is not in the set

unique_numbers.discard(2) # no error if 2 is not in the set