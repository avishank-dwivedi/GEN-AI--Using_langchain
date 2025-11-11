from typing import TypedDict
class Person(TypedDict):
    name: str
    age: int
    
new_persinon: Person = {
    "name": "Alice",
    "age": 30
}
print(new_persinon)