from person import Person


class People:
    def __init__(self):
        self.__people = []

    def addPerson(self, person: Person):
        self.__people.append(person)

    def getPeople(self):
        return self.__people

    def printPeople(self):
        for person in self.__people:
            print(person)