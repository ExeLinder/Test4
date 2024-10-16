from Person import Person


class People:
    def __init__(self):
        self.people = []

    def add_person(self, person:Person):
        self.people.append(person)

    def remove_person(self, person:Person):
        self.people.remove(person)