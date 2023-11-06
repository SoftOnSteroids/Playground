### Reto programación ###
"""
 Crea 3 funciones, cada una encargada de detectar si una cadena de
 texto es un heterograma, un isograma o un pangrama.
- Debes buscar la definición de cada uno de estos términos.

https://github.com/mouredev/retos-programacion-2023/blob/main/Retos/Reto%20%239%20-%20HETEROGRAMA%2C%20ISOGRAMA%20Y%20PANGRAMA%20%5BF%C3%A1cil%5D/ejercicio.md
 """
import re, string
from unidecode import unidecode

def count_letters(text: str) -> dict:
    text_clean = re.findall(r"[a-z]", unidecode(text).lower())
    letters_count = {}
    for letter in text_clean:
        if letter in letters_count.keys():
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return letters_count

### Heterogram ###
def is_heterogram(text: str) -> bool:
    dict = count_letters(text)
    for val in dict.values():
        if val > 1:
            return False
    return True

### Isograma ###
def is_isogram(text: str) -> int:
    dict = count_letters(text)
    order = 0
    for val in dict.values():
        if order == 0:
            order = val
        elif order != val:
            return 0
    return order

### Pangram ###
def is_pangram(text: str) -> bool:
    dict = count_letters(text)
    if len(string.ascii_lowercase) == len(dict.keys()):
        return True
    return False

heterogram = "Mi frase, bontú."
isogram = "Mi perro pilameola Mi perro pilameola"
pangram = "Un jugoso zumo de piña y kiwi bien frío es exquisito y no lleva alcohol."
frase = pangram
print(f"La frase:\n{frase}\nes un:\nPangrama: {is_pangram(frase)}\nHeterograma: {is_heterogram(frase)}\n"+
      f"Isograma de orden: {is_isogram(frase)}")



### Solucion previa ###
### Heterogram ###
"""
def is_heterogram(text: str) -> bool:
    my_text = text.lower()
    for letter in my_text:
        if letter.isalnum() and my_text.count(letter) > 1:
            return False
    return True

### Isograma ###
def is_isogram(text: str) -> bool:
    text = text.lower().replace(" ", "")
    eval_control = []
    count = 0
    for letter in text:
        if letter.isalnum and eval_control.count(letter) == 0:
            eval_control.append(letter)
            if count != 0 and text.count(letter) != count:
                return "No"
            count = text.count(letter)
    return f"Sí, de {count} nivel."

### Pangram ###
import string

def is_pangram(text: str) -> bool:
    text = text.lower()
    alphabet_lower:str = string.ascii_lowercase
    for letter in alphabet_lower:
        if text.count(letter) == 0:
            return False
    return True"""