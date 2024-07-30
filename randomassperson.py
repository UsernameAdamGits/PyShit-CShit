namer = 'Shit'
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, what's up, {self.name}?")

person2 = Person('Sanders')
person2.talk()
