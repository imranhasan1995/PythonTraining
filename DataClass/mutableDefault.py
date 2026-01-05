from dataclasses import dataclass, field
from typing import List

@dataclass
class Course:
    name: str
    total: int = field(default=0)
    students: List[str] = field(default_factory=list)

course1 = Course("Math")
course2 = Course("Science", 100, ["Alice", "Bob"])
course1.students.append("Charlie")
course1.total = 50
print(course1)
print(course2)