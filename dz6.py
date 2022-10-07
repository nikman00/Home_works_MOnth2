import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color
        self.__full_name = []
        self.__email = []
        self.__file_name = []
        self.__color = []

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    while True:
        print("_Меню опций____")
        print("1 - Считать имена и фамилии\n")
        print("2 - Считать все емайлы\n")
        print("3 - Считать названия файлов\n")
        print("4 - Считать цвета\n")
        print("5 - Выход")
        choice = int(input("Выборите опцию меню: "))
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content = file.read()
            if choice == 1:
                name = re.findall(r"[A-Z](?:[a-zA-Z]|-|'|)*\s", content)
                full_name = open("full_name.txt", "w")
                i = 0
                while i < len(name) - 1:
                    print(name[i] + name[i + 1])
                    full_name.write(name[i] + name[i + 1] + "\n")
                    i += 2
            elif choice == 2:
                email1 = re.findall(r"(?:\w)*@[^\s]*", content)
                email = open("email.txt", "w")
                for i in email1:
                    email.write(i + "\n")
                    print(i)
            elif choice == 3:
                file_names = re.findall(r"[A-Z](?:[a-zA-Z])*\.[^\s]*", content)
                file_name = open("name_of_file.txt", "w")
                for i in file_names:
                    file_name.write(i + "\n")
                    print(i)

            elif choice == 4:
                colors = re.findall(r"#[^\s]*", content)
                color = open("color.txt", "w")
                for i in colors:
                    color.write(i + "\n")
                    print(i)

            elif choice == 5:
                break
            else:
                print("такой команды нет ")
