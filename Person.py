class Person:
    def __init__(self, id, firstname, lastname, age, email):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__email = email

    def __str__(self):
        return f'Person {self.__id} {self.__firstname}, {self.__lastname}, {self.__age}, {self.__email}'