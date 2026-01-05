from enum import Enum, unique
class Season(Enum):
    SPRING = 1
    SUMMER = 2
    AUTUMN = 3
    WINTER = 4

print(Season.AUTUMN.name)
print(Season.SPRING.value)

for s in Season:
    print(f"Name: {s.name}, Value: {s.value}")

class Animal(Enum):
    DOG = 1
    CAT = 2
    LION = 3

sounds = {
    Animal.DOG: "bark",
    Animal.LION: "roar"
}

print(sounds[Animal.LION])

print(Animal.DOG is Animal.LION)
print(Animal.DOG == Animal.LION)



@unique
class subjects(Enum):
   ENGLISH = 1
   MATHS = 2
   GEOGRAPHY = 3
   BANGLA = 4

subjects = Enum("subject", "ENGLISH MATHS SCIENCE SANSKRIT")
print(subjects.ENGLISH.value)
print(subjects.MATHS)
print(subjects.SCIENCE)
print(subjects.SANSKRIT)