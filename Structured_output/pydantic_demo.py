from pydantic import BaseModel
from typing import Optional
class Person(BaseModel):

    name: str
    age: Optional[int] = None

new_student = {'name':"Alice"}
new_student = {'name':"Alice", 'age': 30}
student = Person(**new_student)
print(type(student))

