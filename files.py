# Files handling
# How to work with file imports, path and relative imports explained in StackOverflow:
# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912

import os
FILES_DIR_URL = "./Theory/Excercises/Files/"

def play_with_files():
    # txt file
    FILE_URL = FILES_DIR_URL + "txt_file.txt"

    txt_file = open(FILE_URL, "w+")

    txt_file.write("Mi nombre es Franco\nMe gusta programar en Python\nMe encanta poder escribir en un archivo de texto.\nY poder leerlo.")

    print (f"Pointer position: {txt_file.tell()}")
    txt_file.seek(0)

    print(txt_file.read())

    if not txt_file.closed:
        txt_file.close()
    
    # Right way to open a file
    with open(FILE_URL, "w+", encoding="UTF-8") as file:
        file.write(" Siguiente:\n".join([f"Línea nueva nro {i+1}." for i in range(5)]))

    # os.remove(FILE_URL)

class Person:
    def __init__(self, name, surname) -> None:
        self.__name: str = name
        self.__surname = surname
    
    def set_name(self, new_name):
        self.__name = new_name

    def present(self):
        print(f"Me llamo {self.__name} {self.__surname}")

    def talk_to(self, persona):
        print(f"Hola, {persona.__name}")
        persona.__name = "Pepe"
        print(f"Te rebauticé a {persona.__name} {persona.__surname}")

def ejecutar_codigo():
    my_person = Person(surname="Coloccini", name="Franco")

    new_person = Person("Jose", "Perez")

    my_person.talk_to(new_person)
    new_person.present()
    new_person.set_name("Random2")
    new_person.present()
    new_person.__name = "Random"
    print ("El nombre nuevo es: "+ new_person.__name)
    new_person.present()

def hacer_hablar (persona):
    persona.present()

### JSON files ###

import json

class Car():
    def __init__(self, wheels = 4, doors = 5, speed = 150):
        self.wheels= wheels
        self.doors= doors
        self.speed= speed

def play_with_json():
    print (f"Current dir: {os.getcwd()}")
    my_person = Person(name="Franco", surname="Coloccini")
    my_json_person = json.dumps(my_person.__dict__)

    my_car = Car()
    my_json_car = json.dumps(my_car.__dict__)

    print (my_json_person)
    # print (my_json_car)

    my_json_car_file = open(FILES_DIR_URL + "my_car.json", "w+")
    my_json_car_file.write(my_json_car)
    my_json_car_file.seek(0)
    print(type(my_json_car_file))
    print (my_json_car_file.read())
    my_json_car_file.close()

    my_new_json_car = json.load(open(FILES_DIR_URL + "my_car.json"))
    print (my_new_json_car)


play_with_json()