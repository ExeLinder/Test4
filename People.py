from Person import Person


class People:
    def __init__(self):
        self.people = []

    def add_person(self, person:Person):
        self.people.append(person)

    def remove_person(self, person:Person):
        if person in self.people:
            self.people.remove(person)
        else:
            print("Person not found in list")

    def getPeople(self):
        return self.__people

    def printPeople(self):
        for person in self.__people:
            print(person)