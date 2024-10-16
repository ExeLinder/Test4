class Person:
    def __init__(self, id, firstname, lastname, age, email):
        self.__id = id
        self.__firstname = firstname
        self.__lastname = lastname
        self.__age = age
        self.__email = email

    def display_info(self):
        print(f"ID: {self.__id}")
        print(f"Имя: {self.__firstname}")
        print(f"Фамилия: {self.__lastname}")
        print(f"Возраст: {self.__age}")
        print(f"Электронная почта: {self.__email}")