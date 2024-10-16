from Person import Person


class People:
    def __init__(self):
        self.__people = []

    def add_person(self, person: Person):
        self.__people.append(person)

    def remove_person(self, person: Person):
        if person in self.__people:
            self.__people.remove(person)
        else:
            print("Person not found in list")

    def getPeople(self):
        return self.__people

    def printPeople(self):
        for person in self.__people:
            print(person)
    def insertPerson(self, person: Person,  index: int):
        self.__people.insert(index, person)
